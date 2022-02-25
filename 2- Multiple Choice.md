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

7- ¿Cuáles de los siguientes comandos de Linux no puede ser aplicado a un directorio?
     
    a) touch
    b) rm -r
    c) cat
    d) file

RESPUESTA: Opción d

8- ¿Qué vulnerabilidad puedes identificar en este fragmento de código?
    
    const express = require("express");
    const app = express();
    app.GET('/users', function (request, response) {
        let url_address = request.query.callback_address;
        response.redirect(302,'https://{url_address}/home');
    });
    
     
    Información útil:
    o	SSRF (Server Side Request Forgery): Permite a un atacante acceder a un servidor arbitrario usando un servidor de la red interna como pivot.
    o	IDOR (Insecure Direct Object Reference): Mala práctica de desarrollo donde los identificadores de objeto son predecibles y no tienen controles de autorización.
    o	Open Redirect: permite a los atacantes dirigir a las víctimas a direcciones URL maliciosas.
    o	Broken Access Control: Los atacantes autenticados obtienen acceso a recursos no autorizados, esto se debe a una falta de validación en los permisos de los usuarios.
     
    a) SSRF
    b) Broken Access Control
    c) Open Redirect
    d) IDOR

RESPUESTA: Opción c

9- ¿Qué vulnerabilidad puede identificar en el fragmento de código responsable de consultar una dirección a partir de su ID?
 
    from django.http import HttpResponse
    from django.db import connection
    
    def address(request):
        id = request.GET.get("id", "")
        cursor = connection.cursor()
        cursor.execute("SELECT address FROM addresses_user WHERE id=%s" % id) 
        row = cursor.fetchone()
        return HttpResponse("Address is %s" % row[0])
    
    }
     
    Información útil:
    o	SSRF (Server Side Request Forgery): permite a los atacantes acceder a servidores (o dominios) arbitrarios utilizando un servidor de la red interna  como pivote.
    o	RCE (Remote Code Execution): Permite a un atacante ejecutar remotamente código malicioso en una computadora.
    o	SQL Injection: Es una vulnerabilidad de seguridad web que permite a un atacante interferir en las consultas que una aplicación realiza a su base de datos.
    o	XSS: surge cuando falta la validación de entrada, no se aplica codificación de salida y puede inyectar javascript malicioso para que lo ejecuten otros usuarios de aplicaciones.
     
    a) SQL Injection
    b) SSRF
    c) XSS
    d) RCE

RESPUESTA: Opción c

