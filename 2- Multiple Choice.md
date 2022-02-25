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

3- ¿Cuál de los siguientes strings NO REPRESENTA un HEADER HTTP durante una petición de tipo GET?
 
    a) Host
    b) Content-Type
    c) bcrypt
    d) Cookie

RESPUESTA: Opción c

4- ¿Cuál de los siguientes String NO REPRESENTA a un header HTTP de respuesta a una petición GET desde un servidor web?
 
    a) Content-Length
    b) Base64
    c) Location
    d) Set-Cookie

RESPUESTA: Opción b

5- ¿Cuál de las siguientes afirmaciones acerca del protocolo DNS es correcta?
 
    a) 8.8.8.8 es un DNS publico de Google que puede ser configurado en un router de hogar como también en un host 
    linux modificando el archivo /etc/resolv.conf
    b) DNS usa SQL como lenguaje para sus queries
    c) DNS usualmente trabaja en el puerto 80
    d) Los navegadores web utilizan el protocolo DNS para traducir de direcciones IP a nombres de dominios

RESPUESTA: Opción d

6- ¿Cuál de las siguientes afirmaciones es correcta acerca de Procesos y Threads?
 
    a) Un proceso es una instancia en ejecución de un programa que contiene uno o varios threads
    b) Un cambio realizado en el proceso padre afecta a todos los procesos hijos
    c) Los threads ejecutan en un espacio de memoria compartida con sus correspondientes procesos.

RESPUESTA: Opción a

