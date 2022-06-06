class Message:

    PROPOSE = 'PROPOSE'
    PREPARE = 'PREPARE'
    PROMISE = 'PROMISE'
    ACCEPT = 'ACCEPT'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'

    def __intit__(self, source, destination, msg_type):
        self.source = source
        self.destination = destination
        self.msg_type = msg_type
