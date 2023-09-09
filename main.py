from alphabets import *
from language import *

def ingresar_alfabetos():
    alphabet1_input = input("Primer alfabeto (separado por comas): ")
    alphabet2_input = input("Segundo alfabeto (separado por comas): ")
    alphabet1 = Alphabet(alphabet1_input)
    alphabet2 = Alphabet(alphabet2_input)
    return alphabet1, alphabet2

def star_lock(alphabet):
    star_lock = alphabet.star_lock(int(input("Cantidad de palabras para la cerradura de estrella: ")))
    Lenguaje = Language(alphabet.language_generator(star_lock, 2))
    Lenguaje.__str__()
    print(f"Cerradura de estrella: {star_lock}")



if __name__ == "__main__":
    alphabet1, alphabet2 = ingresar_alfabetos()

    uni = Alphabet.union(alphabet1, alphabet2)
    print(f"La unión de los alfabetos es: {uni}")

    inter = Alphabet.intersection(alphabet1, alphabet2)
    print(f"La interseccion de los alfabetos es: {inter}")

    dif = Alphabet.difference(alphabet1, alphabet2)
    print(f"La diferencia de los alfabetos es: {dif}")

    print("Primer Alfabeto")
    star_lock(alphabet1)
    print("Segundo Alfabeto")
    star_lock(alphabet2)


