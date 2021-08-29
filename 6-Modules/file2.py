from file1 import GreenCard


class BirthdayCard(GreenCard):
    def __init__(self, _sender_age=0):
        super().__init__()
        self._sender_age = _sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print(f"Happy {self._sender_age} B.day ")
