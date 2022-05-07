listaEntradas = [int(i) for i in input().split(",")]
for i in range(256):
    print(i)
    for j in range(len(listaEntradas)):
        listaEntradas[j] -= 1
        if listaEntradas[j] == -1:
            listaEntradas[j] = 6
            listaEntradas.append(8)

print(len(listaEntradas))