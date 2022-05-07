profundidad = 0
delante = 0

while True:
    palabra, valor = input().split(" ")
    if palabra == "up":
        profundidad -= int(valor)
    elif palabra == "down":
        profundidad += int(valor)
    elif palabra == "forward":
        delante += int(valor)

    print(profundidad, delante, profundidad*delante)