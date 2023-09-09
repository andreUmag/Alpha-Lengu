class Figure():
    def union(self, other):
        if isinstance(other, self.__class__):
            return (", ".join(self.list_elements.union(other.list_elements)))
        else:
            raise ValueError("El argumento no es valido")

    def intersection(self, other):
        if isinstance(other, self.__class__):
            return (", ".join(self.list_elements.intersection(other.list_elements)))
        else:
            raise ValueError("El argumento no es valido")

    def difference(self, other):
        if isinstance(other, self.__class__):
            return (", ".join(self.list_elements.difference(other.list_elements)))
        else:
            raise ValueError("El argumento no es valido")