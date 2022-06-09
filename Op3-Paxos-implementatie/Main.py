from Input import ReadInput, read_input
from Network import Network
from Computers import Proposer, Acceptor
from Messages import Message


def simulatie(proposers, acceptors, tmax, events):
    network = Network(acceptors, proposers)

    for i in range(tmax):
        if len(network.msg_queue) == 0 and len(events) == 0:
            break

        print(f'{str(i).zfill(3)}: ', end='')

        if i in events.keys():
            event = events[i]
        else:
            event = None

        if event is not None:
            events.pop(i)

            if event.message.message_type == Message.PROPOSE:
                network.deliver_message(event.message)
            else:
                [computer.computer_fail() for computer in event.fail]
                [computer.computer_recover() for computer in event.recover]

        else:
            message = network.extract_message()
            if message is not None:
                network.deliver_message(message)
            else:
                print()

    print()
    for proposer in proposers.values():
        if proposer.agreement:
            print(
                f'{proposer} heeft wel consensus (voorgesteld: {proposer.proposed_value}, geaccepteerd: {proposer.value})')


input_variables = read_input('Input/voorbeeld2.txt')
simulatie(*input_variables)
