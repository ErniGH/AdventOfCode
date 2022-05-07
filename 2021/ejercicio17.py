entradaX = (217, 240)
entradaY = (-126, -69)

ht = 0

for i in range(400):
    for j in range(-400, 400):
        hm = 0
        dx = i
        dy = j
        p = [0, 0]
        while True:
            p[0] += dx
            p[1] += dy
            if dx > 0:
                dx -= 1
            dy -= 1

            if entradaX[0] <= p[0] <= entradaX[1] and entradaY[0] <= p[1] <= entradaY[1]:
                print(i, j)
                ht += 1
                break

            if dx == 0 and p[1] < entradaY[0]:
                break

print(ht)
