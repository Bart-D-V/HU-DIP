class Network:
    def __init__(self, acceptors, proposers):
        self.acceptors = acceptors
        self.proposers = proposers
        self.msg_queue = []

    def queue_message(self, message):
        self.msg_queue.append(message)

    def extract_message(self):
        for message in self.msg_queue:
            if not message.source.failed and not message.destination.failed:
                self.msg_queue.remove(message)

                return message

    def deliver_message(self, message):
        print(f'{message.source} -> {message.destination} {message.msg_type} ')
        # moet bij de gegeven messagetype de juiste functie gebruiken om de message aftehandelen.
        return 0