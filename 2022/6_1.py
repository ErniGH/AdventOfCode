
entrada = input()
for i in range(len(entrada)-3):
    subString = entrada[i:i+4]
    if len(set(subString)) == len(subString):
        print(i + 4)
        break