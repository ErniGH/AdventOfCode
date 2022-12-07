class Nodo:
    def __init__(self, peso):
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


nodoActual = Nodo(0)
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
        nodoNuevo = Nodo(0)
        nodoNuevo.setPadre(nodoActual)
        nodoActual.add(nombreNuevoNodo, nodoNuevo)
        lista.append(nodoNuevo)

    else:
        peso = int(division[0])
        nombreNuevoNodo = division[1]
        nodoNuevo = Nodo(peso)
        nodoActual.add(nombreNuevoNodo, nodoNuevo)

total = 0
for i in lista:
    valor = i.calcular()
    if valor <= 100000 and i.subnodos != []:
        total += valor

print(total)