class Computer:
    def __init__(self, pc_id, value):
        self.pc_id = pc_id
        self.value = value
        self.failed = False

    """functie om een computer kapot te maken."""
    def computer_fail(self):
        print(f'** {self.pc_id} kapot **')
        self.failed = True

    """functie om een computer gerepareerd te maken."""
    def computer_recover(self):
        print(f'** {self.pc_id} gerepareerd **')
        self.failed = False

    def __str__(self):
        return f'{self.pc_id}'
