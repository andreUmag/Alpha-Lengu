from alphabets import *

class Language(Figura):
    def __init__(self, Language):
        self.list_elements = Language

    def union(self, other):
        return self.__class__(set((super().union(other)).split(", ")))
    
    def intersection(self, other):
        return self.__class__(set((super().intersection(other)).split(", ")))
    
    def difference(self, other):
        return self.__class__(set((super().difference(other)).split(", ")))

    def __str__(self):
        return print(self.list_elements)

    def concatenate(self):
        pass
    def expressive_power(self, exponent):
        result = list(self.list_elements)

        if exponent == 0:
            return ['']

        for i in range(exponent-1):
            temporary_power = []
            for word_1 in result:
                for word_2 in list(self.list_elements):
                    temporary_power.append(word_1 + word_2)
            result = temporary_power

        return result

    def inverse(self):
        result = list(self.list_elements)
        result.reverse()

        return result

    def cardinality(self):
        return len(self.list_elements)