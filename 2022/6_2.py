
entrada = input()
for i in range(len(entrada)-13):
    subString = entrada[i:i+14]
    if len(set(subString)) == len(subString):
        print(i + 14)
        break
