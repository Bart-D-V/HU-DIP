from Computers import Computer
from Messages import Message


class Proposer(Computer):
    propose_id = 0

    def __init__(self, pc_id, value=None):
        super().__init__(pc_id, value)
        self.propose_id = None
        self.proposed_value = None
        self.agreement = False
        self.accepted = 0
        self.rejected = 0

    def set_proposed_value(self, proposed_value):
        self.proposed_value = proposed_value

    def take_in_propose(self, message):
        self.value = self.proposed_value
        Proposer.propose_id += 1
        self.propose_id = Proposer.propose_id

        return lambda acceptor: Message(message.destination, acceptor, message.PREPARE)

    def take_in_promise(self, message):
        if message.source.value:
            self.value = message.source.value

        return Message(message.destination, message.source, message.ACCEPT)

    def take_in_accepted_or_rejected(self, message, n_acceptors):
        majority = n_acceptors / 2

        if message.message_type == 'ACCEPTED':
            self.accepted += 1
            if self.accepted >= majority and self.accepted + self.rejected == n_acceptors:
                self.agreement = True
                return False

        elif message.message_type == 'REJECTED':
            self.rejected += 1
            if self.rejected >= majority and self.accepted + self.rejected == n_acceptors:
                self.accepted = 0
                self.rejected = 0
                return True

        return False
