#Programa Principal, desde aqui haremos el menu
import os
from reversi import Reversi
import MenuJugar
import SortFile
import menuUsuarios

menu1=['1-Jugar','2-Ver Top 10','3-Cargar,generar o actualizar archivo Usuarios','0-Salir']
menu2=['1-Reset archivo Usuarios','2-Cargar nuevo arhivo Usuarios','3-Actualizar archivo Usuarios','4-Generar Usuarios aleatorio','5-Visualizar archivo Usuarios actual','0-Volver al Menu Principal']

ARCHIVO_USUARIOS = 'Usuarios.csv'

i=1
while i!=0:
    for k in menu1:
        print k,'\n'
    j=1
    i=input('Por favor ingresar la accion a realizar acorde al numero correspondiente\n')
    if i==1:
        # Habria que hacer que verifique e ingrese en uno solo
        nombre=MenuJugar.ingresarNombre()
        MenuJugar.verificarUsuarioInicial(ARCHIVO_USUARIOS, nombre)
        #ACA VA EL JUEGO
        puntaje = Reversi.jugar_reversi()
        MenuJugar.actualizarUsuarios(ARCHIVO_USUARIOS, nombre, puntaje)
    elif i == 2: #Ordenamiento top 10
        listaParaOrdenar=SortFile.crearLista(ARCHIVO_USUARIOS)
        listaUsuarios=SortFile.ordenarLista(listaParaOrdenar)
        SortFile.imprimirLista(listaUsuarios)
        while j != 0:
            j=input('Presione 0 para volver al menu principal\n')
    elif i==3:
        #Va a menuUsuarios
        while j!=0:
            for k in menu2:
                print k,'\n'
            j=input('Por favor ingresar la accion a realizar acorde al numero correspondiente\n')
            if j==1: #Resetear archivo usuarios, borra el anterior
                menuUsuarios.resetearArchUsuarios(ARCHIVO_USUARIOS)
            elif j==2: #Cargar nuevo archivo usuarios, borra el anterior
                menuUsuarios.cargarArchUsuarios(ARCHIVO_USUARIOS)
            elif j==3: #Crear novUsuarios para luego aparearlo con Usuarios.csv
                menuUsuarios.novedadesUsuarios('novUsuarios.csv')
                menuUsuarios.apareoNovedades(ARCHIVO_USUARIOS,'novUsuarios.csv')
            elif j==4: #Crea usuarios Aleatorios, borra el anterior
                menuUsuarios.usuariosAleatorios(ARCHIVO_USUARIOS)
            elif j==5: #Imprime todos los usuarios ordenados por nombre
                menuUsuarios.visualizar(ARCHIVO_USUARIOS)
            else: #Accion invalida
                print ('Por favor ingresar un numero valido')
            os.system('cls')
    elif i==0:
        print 'algo'
        #Como no hace nada sale del programa
    else: #Accion invalida
        print ('Por favor ingresar un numero valido')
    os.system('cls')
