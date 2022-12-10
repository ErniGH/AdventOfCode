bosque = []

while True:
    entrada = input()
    if entrada == "-":
        break
    bosque.append(entrada)

validos = [[False for j in i]for i in bosque]

# Oeste -> Este
for i in range(len(bosque)):
    maximo = bosque[i][0]
    validos[i][0] = True
    for j in range(len(bosque[0])):
        if int(bosque[i][j]) > int(maximo):
            maximo = bosque[i][j]
            validos[i][j] = True

# Este -> Oeste
for i in range(len(bosque)):
    maximo = bosque[i][len(bosque)-1]
    validos[i][len(bosque)-1] = True
    for j in range(len(bosque[0])-1, 0, -1):
        if bosque[i][j] > maximo:
            maximo = bosque[i][j]
            validos[i][j] = True

# Norte -> Sur
for i in range(len(bosque[0])):
    maximo = bosque[0][i]
    validos[0][i] = True
    for j in range(len(bosque)):
        if bosque[j][i] > maximo:
            maximo = bosque[j][i]
            validos[j][i] = True

# Sur -> Norte
for i in range(len(bosque[0])):
    maximo = bosque[len(bosque)-1][i]
    validos[len(bosque)-1][i] = True
    for j in range(len(bosque[0])-1, 0, -1):
        if bosque[j][i] > maximo:
            maximo = bosque[j][i]
            validos[j][i] = True

total = 0
for i in validos:
    for j in i:
        if j:
            total += 1
print(total)