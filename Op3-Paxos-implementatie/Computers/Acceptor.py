from Computers import Computer


class Acceptor(Computer):
    def __init__(self, pc_id, value):
        super().__init__(pc_id, value)
        self.propose_id = 0

    def take_in_prepare(self, message):
        if self.propose_id < message.source.propose_id:
            self.propose_id = message.source.propose_id
            return message# promise message

    def take_in_accept(self, message):
        # als pc_id gelijk is aan propose_id maak de gegeven value self.value en geef en return een accepted message,
        # anders return een rejected message.
        if self.propose_id == message.source.propose_id:
            self.value = message.source.value
            return message# accepted message
        else:
            return message# rejected message
