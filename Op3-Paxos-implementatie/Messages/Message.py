class Message:

    PROPOSE = 'PROPOSE'
    PREPARE = 'PREPARE'
    PROMISE = 'PROMISE'
    ACCEPT = 'ACCEPT'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'

    def __init__(self, source, destination, message_type):
        self.source = source
        self.destination = destination
        self.message_type = message_type

    def get_output_info(self):
        if self.message_type == Message.PROPOSE: return f'v={self.destination.proposed_value}'
        elif self.message_type == Message.PREPARE: return f'n={self.source.propose_id}'
        elif self.message_type == Message.PROMISE:
            if self.source.value:
                prior = f"n={self.source.propose_id}, v={self.source.value}"
            else:
                prior = None
            return f'n={self.destination.propose_id} (Prior: {prior})'
        elif self.message_type == Message.ACCEPT: return f'n={self.source.propose_id} v={self.source.value}'
        elif self.message_type == Message.ACCEPTED: return f'n={self.destination.propose_id} v={self.destination.value}'
        elif self.message_type == Message.REJECTED: return f'n={self.destination.propose_id}'
        else:
            return ''

    def __str__(self):
        return f'{self.message_type} {self.get_output_info()}'
