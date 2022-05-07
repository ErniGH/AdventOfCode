
anterior = 1000000
total = 0

while True:
    siguiente = int(input())
    if siguiente > anterior:
        total += 1
    anterior = siguiente
    print(total)