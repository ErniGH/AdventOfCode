def v(c):
    if ord(c) > 96:
        return ord(c) - 96
    else:
        return ord(c) - 38


valor = 0
while True:
    entrada1 = input()
    if entrada1 == "-":
        break

    entrada2 = input()
    entrada3 = input()

    for c in entrada1:
        if c in entrada2 and c in entrada3:
            valor += v(c)
            break

print(valor)
