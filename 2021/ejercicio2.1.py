profundidad = 0
delante = 0
aim = 0

while True:
    palabra, valor = input().split(" ")
    if palabra == "up":
        aim -= int(valor)
    elif palabra == "down":
        aim += int(valor)
    elif palabra == "forward":
        delante += int(valor)
        profundidad += aim * int(valor)

    print(profundidad, delante, profundidad*delante)