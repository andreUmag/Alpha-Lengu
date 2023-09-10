from alphabets import *
from language import *

def ingresar_alfabetos():
    alphabet1_input = input("Primer alfabeto (separado por comas): ")
    alphabet2_input = input("Segundo alfabeto (separado por comas): ")
    alphabet1 = Alphabet(alphabet1_input)
    alphabet2 = Alphabet(alphabet2_input)
    return alphabet1, alphabet2

def star_lock(alphabet):
    star_lock = alphabet.star_lock(int(input("Cantidad de palabras de cerradura de estrella: ")))
    return star_lock

def lenguaje_generator(alphabet):
    cant_palabras = int(input("Cantidad de palabras para el lenguaje"))

def potencia(lenguaje):
    pot = lenguaje.expressive_power(int(input("Potencia el lenguaje a: ")))
    return pot


if __name__ == "__main__":
    alphabet1, alphabet2 = ingresar_alfabetos()

    uni = Alphabet.union(alphabet1, alphabet2)
    print(f"La unión de los alfabetos es: {uni}")

    inter = Alphabet.intersection(alphabet1, alphabet2)
    print(f"La interseccion de los alfabetos es: {inter}")

    dif = Alphabet.difference(alphabet1, alphabet2)
    print(f"La diferencia de los alfabetos es: {dif}")

    print("Primer Alfabeto: ")
    star_1 = star_lock(alphabet1)
    print(star_1)
    print("Segundo Alfabeto: ")
    star_2 = star_lock(alphabet2)
    print(star_2)

    lenguaje1 = Language(alphabet1.language_generator(star_1, int(input("Cantidad de palabras que tendrá el lenguaje "
                                                                        "\n(Debe ser menor que la cantidad en la cerradura de estrella)"
                                                                        "\n Indique: "))))
    lenguaje1.__str__()
    lenguaje2 = Language(alphabet2.language_generator(star_2, int(input("Cantidad de palabras que tendrá el lenguaje "
                                                                        "\n(Debe ser menor que la cantidad en la cerradura de estrella)"
                                                                        "\n Indique: "))))
    lenguaje2.__str__()

    unil = lenguaje1.union(lenguaje2)
    print(f"La unión de los lenguajes es: ")
    unil.__str__()

    interl = lenguaje1.intersection(lenguaje2)
    print(f"La interseccion de los lenguajes es: ")
    interl.__str__()

    difl = lenguaje1.difference(lenguaje2)
    print(f"La diferencia de los lenguajes es: ")
    difl.__str__()

    conc = lenguaje1.concatenate(lenguaje2)
    print(f"La concatenacion de los lenguajes es:\n{conc}")

    print("Primer Lenguaje: ")
    print(potencia(lenguaje1))
    print("Segundo Lenguaje: ")
    print(potencia(lenguaje2))

    print("Primer Lenguaje inverso: ")
    print(Language.inverse(lenguaje1))
    print("Segundo Lenguaje inverso: ")
    print(Language.inverse(lenguaje2))

    print("Primer Lenguaje cardinalidad: ")
    print(Language.cardinality(lenguaje1))
    print("Segundo Lenguaje cardinalidad: ")
    print(Language.cardinality(lenguaje2))