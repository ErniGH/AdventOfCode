
contador = 0
while True:
    entrada = input()
    if entrada == "-":
        break
    elfos = entrada.split(",")
    elfo1 = [int(i) for i in elfos[0].split("-")]
    elfo2 = [int(i) for i in elfos[1].split("-")]

    if (elfo1[0] <= elfo2[0] and elfo1[1] >= elfo2[1]) or (elfo2[0] <= elfo1[0] and elfo2[1] >= elfo1[1]):
        contador += 1

print(contador)