#Debe haber una lista facia creada anteriormente, la llamamos listaUsuarios
def crearLista (file): #Pasa los datos de Usuarios.csv a una lista para luego ser ordenados
	import csv
	with open(file,'r') as my_file:
		reader = csv.reader(my_file, skipinitialspace=True)
		header=next(reader)
		lista=[dict(zip(header,map(str,row))) for row in reader]
		return lista

def ordenarLista (listaInicial): #Se le pasa la lista creada anteriormente
	lista=sorted(listaInicial, key=lambda k:int(k['Puntaje']), reverse=True)#ordena por puntaje de mayor a menor
	j=1
	for i in range(0,(len(lista)-1)):
		if  lista[j-1]['Puntaje']==lista[j]['Puntaje']: #Si en el registro de un jugador el puntaje es igual al del siguiente
			if int(lista[j-1]['PartGanados'])<int(lista[j]['PartGanados']): #Si el PG del segundo es mas grande que el del primero los cambia de lugar
				aux=lista[j-1]	
				lista[j-1]=lista[j]
				lista[j]=aux
			if int(lista[j-1]['PartGanados'])==int(lista[j]['PartGanados']): #Si sus PG son iguales, ingresa los nombres en una lista pequena y los ordena alfabeticamente
				lst=[lista[j-1]['Nombre'],lista[j]['Nombre']]
				lst.sort()
				if lista[j]['Nombre']==lst[0]: #Si el primer nombre de la lst es igual al siguiente de la lista usuarios, cambia de lugar
					aux=lista[j-1]
					lista[j-1]=lista[j]
					lista[j]=aux
		j=j+1
	return lista

def imprimirLista(lista):
	j=1
	for i in range(0,9):
		print 'Puesto {}: {} con {} puntos y {} partidos ganados'.format(j,lista[i]['Nombre'],lista[i]['Puntaje'],lista[i]['PartGanados'])
		j=j+1
		
