#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class BASE_vendor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def read_char(self):
        pass

    def __iter__(self):
        while True:
            yield self.read_char()
