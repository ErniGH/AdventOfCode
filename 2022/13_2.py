def compararListaLista(lista1, lista2):
    salida = 0  # -1 no en orden, 1 en orden, 0 continua
    for n in range(min(len(lista1), len(lista2))):
        if type(lista1[n]) == type(lista2[n]) == int:
            if lista1[n] < lista2[n]:
                return 1
            elif lista1[n] > lista2[n]:
                return -1
            else:
                continue

        elif type(lista1[n]) == list and type(lista2[n]) == int:
            salida = compararListaLista(lista1[n], [lista2[n]])
        elif type(lista2[n]) == list and type(lista1[n]) == int:
            salida = compararListaLista([lista1[n]], lista2[n])
        elif type(lista1[0]) == type(lista2[0]) == list:
            salida = compararListaLista(lista1[n], lista2[n])

        if salida != 0:
            return salida

    if len(lista1) != len(lista2):
        return 1 if len(lista1) < len(lista2) else -1

    return 0


class Elemento:
    def __init__(self, cuerpo):
        self.cuerpo = cuerpo

    def __lt__(self, other):
        return compararListaLista(self.cuerpo, other.cuerpo) == 1

    def __eq__(self, other):
        return self.cuerpo == other.cuerpo

    def __str__(self):
        return str(self.cuerpo)


lista = []
lista.append(Elemento([[2]]))
lista.append(Elemento([[6]]))

while True:
    entrada1 = eval(input())
    entrada2 = eval(input())
    entrada3 = input()

    lista.append(Elemento(entrada1))
    lista.append(Elemento(entrada2))

    if entrada3 == "-":
        break

lista.sort()
i1 = lista.index(Elemento([[2]])) + 1
i2 = lista.index(Elemento([[6]])) + 1

for i in lista:
    print(i)
print(i1 * i2)