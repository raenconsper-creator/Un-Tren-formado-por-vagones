

class Vagon:
    """Vagon"""

    def __init__(self, dato = None):
        self.dato = dato
        self.siguiente = None
        self.numero = None
    
    def agregar(self, dato):
        nuevo = Vagon(dato)

        if self.numero is None:
            self.numero = nuevo
            return

        actual = self.numero

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def mostrar(self):
        actual = self.numero

        while actual:
            print(actual.dato, end= "->" )
            actual = actual.siguiente
        print("None")

vagon = Vagon()
vagon.agregar(1)
vagon.agregar(2)
vagon.agregar(3)
vagon.agregar(4)

vagon.mostrar()
