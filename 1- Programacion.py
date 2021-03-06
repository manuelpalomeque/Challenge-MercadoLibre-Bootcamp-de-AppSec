# 1) Haga una función donde se analicen dos números y retorne
# “true“ si el número2 es mayor al numero1, -1 si son iguales y “false” si numero1 es
# mayor que numero2

n1 = input('Ingrese el valor del primer numero:')
n2 = input('Ingrese el valor del segundo numero:')

def NumberChallenge(n1, n2):
    if n2 > n1:
        return True
    elif n2 == n1:
        return -1
    else:
        return False

print(NumberChallenge(n1, n2))

# 2) Desafío de cuerdas
# Haga que la función StringChallenge( str ) tome el parámetro str que se pasa, que será
# una cadena que contenga letras del alfabeto, y devuelva una nueva cadena según las
# siguientes reglas. Cada vez que encuentre una M mayúscula, duplique el carácter
# anterior (luego elimine la M), y cada vez que encuentre una N mayúscula, elimine el
# siguiente carácter de la cadena (luego elimine la N). Todos los demás caracteres de la
# cadena serán letras minúsculas. Por ejemplo: "abcNdgM" debería devolver "abcgg". La
# cadena final nunca estará vacía.
# Ejemplos
# Entrada: "MrtyNNgMM"
# Salida: rtyggg
# Salida final: rtygggEntrada: "oMoMkkNrrN"
# Salida: ooookkr
# Salida final: ooookkr

strParam1 = 'MrtyNNgMM'
def stringChallenge(strCadena,str1,str2):
    strParam2 = list(strCadena)
    # Primer parte, con la letra 'M':
    lista1 = []
    cont1 = 0
    # ubico el indice donde se encuentra la letra M:
    for x in strCadena:
        if x == str1:
            lista1.append(cont1)
            cont1 += 1
        else:
            cont1 += 1
    # Duplico el caracter anterior:
    for x in lista1:
        if x > 0:
            strParam2[x] = strParam2[x-1]

    # Segunda parte, con la letra 'N':
    lista2 = []
    cont2 = 0
    # ubico el indice donde se encuentra la letra N
    for x in strParam2:
        if x == str2:
            lista2.append(cont2)
            cont2 += 1
        else:
            cont2 += 1
    # elimino el caracter siguiente a N
    for x in lista2:
        if x < len(lista2):
            strParam2[x] = strParam2[x+1]

    strParam2 = "".join(strParam2)  # cambio de lista a str
    strParam2 = strParam2.replace(str2, '')  # elimino la letra M
    strParam2 = strParam2.replace(str1, '')  # elimino N
    strParam2 = strParam2.lower()  # me aseguro que el valor quede en minuscula siempre

    if len(strParam2) == 0:
        return 'No se puede procesar, la cadena quedaria vacia. Cadena original: {} '.format(strCadena)
    else:
        return strParam2

stringChallenge(strParam1, 'M', 'N')

# 3) Desafío de cuerdas
# Haga que la función StringChallenge( str ) tome el parámetro str y codifique el mensaje
# de acuerdo con la siguiente regla: codifique cada letra en su posición numerada
# correspondiente en el alfabeto. Los símbolos y espacios también se utilizarán en la
# entrada. Por ejemplo: si str es "af5c a#!" ¡ entonces su programa debería
# devolver 1653 1#! .
# Ejemplos
# Entrada: "hola 45"
# Salida: 85121215 45Entrada: "jaj-a"
# Salida: 10110-1

strParam2 = 'hola 45'

def stringChallenge1(strCadena):
    # me aseguro de que la cadena ingresada quede en minuscula siempre:
    strCadena = strCadena.lower()
    # vuelvo el dato en tipo list:
    strCadena = list(strCadena)
    # formalice la lista con las letras del alfabeto:
    alfabeto = list(string.ascii_lowercase)

    # Inicializo  las listas que necesitare para analizar:
    strParametro_3 = strCadena
    indices_alfabeto = []
    indice_strParametro3 = []
    cont1 = 0

    # Recorro la lista strParametro_3 y verifico si el elemento coincide con algun elemento de la lista alfabeto
    for x in strParametro_3:
        cont2 = 0
        for y in alfabeto:
            if x == y:
                indices_alfabeto.append(cont2 + 1)  # guardo el indice donde coincide con alfabeto
                indice_strParametro3.append(cont1)  # guardo el indice donde hay una letra en strParam_2
                cont2 += 1
            else:
                cont2 += 1
        cont1 += 1

    # En base a los indices guardados, los cuales coinciden con una posicion de una letra en strParam_2,
    # reemplazo la ubicacion con el numero que corresponde en base a la posicion en el alfabeto
    for i in indice_strParametro3:
        strParametro_3[i] = str(indices_alfabeto[i])
        # con str() me aseguro que los numeros cambien de tipo de dato a str (sino quedan en tipo int)

    # vuelvo a str la lista:
    strParametro_3 = "".join(strParametro_3)

    return strParametro_3

stringChallenge1(strParam_2)