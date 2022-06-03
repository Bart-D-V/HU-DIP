from Computers import Computer


class Propose(Computer):

    propose_id = 0

    def __init__(self, pc_id, value=None):
        super().__init__(pc_id, value)
        self.propose_id = None
        self.suggest_value = None
        self.agreement = False
        self.accepted = 0

    def take_in_propose(self, value):
        self.value = value
        Propose.propose_id += 1
        self.propose_id = Propose.propose_id

    def take_in_promise(self, message):
        if # message een value heeft:
            self.value = # value van de source message

        return 0 # naar alle acceptors een accept message sturen

    def take_in_accepted(self, message, majority):
        self.accepted += 1
        if self.accepted >= majority and not self.agreement:
            self.agreement = True


    def reset(self):
        self.accepted = 0
        Propose.propose_id += 1
        self.propose_id = Propose.propose_id