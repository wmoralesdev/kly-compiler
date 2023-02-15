from dataclasses import dataclass

from ds.object import Object


class Registry:
    name: str
    ttype: Object

    def __init(self, name):
        self.name = name

    def __init__(self, name, ttype):
        self.__init(name)
        self.ttype = ttype
