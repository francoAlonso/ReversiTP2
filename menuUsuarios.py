def grabarUsuario(archivo,nombre,puntaje,PJ,PG,PP,PE,espacio):
usuarios.write(nombre+','+puntaje+','+PJ+','+PG+','+PP+','+PE+espacio)

def accionARealizar():
	ingreso=raw_input('Ingrese la acción a realizar')
	return ingreso


def resetear():
    if ingreso=RESETEAR:
		usuarios=open('usuarios.csv', 'w')
		leer(usuarios, 'NONE,0,0,0,0,0,0')
        while linea in usuarios:
            usuarios.remove(linea)
            leer(usuarios, 'NONE,0,0,0,0,0,0')

def usuariosAleatorios():
	import random
        generados=input('¿Cuántos usuarios de forma aleatoria desea generar?')
        for i in range [1, generados+1]
			nombre_aleatorio=[random.choice("abcdefghijklmnopqrstuvwxyz") for j in range(4)]
			nombre_aleatorio=''.join(nombre_aleatorio)
			puntaje, PJ, PG, PP, PE=random.randrange(10), random.randrange(10), random.randrange(10),random.randrange(10),random.randrange(10)
			usuarios.seek(0,2)
			grabarUsuario(usuarios, nombre_aleatorio, puntaje, PJ, PG, PP, PE,'')
	

#"main"
ingreso=accionARealizar()
if ingreso=RESETEAR:
	resetear()
elif ingreso=RANDOM:
	usuariosAleatorios()
		
