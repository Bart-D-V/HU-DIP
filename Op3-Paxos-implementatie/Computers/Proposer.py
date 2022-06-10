from Computers import Computer
from Messages import Message


class Proposer(Computer):
    # variable die bijhoud hoeveel proposeles er zijn geweest.
    propose_count = 0

    def __init__(self, pc_id, value=None):
        super().__init__(pc_id, value)
        self.propose_id = None
        self.proposed_value = None
        self.agreement = False
        self.send_accept = False
        self.accepted = 0
        self.rejected = 0
        self.promise_votes = 0

    def set_proposed_value(self, proposed_value):
        self.proposed_value = proposed_value

    """ 
    proposer krijgt een PROPOSE message en neemt proposed_value over in value, 
    daarna gaat de propose_count met 1 omhoog en neemt propose_count als propose_id.
    dan word naar alle acceptors een PREPARE message gestuurd.
    """
    def take_in_propose(self, message):
        self.value = self.proposed_value
        Proposer.propose_count += 1
        self.propose_id = Proposer.propose_count

        return lambda acceptor: Message(message.destination, acceptor, message.PREPARE)

    """
    proposer krijgt een PROMISE message en telt 1 op bij promise_votes,
    de proposer neemt de value van de source over als die een value heeft.
    als er een meerderheid in votes is bereikt word er een accept message terug gestuurd naar alle acceptors.
    """
    def take_in_promise(self, message, n_acceptors):
        self.promise_votes += 1
        if message.source.value:
            self.value = message.source.value

        if self.promise_votes >= n_acceptors/2 and not self.send_accept:
            self.send_accept = True
            return lambda acceptor: Message(message.destination, acceptor, message.ACCEPT)

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
                self.promise_votes = 0
                self.send_accept = False
                return True

        return False
