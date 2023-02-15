from common.consts import BLANK
from common.token import Token
from lexer.reader import Reader


class Lexer:
    reader: Reader
    tokens: [Token]

    def __init__(self, path: str):
        self.reader = Reader(path)
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        column = 0
        line, row = self.reader.get_next_line()

        while line:
            while len(line) > 0:
                while line and line[0] == '#' or line in BLANK:
                    line, row = self.reader.get_next_line()

                while line and line[0] in BLANK:
                    column += 1
                    line = line[1:]

                token = Token.build_token(line, row, column)

                column += len(token.repr)
                self.tokens.append(token)

                line = line[len(token.repr):]

            line, row = self.reader.get_next_line()
            column = 0

