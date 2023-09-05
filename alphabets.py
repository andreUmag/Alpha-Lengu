import random
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def union(self, otter):
        pass

    @abstractmethod
    def intersection(self, otter):
        pass

    @abstractmethod
    def difference(self, otter):
        pass


class Alphabet(Figura):
    def __init__(self, alphabet):
        self.list_alpha = list(alphabet)

    def add_alphabet(self, string):
        self.list_alpha.extend(string.split(','))

    def union(self, otter):
        new_alpha = Alphabet(self.list_alpha.union(otter.list_alpha))
        return new_alpha

    def intersection(self, otter):
        new_alpha = Alphabet(self.list_alpha.intersection(otter.list_alpha))
        return new_alpha

    def difference(self, otter):
        new_alpha = Alphabet(self.list_alpha.difference(otter.list_alpha))
        return new_alpha

    def star_lock(self, n):
        pass
