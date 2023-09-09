import random


class Figura():
    def union(self, other):
        if isinstance(other, self.__class__):
            return (", ".join(self.list_elements.union(other.list_elements)))
        else:
            raise ValueError("El argumento no es valido")
        
    def intersection(self, other):
        if isinstance(other, self.__class__):
            return (", ".join(self.list_elements.intersection(other.list_elements)))
        else:
            raise ValueError("El argumento no es valido")
        
    def difference(self, other):
        if isinstance(other, self.__class__):
            return (", ".join(self.list_elements.difference(other.list_elements)))
        else:
            raise ValueError("El argumento no es valido")

class Alphabet(Figura):
    def __init__(self, alphabet):
        self.list_elements = set(alphabet.split(", "))

    def add_alphabet(self, string):
        self.list_elements.add(string.split(','))

    def union(self, other):
        return self.__class__(super().union(other))
    
    def intersection(self, other):
        return self.__class__(super().intersection(other))
    
    def difference(self, other):
        return self.__class__(super().difference(other))
    
    def generate_word(self):
        word = []
        auxiliary_list=list(self.list_elements)
        for _ in range(random.randint(2, 10)):
            caracter = random.choice(auxiliary_list)
            word.append(caracter)
        return ''.join(word)

    def Language_generator(self, number_of_words):
        Language=set()
        for _ in range(number_of_words):
            Generated_word = self.generate_word()
            Language.add(Generated_word)
        return Language





   

 
    

