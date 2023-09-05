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
    def __init__(self, characters):
        self.list_alpha = list(characters)

    def add_alphabet(self, string):
        self.list_alpha.extend(string.split(','))

    def union(self, otter):
        new_alpha = Alphabet("".join(self.list_alpha))
        new_alpha.add_alphabet("".join(otter.list_alpha))
        return new_alpha

    def intersection(self, otter):
        new_alpha = Alphabet("".join(filter(lambda x: x in otter.list_alpha, self.list_alpha)))
        return new_alpha

    def difference(self, otter):
        new_alpha = Alphabet("".join(filter(lambda x: x not in otter.list_alpha, self.list_alpha)))
        return new_alpha

    def star_lock(self, n):
        pass
