import os.path
import unittest

from lexer.lexer import Lexer

BASEPATH = os.path.dirname(__file__)


def map_repr_meta(token):
    return token.repr


class LexerTests(unittest.TestCase):
    @staticmethod
    def map_repr(token_list):
        return list(map(map_repr_meta, token_list))

    def test_function(self):
        lexer = Lexer(os.path.join(BASEPATH, 'input/function/function.txt'))

        self.assertEqual(self.map_repr(lexer.tokens), ['function', 'main', '(', ')', ':', 'int', '{', '}'])

    def test_multiple_function(self):
        lexer = Lexer(os.path.join(BASEPATH, 'input/function/multiple_function.txt'))

        self.assertEqual(self.map_repr(lexer.tokens), [
            'function', 'getnumber', '(', 'num_01', ':', 'int', ',', 'num_02', ':', 'int', ')', ':', 'int', '{', '}',
            'function', 'main', '(', ')', ':', 'int', '{', '}'
        ])

    def test_relational_operators(self):
        lexer = Lexer(os.path.join(BASEPATH, 'input/conditional/relational_operators.txt'))

        self.assertEqual(self.map_repr(lexer.tokens),
                         ['if', '(', 'a', '>', 'b', '&&', 'a', '>=', 'b', '&&', 'a', '<', 'b', '&&', 'a',
                          '<=', 'b', '||', 'a', '==', 'b', '||', 'a', '!=', 'b', ')', '{', '}'])

    def test_if_else(self):
        lexer = Lexer(os.path.join(BASEPATH, 'input/conditional/with_else.txt'))

        self.assertEqual(self.map_repr(lexer.tokens),
                         ['if', '(', 'invoke', 'getnumbers', '(', ')', '==', 'b', ')', '{', '}', 'else',
                          '{', '}'])

    def test_unexpected_char(self):
        lexer = Lexer(os.path.join(BASEPATH, 'input/unexpected.txt'))

        self.assertEqual(self.map_repr(lexer.tokens), ['main', None, None])


if __name__ == '__main__':
    unittest.main()
