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


total = 0
contador = 1
while True:
    entrada1 = eval(input())
    entrada2 = eval(input())
    entrada3 = input()

    if entrada3 == "-":
        break

    if compararListaLista(entrada1, entrada2) == 1:
        total += contador
        print(contador)
    contador += 1

print(total)