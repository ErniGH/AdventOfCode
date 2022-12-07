class Nodo:
    def __init__(self, peso, nombre):
        self.nombre = nombre
        self.subnodos = {}
        self.peso = peso
        self.padre = "NO TIENE PADRE"

    def add(self, k, nodo):
        self.subnodos[k] = nodo

    def calcular(self):
        return sum([self.subnodos[k].calcular() for k in self.subnodos]) + self.peso

    def setPadre(self, padre):
        self.padre = padre

    def getPadre(self):
        return self.padre


nodoActual = Nodo(0, "/")
lista = [nodoActual]

primeralinea = input()


while True:
    entrada = input()
    if entrada == "-":
        break
    division = entrada.split()
    if division[0] == "$":
        if division[1] == "cd":
            if division[2] == "..":
                nodoActual = nodoActual.getPadre()
            else:
                nodoActual = nodoActual.subnodos[division[2]]

    elif division[0] == "dir":
        nombreNuevoNodo = division[1]
        nodoNuevo = Nodo(0, nombreNuevoNodo)
        nodoNuevo.setPadre(nodoActual)
        nodoActual.add(nombreNuevoNodo, nodoNuevo)
        lista.append(nodoNuevo)

    else:
        peso = int(division[0])
        nombreNuevoNodo = division[1]
        nodoNuevo = Nodo(peso, nombreNuevoNodo)
        nodoActual.add(nombreNuevoNodo, nodoNuevo)

nombres = []
valores = []


for i in lista:
    nombres.append(i.nombre)
    valores.append(i.calcular())

restante = 70000000 - valores[0]

nombresMenores = []
valoresMenores = []

for i in range(len(valores)):
    if valores[i] + restante >= 30000000:
        nombresMenores.append(nombres[i])
        valoresMenores.append(valores[i])

print(min(valoresMenores))