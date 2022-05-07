total = 0
entrada= []
while True:
    nuevo = input()
    if nuevo == "fin":
        break
    entrada.append(nuevo)


for i in entrada:
    output = i.split("|")[1].split(" ")
    for palabra in output:
        if len(palabra) == 2 or len(palabra) == 4 or len(palabra) == 3 or len(palabra) == 7:
            total += 1
print(total)