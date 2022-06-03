from Computers import Computer


class Acceptor(Computer):
    def __init__(self, pc_id, value):
        super().__init__(pc_id, value)
        self.propose_id = 0

    def take_in_prepare(self, message):
        # als pc_id groter is dan propose_id maak propose_id pc_id en return promise message.
        return 0

    def take_in_accept(self, message):
        # als pc_id gelijk is aan propose_id maak de gegeven value self.value en geef en return een accepted message,
        # anders return een rejected message.
        return 0
