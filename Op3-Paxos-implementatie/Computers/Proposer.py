from Computers import Computer


class Propose(Computer):
    propose_id = 0

    def __init__(self, pc_id, value=None):
        super().__init__(pc_id, value)
        self.propose_id = None
        self.suggest_value = None

    def take_in_propose(self, value):
        self.value = value
        Propose.propose_id += 1
        self.propose_id = Propose.propose_id

    def take_in_promise(self, message):
        return 0

    def take_in_accepted(self, message):
        return 0