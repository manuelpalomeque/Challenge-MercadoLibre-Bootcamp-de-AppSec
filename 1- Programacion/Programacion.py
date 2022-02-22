# 1) Haga una función donde se analicen dos números y retorne
# “true“ si el número2 es mayor al numero1, -1 si son iguales y “false” si numero1 es
# mayor que numero2

def NumberChallenge(n1, n2):
    # code goes here


print(NumberChallenge(input()))


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
#Salida final: ooookkr

def StringChallenge1(strParam1):
    # code goes here
    return strParam1


# keep this function call here
print(StringChallenge1(input()))


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

def StringChallenge2(strParam2):
    # code goes here
    return strParam2

# keep this function call here
print(StringChallenge2(input()))
