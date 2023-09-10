from alphabets import *
from language import *

def in_alphabets():
    alphabet1_input = input("Primer alfabeto (separado por comas): ")
    alphabet2_input = input("Segundo alfabeto (separado por comas): ")
    alphabet1 = Alphabet(alphabet1_input)
    alphabet2 = Alphabet(alphabet2_input)
    return alphabet1, alphabet2

def star_lock(alphabet):
    star_lock = alphabet.star_lock(int(input("Cantidad de palabras de cerradura de estrella: ")))
    return star_lock

def language_generator(alphabet):
    cant_words = int(input("Numero de palabras del lenguaje"))

def power(language):
    pot = language.expressive_power(int(input("Potenciar el lenguaje a: ")))
    return pot

def line_spacing():
    print("-" * 60)

if __name__ == "__main__":
    alphabet1, alphabet2 = in_alphabets()

    line_spacing()
    uni = Alphabet.union(alphabet1, alphabet2)
    print(f"\nLa unión de los alfabetos es: {uni}")
    inter = Alphabet.intersection(alphabet1, alphabet2)
    print(f"\nLa interseccion de los alfabetos es: {inter}")
    dif = Alphabet.difference(alphabet1, alphabet2)
    print(f"\nLa diferencia de los alfabetos es: {dif}")

    line_spacing()
    print("\nPrimer Alfabeto: ")
    star_1 = star_lock(alphabet1)
    print(star_1)
    print("\nSegundo Alfabeto: ")
    star_2 = star_lock(alphabet2)
    print(star_2)

    line_spacing()
    language1 = Language(alphabet1.language_generator(star_1, int(input("\nCantidad de palabras que tendrá el 1er lenguaje "
                                                                        "\n(Debe ser menor que la cantidad en la cerradura de estrella)"
                                                                        "\n Indique: "))))
    language1.__str__()
    language2 = Language(alphabet2.language_generator(star_2, int(input("\nCantidad de palabras que tendrá el 2do lenguaje "
                                                                        "\n(Debe ser menor que la cantidad en la cerradura de estrella)"
                                                                        "\n Indique: "))))
    language2.__str__()

    line_spacing()
    unil = language1.union(language2)
    print(f"\nLa unión de los lenguajes es: ")
    unil.__str__()
    interl = language1.intersection(language2)
    print(f"\nLa interseccion de los lenguajes es: ")
    interl.__str__()
    difl = language1.difference(language2)
    print(f"\nLa diferencia de los lenguajes es: ")
    difl.__str__()

    line_spacing()
    conc = language1.concatenate(language2)
    print(f"\nLa concatenacion de los lenguajes es:\n{conc}")

    line_spacing()
    print("\nPrimer Lenguaje: ")
    print(power(language1))
    print("\nSegundo Lenguaje: ")
    print(power(language2))

    line_spacing()
    print("\nPrimer Lenguaje inverso: ")
    print(Language.inverse(language1))
    print("\nSegundo Lenguaje inverso: ")
    print(Language.inverse(language2))

    line_spacing()
    print("\nPrimer Lenguaje cardinalidad: ")
    print(Language.cardinality(language1))
    print("\nSegundo Lenguaje cardinalidad: ")
    print(Language.cardinality(language2))