import random
import figure

class Alphabet(figure.Figure):
    def __init__(self, alphabet):
        self.list_elements = set(alphabet.split(", "))

    def __str__(self):
        return ", ".join(self.list_elements)

    def add_alphabet(self, string):
        self.list_elements.add(string.split(','))

    def union(self, other):
        return self.__class__(super().union(other))

    def intersection(self, other):
        return self.__class__(super().intersection(other))
    
    def difference(self, other):
        return self.__class__(super().difference(other))

    def language_generator(self, star_lock, number_of_words):
        language = set()

        for _ in range(number_of_words):
            generated_word = random.choice(star_lock)
            while generated_word in language:
                generated_word = random.choice(star_lock)
            language.add(generated_word)

        return language

    def star_lock(self, length_star):
        result = []

        if length_star == 0:
           return result

        for _ in range(length_star):
            symbol_length = random.randint(0, 10)
            combination = ''.join(random.choice(list(self.list_elements)) for _ in range(symbol_length))
            while combination in result:
                symbol_length = random.randint(0, 10)
                combination = ''.join(random.choice(list(self.list_elements)) for _ in range(symbol_length))
            result.append(combination)
        return result
