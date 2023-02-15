KEYWORDS = {
    'function': 0,
    'main': 1,
    'return': 2,
    'if': 3,
    'else': 4,
    'while': 5,
    'invoke': 6,
    'var': 7,
    'const': 8,
    'move': 9,
    'is_clear': 10,
    'get_color': 11
}

DATATYPES = {
    'int': 12,
    'float': 13,
    'color': 14,
    'direction': 15,
    'bool': 16,
    'void': 17
}

PRIMITIVES = {
    'red': 18,
    'green': 19,
    'blue': 20,

    'left': 21,
    'right': 22,
    'front': 23,
    'back': 24
}

OPERATORS = {
    '+': 25,
    '-': 26,
    '*': 27,
    '/': 28,
    '%': 29
}

LOGIC = {
    '||': 30,
    '&&': 31
}

RELATION = {
    '>': 32,
    '>=': 33,
    '<': 34,
    '<=': 35,
    '!': 36,
    '!=': 37,
    '==': 38
}

FORMAT = {
    ':': 39,
    ',': 40,
    ';': 41,
    '(': 42,
    ')': 43,
    '{': 44,
    '}': 45
}

# identifier = 45, int_number = 46, color = 47, boolean = 48, direction = 49, none = 50

TOKENS = {**KEYWORDS, **DATATYPES, **PRIMITIVES, **OPERATORS, **LOGIC, **RELATION, **FORMAT,
          'id': 45,
          'integer': 46,
          'color': 47,
          'boolean': 48,
          'direction': 49,
          'none': 50
          }

BLANK = [' ', '\t', '\r', '\n']

DELIMITERS = [',', '.', ':', ';', '(', ')', '{', '}', '+', '-', '*', '/', '>', '<', '!', '=', '|', '&']
RELATIONAL = ['>', '<', '=', '!', '&', '|']

NUMBER = '^(?:[0-9])+(?:[\\.][0-9]+){0,1}$'
IDENTIFIER = '^[A-Za-z]+(?:[_][A-Za-z]+)*(?:[_][0-9]+)*$'

MAX_LEN_SYM_TABLE = 100
