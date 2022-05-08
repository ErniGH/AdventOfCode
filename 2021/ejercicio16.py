def ObtenerCadenaBinaria(cadenaHexadecimal):
    salida = []
    traductor = {
        "0": ["0", "0", "0", "0"],
        "1": ["0", "0", "0", "1"],
        "2": ["0", "0", "1", "0"],
        "3": ["0", "0", "1", "1"],
        "4": ["0", "1", "0", "0"],
        "5": ["0", "1", "0", "1"],
        "6": ["0", "1", "1", "0"],
        "7": ["0", "1", "1", "1"],
        "8": ["1", "0", "0", "0"],
        "9": ["1", "0", "0", "1"],
        "A": ["1", "0", "1", "0"],
        "B": ["1", "0", "1", "1"],
        "C": ["1", "1", "0", "0"],
        "D": ["1", "1", "0", "1"],
        "E": ["1", "1", "1", "0"],
        "F": ["1", "1", "1", "1"]
    }
    for c in cadenaHexadecimal:
        salida += traductor[c]

    return salida


def LeerCadenaBinaria(cadenaBinaria, indice, tam):
    salida = []
    for i in range(indice, indice + tam):
        salida += cadenaBinaria[i]

    return salida, indice + tam


def ObtenerVersion(cadenaBinaria, indice):
    return LeerCadenaBinaria(cadenaBinaria, indice, 3)


def ObtenerTipo(cadenaBinaria, indice):
    return LeerCadenaBinaria(cadenaBinaria, indice, 3)


t = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7",
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}


def AnalizarCadena(cadena):
    cadenaBinaria = ObtenerCadenaBinaria(cadena)
    return AnalizarCadenaBinaria(cadenaBinaria, False)



profundidad = 0


def AnalizarCadenaBinaria(cadenaBinaria, entera):
    global profundidad
    profundidad += 1

    salida = 0
    print("-"*profundidad + "CB", cadenaBinaria)
    version, indice = ObtenerVersion(cadenaBinaria, 0)
    print("v", t["".join(version)])
    tipo, indice = ObtenerTipo(cadenaBinaria, indice)
    print("t", t["".join(tipo)])

    salida += int(t["".join(version)])

    if t["".join(tipo)] == "4":
        iterar = True
        numero = ""
        while iterar:
            actual, indice = LeerCadenaBinaria(cadenaBinaria, indice, 5)
            if actual[0] == "0":
                iterar = False
            numero += t["".join(actual[1:])]
        print(numero)
    else:
        id, indice = LeerCadenaBinaria(cadenaBinaria, indice, 1)
        print("i", id[0])
        if id[0] == "0":
            # los siguientes 15 bits son un número que representa la longitud total en bits de los subpaquetes contenidos en este paquete.
            longitud, indice = LeerCadenaBinaria(cadenaBinaria, indice, 15)
            longitud = int("".join(longitud), 2)
            print("l", longitud)
            subcadena, indice = LeerCadenaBinaria(cadenaBinaria, indice, longitud)
            salida += AnalizarCadenaBinaria(subcadena, True)[0]

        else:
            # los siguientes 11 bits son un número que representa el número de subpaquetes contenidos inmediatamente por este paquete.
            cantidad, indice = LeerCadenaBinaria(cadenaBinaria, indice, 11)
            cantidad = int("".join(cantidad), 2)
            print("c", cantidad)
            for i in range(cantidad):
                salidaObtenida, indiceObtenido = AnalizarCadenaBinaria(cadenaBinaria[indice:], False)
                salida += salidaObtenida
                indice += indiceObtenido

    if indice != len(cadenaBinaria) and entera:
        salida += AnalizarCadenaBinaria(cadenaBinaria[indice:], True)[0]

    profundidad -= 1
    return salida, indice


print("suma", AnalizarCadena("C20D7900A012FB9DA43BA00B080310CE3643A0004362BC1B856E0144D234F43590698FF31D249F87B8BF1AD402389D29BA6ED6DCDEE59E6515880258E0040A7136712672454401A84CE65023D004E6A35E914BF744E4026BF006AA0008742985717440188AD0CE334D7700A4012D4D3AE002532F2349469100708010E8AD1020A10021B0623144A20042E18C5D88E6009CF42D972B004A633A6398CE9848039893F0650048D231EFE71E09CB4B4D4A00643E200816507A48D244A2659880C3F602E2080ADA700340099D0023AC400C30038C00C50025C00C6015AD004B95002C400A10038C00A30039C0086002B256294E0124FC47A0FC88ACE953802F2936C965D3005AC01792A2A4AC69C8C8CA49625B92B1D980553EE5287B3C9338D13C74402770803D06216C2A100760944D8200008545C8FB1EC80185945D9868913097CAB90010D382CA00E4739EDF7A2935FEB68802525D1794299199E100647253CE53A8017C9CF6B8573AB24008148804BB8100AA760088803F04E244480004323BC5C88F29C96318A2EA00829319856AD328C5394F599E7612789BC1DB000B90A480371993EA0090A4E35D45F24E35D45E8402E9D87FFE0D9C97ED2AF6C0D281F2CAF22F60014CC9F7B71098DFD025A3059200C8F801F094AB74D72FD870DE616A2E9802F800FACACA68B270A7F01F2B8A6FD6035004E054B1310064F28F1C00F9CFC775E87CF52ADC600AE003E32965D98A52969AF48F9E0C0179C8FE25D40149CC46C4F2FB97BF5A62ECE6008D0066A200D4538D911C401A87304E0B4E321005033A77800AB4EC1227609508A5F188691E3047830053401600043E2044E8AE0008443F84F1CE6B3F133005300101924B924899D1C0804B3B61D9AB479387651209AA7F3BC4A77DA6C519B9F2D75100017E1AB803F257895CBE3E2F3FDE014ABC")[0])