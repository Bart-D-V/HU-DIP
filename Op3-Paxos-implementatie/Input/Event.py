class Event:
    def __init__(self, tick, fail, recover, message):
        self.tick = tick
        self.fail = fail
        self.recover = recover
        self.message = message
