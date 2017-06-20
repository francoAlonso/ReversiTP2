import csv

#El archivo Usuarios.csv tiene 6 datos, los cuales se encuentran en este orden: Nombre,Puntaje,PJ,PG,PP,PE
#Esta funcion lee el archivo y si encuentra al final, devuelte una clave que indica el EoF
def leer(archivo, default):
	linea = archivo.readline()
	if linea:
		return linea.split(',')
	else:
		return default.split(',')

#Lo unico que hace es grabar en Usuarios.csv los datos que queramos
#El 'espacio' solo es usado cuando se crea un jugador nuevo, para agregar el \n
def grabarUsuario(file,nombre,puntaje,PJ,PG,PP,PE,espacio):
	file.write(nombre+','+puntaje+','+PJ+','+PG+','+PP+','+PE+espacio)

def contarLineas(file):
    reader = csv.reader(file, ',')
    return len(list(reader))

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
def verificarUsuarioInicial(file,nombre):
	nombre_usuario,a,b,c,d,e,f = leer(file,'END,0,0,0,0,0,0')
	last_pos = file.tell() #Nos va a decir donde se encuentra la linea en el archivo
	nombre_usuario,a,b,c,d,e,f = leer(file,'END,0,0,0,0,0,0') #Dos veces para que se saltee las keys
	usuariosLength = contarLineas(file)
	cont=0
	while nombre_usuario!='END':
		if (nombre_usuario!=nombre): #Ponemos un contador en el cual vemos si existe algun jugador con el nombre ingresado
			cont=cont+1
			last_pos=file.tell() 
			nombre_usuario,a,b,c,d,e,f=leer(file,'END,0,0,0,0,0,0')
		else:
			nombre_usuario='END'
			file.seek(last_pos)  #Para que salga del ciclo y deje el puntero en donde empieza la linea
	if cont==usuariosLength:
		grabarUsuario(file,nombre,'0','0','0','0','0','\n')

#Actualiza datos en el Usuarios.csv luego de que termina una partida
def actualizarUsuarios(file, nombre, nuevoPuntaje):
	last_pos=file.tell()
	nombre_usuario,puntaje,PJ,PG,PP,PE=leer(file, 'END,0,0,0,0,0')
	#Pasamos los valores que necesitamos que sean numeros a numerico
	intPuntaje=int(puntaje)
	intPJ=int(PJ)
	intPG=int(PG)
	intPP=int(PP)
	intPE=int(PE)
	intPJ+=1
	intPuntaje=intPuntaje+(nuevoPuntaje)
	if nuevoPuntaje < 0:
		intPP+=1
	elif nuevoPuntaje > 0:
		intPG+=1
	else:
		intPP=+1
	file.seek(last_pos) #Volvemos a la linea que debemos modificar
	grabarUsuario(file,nombre_usuario,intPuntaje,intPJ,intPG,intPP,intPE,' ')
