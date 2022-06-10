from Computers import Computer
from Messages import Message


class Acceptor(Computer):
    def __init__(self, pc_id, value=None):
        super().__init__(pc_id, value)
        self.propose_id = 0

    """
    acceptor krijgt een prepare message en neemt de propose_id over van de source als die hoger is dan de huidige,
    en stuurt een PROMISE message terug.
    """
    def take_in_prepare(self, message):
        if self.propose_id < message.source.propose_id:
            self.propose_id = message.source.propose_id

            return Message(message.destination, message.source, Message.PROMISE)

    """
    acceptor krijgt een prepare message,
    als de propose_id gelijk is aan het eigen propose_id word er een ACCEPTED message terug gestuurd
    als de ids niet gelijk zijn word een REJECTED message gestuurd.
    """
    def take_in_accept(self, message):
        if self.propose_id == message.source.propose_id:
            self.value = message.source.value
            return Message(message.destination, message.source, Message.ACCEPTED)
        else:
            return Message(message.destination, message.source, Message.REJECTED)
