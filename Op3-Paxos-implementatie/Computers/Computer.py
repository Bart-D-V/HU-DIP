class Computer:
    def __init__(self, pc_id, value):
        self.pc_id = pc_id
        self.value = value
        self.failed = False

    def computer_fail(self):
        print(f'** {self.pc_id} kapot **')
        self.failed = True

    def computer_repair(self):
        print(f'** {self.pc_id} gerepareerd **')
        self.failed = False
