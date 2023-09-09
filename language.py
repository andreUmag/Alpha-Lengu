import figure

class Language(figure.Figure):
    def __init__(self, language):
        self.list_elements = language

    def union(self, other):
        return self.__class__(set((super().union(other)).split(", ")))
    
    def intersection(self, other):
        return self.__class__(set((super().intersection(other)).split(", ")))
    
    def difference(self, other):
        return self.__class__(set((super().difference(other)).split(", ")))

    def __str__(self):
        return print(self.list_elements)

    def concatenate(self, other_language):
        if isinstance(other_language, self.__class__):
            concatenated_language = []

            for word_1 in self.list_elements:
                for word_2 in other_language.list_elements:
                    concatenated_language.append(word_1 + word_2)
            return concatenated_language
        else:
            raise ValueError("El argumento no es un objeto de la clase Language.")

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