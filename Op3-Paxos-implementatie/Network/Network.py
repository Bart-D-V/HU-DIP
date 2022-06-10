from Messages import Message


class Network:
    def __init__(self, acceptors, proposers):
        self.acceptors = acceptors
        self.proposers = proposers
        self.msg_queue = []

    """ voegt een message toe aan msg_queue"""
    def queue_message(self, message):
        self.msg_queue.append(message)

    """ haalt een message uit msg_queue en geeft hem terug. """
    def extract_message(self):
        for message in self.msg_queue:

            if not message.source.failed and not message.destination.failed:
                self.msg_queue.remove(message)

                return message

    """ pakt het antwoord van de proposer op een PROPOSE message en voegt het antwoord toe in de queue als een message."""
    def send_propose(self, message):
        prepare_message = message.destination.take_in_propose(message)
        [self.queue_message(prepare_message(acceptor)) for acceptor in self.acceptors.values()]

    """ pakt het antwoord van de acceptor op een PREPARE message en voegt het antwoord toe in de queue als een message."""
    def send_prepare(self, message):
        promise_message = message.destination.take_in_prepare(message)
        self.queue_message(promise_message)

    """ pakt het antwoord van de proposer op een PROMISE message en voegt het antwoord toe in de queue als een message."""
    def send_promise(self, message):
        accept_message = message.destination.take_in_promise(message, len(self.acceptors))
        if accept_message is not None:
            [self.queue_message(accept_message(acceptor)) for acceptor in self.acceptors.values()]

    """ pakt het antwoord van de acceptor op een ACCEPT message en voegt het antwoord toe in de queue als een message."""
    def send_accept(self, message):
        accepted_rejected_message = message.destination.take_in_accept(message)
        self.queue_message(accepted_rejected_message)

    """ 
    pakt het antwoord van de proposer op een ACCEPTED/REJECTED message. 
    rejected is dan True of False, als rejected True is word een PROPOSE message naar de proposer gestuurd
    """
    def send_accepted_or_rejected(self, message):
        rejected = message.destination.take_in_accepted_or_rejected(message, len(self.acceptors))

        if rejected:
            self.send_propose(message)

    """ print de message data uit en pakt voor de message_type de juiste functie om te sturen naar de computer."""
    def deliver_message(self, message):
        print(f'{message.source} -> {message.destination} {message}')

        if message.message_type == Message.PROPOSE:
            self.send_propose(message)
        elif message.message_type == Message.PREPARE:
            self.send_prepare(message)
        elif message.message_type == Message.PROMISE:
            self.send_promise(message)
        elif message.message_type == Message.ACCEPT:
            self.send_accept(message)
        elif message.message_type == Message.ACCEPTED or message.message_type == Message.REJECTED:
            self.send_accepted_or_rejected(message)
