import re

from common.consts import DELIMITERS, BLANK, RELATIONAL, TOKENS, NUMBER, IDENTIFIER


class Token:
    repr: str
    type: int
    row: int
    col: int

    def __init__(self, token, _type, row, col):
        self.repr = token
        self.type = _type
        self.row = row
        self.col = col

    def get_pos(self):
        return f'{self.row}:{self.col}'

    @staticmethod
    def build_token(string: str, row: int, col: int):
        token = ''

        for char in string:
            if char in BLANK:
                if not token:
                    continue
                else:
                    return Token.build_token_meta(token, row, col)

            if char in DELIMITERS:
                # Build floating number
                if char == '.' and token and token.isnumeric():
                    token += '.'
                    continue

                # Build relational operator
                if char in RELATIONAL:
                    token += char
                    continue

                if char == '=' and token in RELATIONAL:
                    return Token.build_token_meta(token + char, row, col)

                if char == '|' and token == char:
                    return Token.build_token_meta(token + char, row, col)

                if char == '&' and token == char:
                    return Token.build_token_meta(token + char, row, col)

                if token:
                    return Token.build_token_meta(token, row, col)
                else:
                    return Token.build_token_meta(char, row, col)

            token += char

        return Token.build_token_meta(token, row, col)

    @staticmethod
    def build_token_meta(token: str, row: int, col: int):
        if token in TOKENS:
            return Token(token, TOKENS[token], row, col)
        elif re.match(IDENTIFIER, token):
            return Token(token, 45, row, col)
        elif re.match(NUMBER, token):
            return Token(token, 46, row, col)
        else:
            return Token(token, 47, row, col)
