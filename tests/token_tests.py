import unittest

from common.token import Token


class TokenTests(unittest.TestCase):
    def test_string(self):
        token = Token.build_token('function main')

        self.assertEqual(token, 'function')

    def test_integer(self):
        token = Token.build_token('12.23 number')
        self.assertEqual(token, '12.23')

    def test_delimiter(self):
        token = Token.build_token('(arg1, arg2)')
        self.assertEqual(token, '(')

    def test_pseudo_identifier(self):
        token = Token.build_token('main_01')
        self.assertEqual(token, 'main_01')


if __name__ == '__main__':
    unittest.main()
