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
    print(star_lock(alphabet1))
    print("Segundo Alfabeto: ")
    print(star_lock(alphabet2))

    lenguaje1 = 0
    lenguaje2 = 0

    unil = Language.union(lenguaje1, lenguaje2)
    print(f"La unión de los lenguajes es: {unil}")

    interl = Language.intersection(lenguaje1, lenguaje2)
    print(f"La interseccion de los lenguajes es: {interl}")

    difl = Language.difference(lenguaje1, lenguaje2)
    print(f"La diferencia de los lenguajes es: {difl}")

    conc = Language.concatenate(lenguaje1, lenguaje2)
    print(f"La concatenacion de los lenguajes es: {conc}")

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