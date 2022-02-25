## MULTIPLE CHOICE QUESTIONS

1- ¿Qué método elegiría para encontrar la palabra "AppSec" dentro de un array de frases?

    frases = [
        "Bootcamp de AppSec",
        "Bootcamp de desarrollo",
        "Otro Bootcamp"
    ]
    string = "AppSec"

OPCIONES:

    OPCION 1
    for frase in frases:
        if string in frase:
            print(frase)
            
    OPCION 2
    for frase in frases:
        frase_length = len(frase)
        string_length = len(string)
        for index in range(frase_length - string_length + 1):
            substring = frase[index:string_length + index]
            if substring == string:
                print(frase)
                
    OPCION 3
    for frase in frases:
        try:
            frase.index(string)
            print(frase)
        except ValueError:
            pass
        
    OPCION 4
    for frase in frases:
        if frase.find(string) >= 0:
            print(frase)
     

RESPUESTA: Opción 1

2- ¿Cuál de las siguientes estrategias considera mejor para proteger las contraseñas almacenadas en una base de datos?
 
    a) Texto plano
    b) MD5
    c) Base64
    d) SHA256

RESPUESTA: Opción d



