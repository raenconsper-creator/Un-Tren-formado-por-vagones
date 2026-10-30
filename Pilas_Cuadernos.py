# Programador: Rafael Constanzo

class Cuaderno:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaCuadernos:
    def __init__(self) -> None:
        self.tope = None

    def apilar(self, dato):
        numero = Cuaderno(dato)
        numero.siguiente = self.tope
        self.tope = numero

    def desapilar(self):
        if self.tope is None:
            raise IndexError("La pila esta vacia")

        dato = self.tope.dato
        self.tope = self.tope.siguiente

        return dato

    def mostrar(self):
        actual = self.tope
        while actual is not None:
            print(actual.dato, end = " => ")
            actual = actual.siguiente

    def peek(self):
        if self.tope is None:
            raise IndexError("La pila esta vacia")
        return self.tope.dato

    
    def esta_vacia(self):
        return self.tope is None

pila_numero = PilaCuadernos()
pila_numero.apilar(1)
pila_numero.apilar(2)
pila_numero.apilar(3)
pila_numero.apilar(4)
#pila_numero.apilar(5)
#pila_numero.apilar(6)
#pila_numero.apilar(7)

print("Contenido de la Pila: ", end=" => ")
pila_numero.mostrar()
print("None")
print("Cuaderno en el tope:", pila_numero.peek())
print("Cuaderno Retirado:", pila_numero.desapilar())
print("Contenido de la pila después de desapilar: ", end="")

pila_numero.mostrar()
print("None")
       