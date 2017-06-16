#Programa Principal, desde aqui haremos el menu
menu1=['1-Jugar','2-Ver Top 10','3-Cargar,generar o actualizar archivo Usuarios','0-Salir']
menu2=['1-Reset archivo Usuarios','2-Cargar nuevo arhivo Usuarios','3-Actualizar archivo Usuarios','4-Generar Usuarios aleatorio','0-Volver al Menu Principal']
i=1
while i!=0:
    for k in menu1:
            print k,'\n'
    j=1
    i=input('Por favor ingresar la accion a realizar acorde al numero correspondiente\n')
    if i==1:
                print 'algo' #Se inicia el juego
    elif i==2:
        #Se imprime el top 10 y vuelve
                #Aca va el programa de top 10
                while j!=0:
                        j=input('Presione 0 para volver al menu principal\n')
    elif i==3:
            #Va a menuUsuarios
        while j!=0:
            for k in menu2:
                print k,'\n'
            j=input('Por favor ingresar la accion a realizar acorde al numero correspondiente\n')
            if j==1:
                                print 'algo'
                                #Resetea Usuarios, se borra el anterior
            elif j==2:
                                print 'algo'
                                #Carga nuevo Usuarios, se borra el anterior
            elif j==3:
                                print 'algo'
                #Permite crear un nuevo novUsuarios y realiza el apareo
            elif j==4:
                                print 'algo'
                #Genera un Usuarios aleatorio, se borra el anterior
            elif j==0:
                                print 'algo'
                                #Vuelve al menu principal
            else: #Accion invalida
                                print ('Por favor ingresar un numero valido')
    elif i==0:
                print 'algo'
        #Como no hace nada sale del programa
    else: #Accion invalida
        print ('Por favor ingresar un numero valido')
