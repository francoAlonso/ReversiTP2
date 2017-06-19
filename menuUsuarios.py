def grabarUsuario(archivo,nombre,puntaje,PJ,PG,PP,PE,espacio):
	usuarios.write(nombre+','+puntaje+','+PJ+','+PG+','+PP+','+PE+espacio)
	
def leer (file,default):
    linea = file.readline()
    if linea:
    	return linea.split(',')
    else:
    	return default.split(',')


#Resetea el archivo borrando todos los usuarios
def resetearArchUsuarios(file):#Se le pasa Usuarios.csv, Crea nuevamente el archivo usuarios con las keys correspondientes
	open (file,'w')
	file.write('Nombre,Puntaje,PartGanados,PartPerdidos,PartEmpatados,PartJugados')
	
def cargarArchUsuarios(file):#Se le pasa Usuarios.csv, Crea nuevamente el archivo usuarios con las keys y deja agregar datos de jugadores
	open (file,'w')
	file.write('Nombre,Puntaje,PartGanados,PartPerdidos,PartEmpatados,PartJugados\n')
	i=Y
	j=1
	while i!='N':
		print 'Por favor ingresar los datos para el usuario numero ',j
		Nombre=raw_imput('Por favor ingresar nombre del jugador')
		Puntaje=raw_imput('Por favor ingresar puntaje del jugador')
		PartGanados=raw_imput('Por favor ingresar la cantidad de partidos ganados del jugador')
		PartPerdidos=raw_imput('Por favor ingresar la cantidad de partidos perdidos del jugador')
		PartEmpatados=raw_imput('Por favor ingresar la cantidad de partidos empatados del jugador')
		PartJugados= int(PartGanados)+int(PartPerdidos)+int(PartEmpatados)
		file.write(Nombre,',',Puntaje,',',PartGanados,',',PartPerdidos,',',PartEmpatados,',',PartJugados,'\n')
		j=j+1
		i=raw_imput('Desea seguir ingresando jugadores? Y/N')
		
def novedadesUsuarios(file):#Se le pasa novUsuarios.csv, Funciona igual que cargarArchUsuarios solo que creamos otro archivo para luego hacer apareo con usuarios original
	cargarArchUsuarios(file) #Necesita un nombre que NO sea Usuarios.csv, novUsuarios.csv funciona
	
def contarLineas(file): #Usado para apareo luego
	import csv
	with open(file,'r') as f:
		reader=csv.reader(file,delimeter=',')
		data=list(reader)
		row_count=len(data)
	return row_count

def apareoNovedades(file1,file2):# Se le pasan Usuarios.csv y novUsuarios.csv en ese orden para realizar el apareo
	open(file1,'r+')
	open(file2,'r+')
	usuariosLength=contarLineas(file1)
	Nom,Puntaje,PG,PP,PE,PJ=leer(file1,'END,0,0,0,0,0')
	Nom_n,Puntaje_n,PG_n,PP_n,PE_n,PJ_n=leer(file2,'END,0,0,0,0,0')
	while Nom!='END': #Mientras el archivo 1 no llegue al EoF
		cont=0
		if Nom==Nom_n: #Si el nombre en archivo 1 coincide con el archivo 2, actualiza los datos
			PuntajeNuevo=int(Puntaje)+int(Puntaje_n)
			PGNuevo=int(PG)+int(PG_n)
			PPNuevo=int(PP)+int(PP_n)
			PENuevo=int(PE)+int(PE_n)
			PJNuevo=int(PJ)+int(PJ_n)
			grabarUsuario(file1,Nom,PuntajeNuevo,PGNuevo,PPNuevo,PENuevo,PJNuevo,' ')
			grabarUsuario(file2,'END','0','0','0','0','0',' ')
			leer(file2,'END,0,0,0,0,0')
		else Nom!=Nom_n: #Para ver si un nombre no esta en toda la lista, vemos si el contador llega a la misma longitud que las lineas del archivo 1
			cont=cont+1
			leer(file1,'END,0,0,0,0,0')
		if cont=usuariosLength:
			grabarUsuario(file1,Nom_n,Puntaje_n,PG_n,PP_n,PE_n,PJ_n,'\n')

#Genera la cantidad de usuarios aleatorios que el usuario desee
def usuariosAleatorios(file):
	import random
	open (file,'w')
	file.write('Nombre,Puntaje,PartGanados,PartPerdidos,PartEmpatados,PartJugados\n')
        generados=input('¿Cuántos usuarios de forma aleatoria desea generar?')
        for i in range [1, generados+1]
			nombre_aleatorio=[random.choice("abcdefghijklmnopqrstuvwxyz") for j in range(4)]
			nombre_aleatorio=''.join(nombre_aleatorio)
			puntaje, PJ, PG, PP, PE=random.randrange(10), random.randrange(10), random.randrange(10),random.randrange(10),random.randrange(10)
			usuarios.seek(0,2)
			grabarUsuario(file, nombre_aleatorio, puntaje, PJ, PG, PP, PE,'')
			
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
		
