#ingreso de elementos del alfabeto
from alphabets import Alphabet 
from language import *


print("Generador de Lenguajes\n","")
words = input("Ingrese la cadena de caracteres del lenguaje separados por comas: ")
alp1=Alphabet(words)
words2 = input("Ingrese la cadena de caracteres del lenguaje separados por comas: ")
alp2=Alphabet(words2)

Lenguaje1=Language(alp1.Language_generator(2))
Lenguaje1.__str__()
Lenguaje2=Language(alp2.Language_generator(4))
Lenguaje2.__str__()
Lenguaje3=Lenguaje1.union(Lenguaje2)
Lenguaje3.__str__()