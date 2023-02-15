from typing import IO


class Reader:
    file: IO
    line: str
    number: int

    def __init__(self, file: str):
        self.file = open(file, 'r')
        self.number = 0

    def get_next_line(self):
        self.line = self.file.readline()

        if self.line:
            self.number += 1

        return self.line, self.number

    def __del__(self):
        self.file.close()
