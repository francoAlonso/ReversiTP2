# -*- coding: utf-8 -*-
import random
import csv

def grabarUsuario(archivo,nombre,puntaje,PJ,PG,PP,PE,espacio):
	archivo.write(nombre + ',' + str(puntaje) + ',' + str(PJ) + ',' + str(PG) + ',' + str(PP) + ',' + str(PE) + espacio)
	
def leer (file,default):
	with open(file, 'r') as fileUsuario:
		linea = fileUsuario.readline()
		if linea:
			return linea.split(',')
		else:
			return default.split(',')


#Resetea el archivo borrando todos los usuarios
def resetearArchUsuarios(file):#Se le pasa Usuarios.csv, Crea nuevamente el archivo usuarios con las keys correspondientes
	archivo = open(file,'w')
	archivo.write('Nombre,Puntaje,PartGanados,PartPerdidos,PartEmpatados,PartJugados\n')


# Se le pasa Usuarios.csv, Crea nuevamente el archivo usuarios con las keys y deja agregar datos de jugadores
def cargarArchUsuarios(file):
	with open(file, 'w') as archivo:
		archivo.write('Nombre,Puntaje,PartGanados,PartPerdidos,PartEmpatados,PartJugados\n')
		respuesta = "Y"
		j=1

		while respuesta != 'N':
			print 'Por favor ingresar los datos para el usuario numero ', j

			Nombre = raw_input('Por favor ingresar nombre del jugador')
			Puntaje = raw_input('Por favor ingresar puntaje del jugador')
			PartGanados = raw_input('Por favor ingresar la cantidad de partidos ganados del jugador')
			PartPerdidos = raw_input('Por favor ingresar la cantidad de partidos perdidos del jugador')
			PartEmpatados = raw_input('Por favor ingresar la cantidad de partidos empatados del jugador')
			PartJugados = str(int(PartGanados)+int(PartPerdidos)+int(PartEmpatados))

			archivo.write(Nombre + ',' + Puntaje + ',' + PartGanados + ',' + PartPerdidos + ',' + PartEmpatados + ',' + PartJugados + '\n')

			j=j+1

			respuesta = raw_input('Desea seguir ingresando jugadores? Y/N').upper()

def novedadesUsuarios(file):#Se le pasa novUsuarios.csv, Funciona igual que cargarArchUsuarios solo que creamos otro archivo para luego hacer apareo con usuarios original
	cargarArchUsuarios(file) #Necesita un nombre que NO sea Usuarios.csv, novUsuarios.csv funciona

# Usado para apareo luego. Cuenta cuantas lineas tiene el archivo.
def contarLineas(file):
	reader = csv.reader(file, delimeter=',')
	return len(list(reader))

# Se le pasan Usuarios.csv y novUsuarios.csv en ese orden para realizar el apareo
def apareoNovedades(file1,file2):
	with open(file1, 'r+') as archivo1, open(file2, 'r+') as archivo2:
		usuariosLength = contarLineas(archivo1)
		Nom, Puntaje, PG, PP, PE, PJ = leer(archivo1,'END,0,0,0,0,0')
		Nom_n, Puntaje_n, PG_n, PP_n, PE_n, PJ_n = leer(archivo2,'END,0,0,0,0,0')
		while Nom != 'END': #Mientras el archivo 1 no llegue al EoF
			cont=0
			if Nom == Nom_n: #Si el nombre en archivo 1 coincide con el archivo 2, actualiza los datos
				PuntajeNuevo=int(Puntaje)+int(Puntaje_n)
				PGNuevo = int(PG) + int(PG_n)
				PPNuevo = int(PP) + int(PP_n)
				PENuevo = int(PE) + int(PE_n)
				PJNuevo = int(PJ) + int(PJ_n)
				grabarUsuario(archivo1, Nom, PuntajeNuevo, PGNuevo, PPNuevo, PENuevo, PJNuevo, '\n')
				grabarUsuario(archivo2,'END','0','0','0','0','0','\n')
				leer(file2,'END,0,0,0,0,0')
			elif Nom != Nom_n: #Para ver si un nombre no esta en toda la lista, vemos si el contador llega a la misma longitud que las lineas del archivo 1
				cont+=cont
				leer(archivo1,'END,0,0,0,0,0')
			if cont == usuariosLength:
				grabarUsuario(archivo1,Nom_n,Puntaje_n,PG_n,PP_n,PE_n,PJ_n,'\n')

#Genera la cantidad de usuarios aleatorios que el usuario desee
def usuariosAleatorios(file):
	with open(file, 'w') as archivo:
		archivo.write('Nombre,Puntaje,PartGanados,PartPerdidos,PartEmpatados,PartJugados\n')
		generados = input('¿Cuántos usuarios de forma aleatoria desea generar?')
		for i in range(generados):
			nombre_aleatorio = [random.choice('sa') for j in range(4)]
			nombre_aleatorio = ''.join(nombre_aleatorio)
			puntaje, PJ, PG, PP, PE = random.randrange(10), random.randrange(10), random.randrange(10), random.randrange(10), random.randrange(10)
			archivo.seek(0,2)
			grabarUsuario(archivo, nombre_aleatorio, puntaje, PJ, PG, PP, PE, '\n')


#Pasa los datos de Usuarios.csv a una lista para luego ser ordenados
def crearLista (file):

	with open(file,'r') as my_file:
		reader = csv.reader(my_file, skipinitialspace=True)
		header=next(reader)
		lista=[dict(zip(header,map(str,row))) for row in reader]
		return lista


#Visualizar todos los usuarios con sus respectivos valores (mostrado alfabeticamente)
def visualizar(file):
	listaUsu = crearLista(file)
	listaUsuOrdenada = sorted(listaUsu, key=lambda k:k['Nombre'])
	for i in range (0,len(listaUsuOrdenada)):
		print listaUsuOrdenada[i],'\n'
	


#"main"
#ingreso=accionARealizar()
#if ingreso=RESETEAR:
#	resetear()
#elif ingreso=RANDOM:
#	usuariosAleatorios()
		
