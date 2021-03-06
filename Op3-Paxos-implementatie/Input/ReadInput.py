from Messages import Message
from Input.Event import Event
from Computers import Acceptor, Proposer

proposers, acceptors = {}, {}

""" pakt event data en geeft een propose message terug """
def propose(tick, message_type, msg_info):
    proposer_id, proposed_value = [int(msg_info[0]), int(msg_info[1])]
    proposers[proposer_id].set_proposed_value(proposed_value)
    message = Message(None, proposers[proposer_id], message_type)

    return Event(tick, [], [], message)


""" krijgt een computer type en ids en geeft een lijst terug met die computers."""
def get_computers(computer_info):
    computer_type = computer_info[0]
    computer_ids = [int(id) for id in computer_info[1:]]
    computers = []

    if computer_type == 'ACCEPTOR':
        for acceptor in computer_ids:
            computers.append(acceptors[acceptor])

    elif computer_type == 'PROPOSER':
        for proposer in computer_ids:
            computers.append(proposers[proposer])

    return computers


""" pakt event data en geeft een event met alle computers die failen."""
def fail(tick, message_type, computers):
    failed = get_computers(computers)
    message = Message(None, None, message_type)

    return Event(tick, failed, [], message)


""" pakt event data en geeft een event met alle computers de recovered worden."""
def recover(tick, message_type, computers):
    recovered = get_computers(computers)
    message = Message(None, None, message_type)

    return Event(tick, [], recovered, message)

""" maakt een event bij het passende message type en geeft hem als return."""
def make_event(line):
    tick, message_type, *msg_info = line.split()
    tick = int(tick)

    if message_type == Message.PROPOSE:
        event = propose(tick, message_type, msg_info)
    elif message_type == 'FAIL':
        event = fail(tick, message_type, msg_info)
    elif message_type == 'RECOVER':
        event = recover(tick, message_type, msg_info)

    return event


"""
leest de file waar de comments voor de simulatie staan. uit de eerste regels worden de proposers en acceptors gemaakt.
daarna word iedere line een voor een geleest en word er een event van gemaakt,
en geeft de computers, ticks en events als input variable voor de simulatie
"""
def read_input(file):
    events = {}
    global proposers, acceptors

    with open(file, 'r') as inp:
        n_proposers, n_acceptors, max_ticks = [int(value) for value in inp.readline().split()]
        proposers = {id: Proposer('P' + str(id)) for id in range(1, n_proposers + 1)}
        acceptors = {id: Acceptor('A' + str(id)) for id in range(1, n_acceptors + 1)}

        lines = inp.read().splitlines()[:-1]
        for line in lines:
            event = make_event(line)
            events[event.tick] = event

    return proposers, acceptors, max_ticks, events
