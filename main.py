#ingreso de elementos del alfabeto
from alphabets import Alphabet 



print("Generador de Lenguajes\n","")
words = input("Ingrese la cadena de caracteres del lenguaje separados por comas: ")
alp1=Alphabet(words)
words2 = input("Ingrese la cadena de caracteres del lenguaje separados por comas: ")
alp2=Alphabet(words2)

apl3=alp1.union(alp2)
print(type(apl3))