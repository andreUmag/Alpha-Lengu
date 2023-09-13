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
    print("\n1.Unión de los alfabetos\n2.Intersección de los alfabetos\n3.Diferencia de los alfabetos\n4.Avanzar")
    line_spacing()
    while True:
        selection = int(input("\nIndique: "))
        match selection:
            case 1:
                uni = Alphabet.union(alphabet1, alphabet2)
                print(f"La unión de los alfabetos es: {uni}")
            case 2:
                inter = Alphabet.intersection(alphabet1, alphabet2)
                print(f"La interseccion de los alfabetos es: {inter}")
            case 3:
                dif = Alphabet.difference(alphabet1, alphabet2)
                print(f"La diferencia de los alfabetos es: {dif}")
            case 4:
                break
            case _:
                print("Ha ingresado un indice incorrecto.")

    line_spacing()
    print("Primer Alfabeto: ")
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
    print("\n1.Unión de los Lenguajes\n2.Intersección de los alfabetos\n3.Diferencia de los alfabetos\n4.Concatenación entre lenguajes"
          "\n5.Potencia de un lenguaje \n6.Inversa de un lenguaje \n7.Cardinalidad de un lenguaje \n8.Finalizar")
    line_spacing()
    while True:
        selection = int(input("\nIndique: "))
        match selection:
            case 1:
                unil = language1.union(language2)
                print(f"La unión de los lenguajes es: ")
                unil.__str__()
            case 2:
                interl = language1.intersection(language2)
                print(f"La interseccion de los lenguajes es: ")
                interl.__str__()
            case 3:
                difl = language1.difference(language2)
                print(f"La diferencia de los lenguajes es: ")
                difl.__str__()
            case 4:
                conc = language1.concatenate(language2)
                print(f"La concatenacion de los lenguajes es:\n{conc}")
            case 5:
                print("- Primer Lenguaje ")
                print(power(language1))
                print("\n- Segundo Lenguaje ")
                print(power(language2))
            case 6:
                print("Primer Lenguaje inverso: ")
                print(Language.inverse(language1))
                print("Segundo Lenguaje inverso: ")
                print(Language.inverse(language2))
            case 7:
                print("Primer Lenguaje cardinalidad: ")
                print(Language.cardinality(language1))
                print("\nSegundo Lenguaje cardinalidad: ")
                print(Language.cardinality(language2))
            case 8:
                break
            case _:
                print("Ha ingresado un indice incorrecto.")