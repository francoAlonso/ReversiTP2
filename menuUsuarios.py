def grabarUsuario(archivo,nombre,puntaje,PJ,PG,PP,PE,espacio):
usuarios.write(nombre+','+puntaje+','+PJ+','+PG+','+PP+','+PE+espacio)


def accionARealizar():
	ingreso=raw_input('Ingrese la acción a realizar')
	return ingreso

#Resetea el archivo borrando todos los usuarios
def resetearArchUsuarios(file):#Se le pasa Usuarios.csv, Crea nuevamente el archivo usuarios con las keys correspondientes
	open (file,'w')
	file.write('Nombre,Puntaje,PartGanados,PartPerdidos,PartEmpatados,PartJugados')

#Genera la cantidad de usuarios aleatorios que el usuario desee
def usuariosAleatorios():
	import random
        generados=input('¿Cuántos usuarios de forma aleatoria desea generar?')
        for i in range [1, generados+1]
			nombre_aleatorio=[random.choice("abcdefghijklmnopqrstuvwxyz") for j in range(4)]
			nombre_aleatorio=''.join(nombre_aleatorio)
			puntaje, PJ, PG, PP, PE=random.randrange(10), random.randrange(10), random.randrange(10),random.randrange(10),random.randrange(10)
			usuarios.seek(0,2)
			grabarUsuario(usuarios, nombre_aleatorio, puntaje, PJ, PG, PP, PE,'')
			
def crearLista (file): #Pasa los datos de Usuarios.csv a una lista para luego ser ordenados
	import csv
	with open(file,'r') as my_file:
		reader = csv.reader(my_file, skipinitialspace=True)
		header=next(reader)
		lista=[dict(zip(header,map(str,row))) for row in reader]
		return lista
			
#Visualizar todos los usuarios con sus respectivos valores (mostrado alfabeticamente)
def visualizar(file,lista):
	listaUsu=crearLista(file)
	listaUsuOrdenada=sorted(listaUsu, key=lambda k:k['Nombre'])
	for i in range (0,len(listaUsuOrdenada)):
		print listaUsuOrdenada[i],'\n'
	


#"main"
ingreso=accionARealizar()
if ingreso=RESETEAR:
	resetear()
elif ingreso=RANDOM:
	usuariosAleatorios()
		
