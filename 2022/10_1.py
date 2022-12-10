registroTemporal = []
registroActual = 1
posicionesMagicas = [20, 60, 100, 140, 180, 220]
while True:
    entrada = input()
    if entrada == "-" or len(registroTemporal) > posicionesMagicas[-1]:
        break

    registroTemporal.append(registroActual)
    if entrada.split(" ")[0] == "addx":
        registroTemporal.append(registroActual)
        registroActual += int(entrada.split(" ")[1])

total = 0
for i in posicionesMagicas:
    total += i * registroTemporal[i-1]

print(total)
