# -*- coding: cp1252 -*-
#El archivo Usuarios.csv tiene 6 datos, los cuales se encuentran en este orden: Nombre,Puntaje,PJ,PG,PP,PE
#Esta funcion lee el archivo y si encuentra al final, devuelte una clave que indica el EoF

def leer (archivo,default):
    linea = usuarios.readline()
    if linea:
        return linea.split(',')
    else:
        return default.split(',')

#Lo unico que hace es grabar en Usuarios.csv los datos que queramos
#El 'espacio' solo es usado cuando se crea un jugador nuevo, para agregar el \n
def grabarUsuario(archivo,nombre,puntaje,PJ,PG,PP,PE,espacio):
    usuarios.write(nombre+','+puntaje+','+PJ+','+PG+','+PP+','+PE+espacio)

#Ingresa el nombre de usuario
def ingresarNombre():
    nombre_usuario=raw_input('Ingrese el nombre de usuario: ')
    return (nombre_usuario)
#Verifica que el nombre ingresado se encuentre en 4 y 8 digitos
def verificarNombreValido():
    global nombre_usuario
    while len(nombre_usuario)<4 or len(nombre_usuario)>8:
            nombre_usuario=raw_input('Ingrese un nombre entre 4 y 8 digitos: ')
   
#Es usado cuando aparece un nuevo jugador, si este ya existe no hace nada, si no, crea el nuevo jugador con los datos default(0)
#Como solo usamos el nombre, ponemos variables random para que pueda leer el archivo correctamente
def existeUsuario(archivo,nombre):
    nombre_usuario,a,b,c,d,e,f=leer(archivo,'NONE,0,0,0,0,0,0')
    while archivo:
        if (nombre_usuario!=nombre):
            grabarUsuario(archivo,nombre,'0','0','0','0','0','\n')
            nombre_usuario,a,b,c,d,e,f=leer(usuarios,'NONE,0,0,0,0,0')

#Actualiza datos en el Usuarios.csv luego de que termina una partida
def actualizarUsuarios(archivo,nombre,fichasJugador,fichasBot):
    nombre_usuario,puntaje,PJ,PG,PP,PE=leer (usuarios, 'NONE,0,0,0,0,0')
    #Pasamos los valores que necesitamos que sean numeros a numerico
    intPuntaje=int(puntaje)
    intPJ=int(PJ)
    intPG=int(PG)
    intPP=int(PP)
    intPE=int(PE)
    intPJ+=1
    intPuntaje=intPuntaje+(fichasJugador-fichasBot)
    if fichasJugador<fichasBot:
        intPP+=1
    elif fichasJugador>fichasBot:
        intPG+=1
    else:
        intPP=+1
        grabarUsuario(usuarios,nombre_usuario,intPuntaje,intPJ,intPG,intPP,intPE,' ')
