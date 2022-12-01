import math


class Nodo:

    def __init__(self):
        self.padre = None
        self.valor = None
        self.nodos = [None, None]
        self.profundidad = 0

    def __add__(self, other):
        n = Nodo()

        self.aumentarProfundidad()
        other.aumentarProfundidad()

        n.addIzquierda(self)
        n.addDerecha(other)

        print("++ Despues de suma ++")
        print(n.mostrarLlaves())

        return n

    def aumentarProfundidad(self):
        self.profundidad += 1
        if self.valor is None:
            self.nodos[0].aumentarProfundidad()
            self.nodos[1].aumentarProfundidad()

    def addIzquierda(self, nodo):
        nodo.padre = self
        self.nodos[0] = nodo

    def addDerecha(self, nodo):
        nodo.padre = self
        self.nodos[1] = nodo

    def setValor(self, valor):
        self.valor = valor

    def mostrar(self):
        print("-"*self.profundidad, self.valor)
        if self.nodos[0]:
            self.nodos[0].mostrar()
        if self.nodos[1]:
            self.nodos[1].mostrar()

    def mostrarLlaves(self):
        if self.valor is None:
            return "[" + self.nodos[0].mostrarLlaves() + "," + self.nodos[1].mostrarLlaves() + "]"
        else:
            return str(self.valor)

    def explotar(self):
        calcularHorizonteArbol()
        if self.valor:

            nodoIzq = Nodo()
            nodoIzq.profundidad = self.profundidad+1
            nodoIzq.valor = math.floor(self.valor/2)
            nodoIzq.padre = self
            self.nodos[0] = nodoIzq

            nodoDer = Nodo()
            nodoDer.profundidad = self.profundidad+1
            nodoDer.valor = math.ceil(self.valor / 2)
            nodoDer.padre = self
            self.nodos[1] = nodoDer

            self.valor = None
        else:
            propagarIzquierda(self.nodos[0])
            propagarDerecha(self.nodos[1])
            self.valor = 0
            self.nodos = [None, None]


def f(entrada, i, profundidad):
    nodoActual = Nodo()
    nodoActual.profundidad = profundidad
    loop = True
    while loop:
        if entrada[i] == "[":
            nodoIzquierda, aumentoIndice = f(entrada, i+1, profundidad+1)
            nodoActual.addIzquierda(nodoIzquierda)
            i = aumentoIndice
        elif entrada[i] == ",":
            nodoDerecha, aumentoIndice = f(entrada, i+1, profundidad+1)
            nodoActual.addDerecha(nodoDerecha)
            i = aumentoIndice
        elif entrada[i] == "]":
            i += 1
            loop = False
        else:
            nodoActual.valor = int(entrada[i])
            loop = False
            i += 1
    return nodoActual, i


# buscamos explotar o dividir el que primero ocurra
def buscarExplotar(nodo):
    # cosas por las que explotar
    if (nodo.profundidad > 3 and nodo.valor is None) or (nodo.valor and nodo.valor >= 10):
        nodo.explotar()
        return True
    elif nodo.nodos[0]:
        resultado = buscarExplotar(nodo.nodos[0])
        if resultado:
            return True
        if nodo.nodos[1]:
            resultado = buscarExplotar(nodo.nodos[1])
            if resultado:
                return True
        return False


# buscamos primero todos los de dividir y luego los de explotar
def buscarExplotar2(nodo):
    exp = buscarExp(nodo)
    if exp:
        return True
    else:
        return buscarDividir(nodo)


def buscarExp(nodo):
    if nodo.profundidad > 3:
        nodo.explotar()
        return True
    elif nodo.nodos[0]:
        resultado = buscarExp(nodo.nodos[0])
        if resultado:
            return True
        if nodo.nodos[1]:
            resultado = buscarExp(nodo.nodos[1])
            if resultado:
                return True
        return False


def buscarDividir(nodo):
    if nodo.valor and nodo.valor >= 10:
        nodo.explotar()
        return True
    elif nodo.nodos[0]:
        resultado = buscarDividir(nodo.nodos[0])
        if resultado:
            return True
        if nodo.nodos[1]:
            resultado = buscarDividir(nodo.nodos[1])
            if resultado:
                return True
        return False


def calcularHorizonteArbol():
    global arbol
    global horizonte
    horizonte = []
    porVisitar = [arbol]
    while len(porVisitar) > 0:
        actual = porVisitar.pop()
        if actual.valor is not None:
            horizonte += [actual]
        else:
            if actual.nodos[1]:
                porVisitar += [actual.nodos[1]]
            if actual.nodos[0]:
                porVisitar += [actual.nodos[0]]


def propagarIzquierda(nodo):
    global horizonte
    valor = nodo.valor
    i = horizonte.index(nodo)
    if i > 0:
        horizonte[i-1].valor += valor


def propagarDerecha(nodo):
    global horizonte
    valor = nodo.valor
    i = horizonte.index(nodo)
    if i < len(horizonte)-1:
        horizonte[i+1].valor += valor


arbol = None
horizonte = []
while True:
    valorActual = input()
    if valorActual == "":
        break
    nodoActual = f(valorActual, 0, 0)[0]
    if arbol is None:
        arbol = nodoActual
    else:
        arbol += nodoActual

    # Reducir
    loop = True
    while loop:
        loop = buscarExplotar2(arbol)
        print("..")
        print(arbol.mostrarLlaves())

    print("_____")
    print(arbol.mostrarLlaves())
    print()



