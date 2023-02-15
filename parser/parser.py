from enum import Enum

import parser
from common.consts import TOKENS as T, DATATYPES, KEYWORDS, LOGIC, RELATION
from common.token import Token
from ds.object import Object
from ds.registry import Registry
from ds.stack import Stack
from error.error import ERRORS as E, ERRORS

MAX_LINE = 1000
MAX_WORD = 11
MAX_DIGIT = 5
MAX_ST = 100


class Parser:
    __tks: Stack
    __current: Token
    __lexeme: str
    __value: int
    __syms: [Registry]
    __it: int
    
    def __init__(self, tokens: [Token]):
        self.__tks = tokens
        self.__it = 0
        self.__syms = [None] * MAX_ST

        self.__function()
        
    def __advance(self):
        self.__current = current = self.__tks.pop()
        
        if current.type == T['id'] or current.type in KEYWORDS:
            self.__lexeme = current.repr + '\0'
        elif current.type == T['integer']:
            self.__value = int(current.repr)
            
    def __find_symbol(self):
        temp = self.__it
        self.__syms[0].name = self.__lexeme

        while self.__syms[temp] != self.__lexeme:
            i = i - 1

        return i
        
    def __function(self):
        while self.__current == T['function']:
            self.__advance()
            
            if self.__current == T['id']:
                self.__put(Object.FUNCTION)
                self.__advance()
            else:
                self.__error(1)

            if self.__current == T['(']:
                self.__advance()
                self.__args()
            else:
                self.__error(2)

            if self.__current == T['{']:
                self.__advance()
                self.__statement()
            else:
                self.__error(3)

    def __params(self):
        while self.__current == T['id']:
            self.__put(Object.PARAMETER)
            self.__advance()

    def __args(self):
        while self.__current == T['id']:
            self.__put(Object.PARAMETER)
            self.__advance()

            if self.__current == T[':']:
                self.__advance()
            else:
                self.__error(16)

            if self.__current in DATATYPES.keys():
                self.__advance()
            else:
                self.__error(17)

            if self.__current == T[',']:
                self.__advance()
            else:
                return


    def __statement(self):
        if self.__current == T['id']:
            id_position = self.__find_symbol()

            if id_position <= 0:
                self.__error(4)
            else:
                if self.__syms[id_position] != Object.VARIABLE:
                    self.__error(5)

                self.__advance()

                if self.__current == T['=']:
                    self.__advance()
                else:
                    self.__error(6)

                self.__expression()
        else:
            if self.__current == T['invoke']:
                self.__advance()

                if self.__current != T['id']:
                    self.__error(9)
                else:
                    id_position = self.__find_symbol()

                    if id_position == 0:
                        self.__error(4)
                    else:
                        if self.__syms[id_position].ttype != Object.FUNCTION:
                            self.__error(10)

                    self.__advance()

                    if self.__current == T['(']:
                        self.__advance()
                        self.__params()
                    else:
                        self.__error(2)

                    if self.__current != T[')']:
                        self.__error(13)
            else:
                if self.__current == T['if'] or self.__current == T['while']:
                    is_while = self.__current == T['while']

                    self.__advance()

                    if self.__current == T['(']:
                        self.__advance()
                        self.__condition()

                        if self.__current == T['{']:
                            self.__advance()
                        else:
                            self.__error(3)

                        self.__statement()

                        if self.__current == T['}']:
                            self.__advance()
                        else:
                            self.__error(15)

                        if not is_while:
                            if self.__current == T['else']:
                                self.__advance()
                            else:
                                self.__error(16)

                            if self.__current == T['{']:
                                self.__advance()
                            else:
                                self.__error(3)

                            self.__statement()

                            if self.__current == T['}']:
                                self.__advance()

                    else:
                        self.__error(11)

                elif self.__current == T['var'] or self.__current == T['const']:
                    self.__advance()
                    self.__decl(self.__current)

                elif self.__current == T['return']:
                    self.__advance()
                    self.__put(Object.RETURN)

    def __decl(self, ttype):
        while self.__current == T['id']:
            self.__put(Object.VARIABLE if ttype == T['var'] else Object.CONST)
            self.__advance()

            if self.__current == T[':']:
                self.__advance()
            else:
                self.__error(17)

            if self.__current in DATATYPES.keys():
                self.__advance()
            else:
                self.__error(18)

            if self.__current == T[',']:
                continue
            elif self.__current == T['=']:
                self.__advance()
                self.__expression()

        if self.__current != T[';']:
            self.__error(';')

    def __expression(self):
        if self.__current == T['+'] or self.__current == T['-']:
            self.__advance()
            self.__term()
        else:
            self.__term()

        while self.__current == T['+'] or self.__current == T['-']:
            self.__advance()
            self.__term()

    def __term(self):
        self.__factor()

        while self.__current == T['*'] or self.__current == T['/'] or self.__current == T['%']:
            self.__advance()
            self.__factor()

    def __factor(self):
        if self.__current == T['invoke']:
            self.__advance()

        if self.__current == T['id']:
            id_position = self.__find_symbol()

            if id_position == 0:
                self.__error(4)
            else:
                self.__advance()
        else:
            if self.__current == T['integer'] or self.__current == T['direction'] or self.__current == T['color']:
                self.__advance()

            else:
                if self.__current == T['(']:
                    self.__advance()
                    self.__expression()

                    if self.__current == T[')']:
                        self.__advance()
                    else:
                        self.__error(7)
                else:
                    self.__error(8)

    def __condition(self):
        self.__expression()

        if self.__current not in LOGIC.keys() or self.__current not in RELATION.keys():
            self.__error(13)
        else:
            self.__advance()
            self.__expression()

            while self.__current in RELATION.keys():
                self.__condition()

            if self.__current == T[')']:
                self.__advance()
            else:
                self.__error(14)

    def __put(self, ob: Object):
        self.__it = self.__it + 1
        
        if self.__it >= MAX_ST:
            self.__error(0)
        else:
            self.__syms[self.__it] = Registry(self.__lexeme, ob)

    def __error(self, error_no):
        print('Remaining tokens to process:\t' + str(len(self.__tks)))
        print(ERRORS[error_no])
        exit(1)
