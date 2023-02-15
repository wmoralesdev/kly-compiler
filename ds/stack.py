from common.token import Token


class Stack:
    items: [Token]

    def __init__(self, items: [Token]):
        self.items = items

    def peek(self) -> str:
        return self.items[0].repr

    def pop(self) -> Token:
        return self.items.pop(0)

