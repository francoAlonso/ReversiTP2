#Debe haber una lista facia creada anteriormente, la llamamos listaUsuarios
def crearLista (file,listName): #Pasa los datos de Usuarios.csv a una lista para luego ser ordenados
	import csv
	with open (file, 'rb') as l:
		reader= csv.reader(l)
		listName=list(reader)

def ordenarLista (lista): #Se le pasa la lista creada anteriormente
	lista.sort(key=lambda datos:datos[1], reverse=True) #ordena por puntaje de mayor a menor
	while line in lista:
		i=0
		if  lista[i][1]==lista[i+1][1]: #Si en el registro de un jugador el puntaje es igual al del siguiente
			if lista[i][2]<lista[i+1][2]: #Si el PG del segundo es mas grande que el del primero los cambia de lugar
				aux=lista[i]
				lista[i]=lista[i+1]
				lista[i+1]=aux
			if lista[i][2]==lista[i+1][2]: #Si sus PG son iguales, ingresa los nombres en una lista pequena y los ordena alfabeticamente
				lst=[lista[i][0],lista[i+1][0]]
				lst.sort()
				if lista[i+1][0]==lst[0]: #Si el primer nombre de la lst es igual al siguiente de la lista usuarios, cambia de lugar
					aux=lista[i+1]
					lista[i]=lista[i+1]
					lista[i+1]=aux
		i+=1

def imprimirLista(lista):
	while line in lista:
		print lista
				
