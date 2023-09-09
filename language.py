from alphabets import *

class Language(Figura):
    def __init__(self, Language):
        self.list_elements = Language

    def union(self, other):
        return self.__class__(set((super().union(other)).split(", ")))
    
    def intersection(self, other):
        return self.__class__(set((super().intersection(other)).split(", ")))
    
    def difference(self, other):
        return self.__class__(set((super().difference(other)).split(", ")))

    def __str__(self):
        return print(self.list_elements)
        