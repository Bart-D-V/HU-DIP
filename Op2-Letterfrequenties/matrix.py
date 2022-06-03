import numpy as np
from main import *
from collections import defaultdict


# loads a matrix
def load_matrix(language):
    matrix = np.load(f'matrix/{language}.npy')
    print(f'loaded {language} matrix')
    return matrix


# fills a matrix with frequency data of bigrams
def fill_matrix(bigram_frequencys, matrix):
    for bigram, frequency in bigram_frequencys.items():
        kolom = CHARACTERS.index(bigram[0])
        row = CHARACTERS.index(bigram[1])
        matrix[kolom][row] = frequency

    return matrix


# makes the text lowercase and replaces every character not in ascii with '_'
def prep_line(line):
    line = line.lower()
    for i in range(len(line)):
        if line[i] not in CHARACTERS:
            line = line.replace(line[i], '_')
    return line


# maps each line into a count of the bigrams in the line
def mapper_bigram_count(line_data):
    bigram_count = {}
    line_data = prep_line(line_data)
    for i in range(len(line_data) - 1):

        key = line_data[i] + line_data[i + 1]
        if key in bigram_count:
            bigram_count[key].append(1)
        else:
            bigram_count[key] = [1]

    return bigram_count


# shuffles the same bigrams together
def shuffler(map_result):
    shuffled = defaultdict(list)
    for dict in map_result:
        for key, value in dict.items():
            for item in value:
                shuffled[key].append(item)

    return shuffled


# reduces the data by counting the list of 1's
def reducer_sum_bigrams(bigram_data):
    return bigram_data[0], sum(bigram_data[1])


# calculates the frequentie of each bigram
def bigrams_frequency(bigrams_total):
    bigram_frequency = {}
    for bigram, total in bigrams_total.items():
        bigram_frequency[bigram] = total / sum(bigrams_total.values()) * 100

    return bigram_frequency


# creates bigram frequentie matrix for languages
def map_reduce_language_matrices():
    # create for each language a 27x27 matrix
    matrices = dict(map(lambda lan: (lan, np.zeros((MAT_SIZE, MAT_SIZE))), LANGUAGES))
    # load in texts
    inputs = dict(
        map(lambda lan: (lan, list(open(f'train_data/{lan}.txt', 'r', encoding='utf8').readlines())), LANGUAGES))
    # dict to store from mapper and reducer
    map_reduce_data = {}
    for l in LANGUAGES:
        # map, shuffle and reduce the input text
        map_reduce_data[l] = list(map(mapper_bigram_count, inputs[l]))
        map_reduce_data[l] = shuffler(map_reduce_data[l])
        map_reduce_data[l] = dict(map(reducer_sum_bigrams, map_reduce_data[l].items()))
        map_reduce_data[l] = bigrams_frequency(map_reduce_data[l])

        # fill in matrix with bigram frequenties and save
        matrices[l] = fill_matrix(map_reduce_data[l], matrices[l])
        np.save(f'matrix/{l}.npy', matrices[l])
        print(f'created and saved {l} matrix')

    return 0


map_reduce_language_matrices()
