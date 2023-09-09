from alphabets import *
from language import *

print("Generador de Lenguajes\n","")
words = input("Ingrese la cadena de caracteres del lenguaje separados por comas: ")
alp1=Alphabet(words)
words2 = input("Ingrese la cadena de caracteres del lenguaje separados por comas: ")
alp2=Alphabet(words2)

star_lock1 = alp1.star_lock(int(input("Ingrese la cantidad de palabras que se generarán para la cerradura de estrella: ")))
Lenguaje1=Language(alp1.language_generator(star_lock1, 2))
Lenguaje1.__str__()
star_lock2 = alp2.star_lock(int(input("Ingrese la cantidad de palabras que se generarán para la cerradura de estrella: ")))
Lenguaje2=Language(alp2.language_generator(star_lock2,4))
Lenguaje2.__str__()
Lenguaje3=Lenguaje1.union(Lenguaje2)
Lenguaje3.__str__()