DIMENSION = 9
FICHA_NEGRA = 'N'
FICHA_BLANCA = 'B'
ESPACIO_LIBRE = '_'
CANTIDAD_DIRECCIONES = 8

#esta funcion se llama una unica vez y recibe el tablero en blanco, donde los rellenariamos con las fichas iniciales del juego.
def inicializar_tablero(tablero):
    for i in range(DIMENSION+1):
        for n in range(DIMENSION+1):
            if(i==0 or i==DIMENSION):
                tablero[i][n] = chr(48 + n)
            elif(n==0 or n==DIMENSION):
                tablero[i][n] = chr(48 + i)
            else:
                tablero[i][n] = ESPACIO_LIBRE

    tablero[ int((DIMENSION-1)/2) ][ int((DIMENSION-1)/2) ] = FICHA_NEGRA
    tablero[ int((DIMENSION-1)/2) ][ int((1+DIMENSION)/2) ] = FICHA_BLANCA
    tablero[ int((1+DIMENSION)/2) ][ int((DIMENSION-1)/2) ] = FICHA_BLANCA
    tablero[ int((1+DIMENSION)/2) ][ int((1+DIMENSION)/2) ] = FICHA_NEGRA

    return tablero

#una vez inicializado el tablero, va a imprimirlo para que el usuario vea el estado actual.
def dibujar_tablero(tablero):
    for i in range(DIMENSION+1):
        for n in range(DIMENSION+1):
            print tablero[i][n], ' ',

        print
        print

#estando ya definido los campos 'fichasADarVuelta' y 'direccionValida' en la creacion de la lista, tengo que indicarle hacia donde se dirige la direccion
def inicializar_vector_direccion(vectorDireccion):
    vectorDireccion[0]['direccionX'] = 0#derecha
    vectorDireccion[0]['direccionY'] = 1
    vectorDireccion[1]['direccionX'] = 0#izquierda
    vectorDireccion[1]['direccionY'] = -1
    vectorDireccion[2]['direccionX'] = 1#arriba
    vectorDireccion[2]['direccionY'] = 0
    vectorDireccion[3]['direccionX'] = -1#abajo
    vectorDireccion[3]['direccionY'] = 0
    vectorDireccion[4]['direccionX'] = 1#diagonal superior derecha
    vectorDireccion[4]['direccionY'] = 1
    vectorDireccion[5]['direccionX'] = -1#diagonal inferior derecha
    vectorDireccion[5]['direccionY'] = 1
    vectorDireccion[6]['direccionX'] = 1#diagonal superior izquierda
    vectorDireccion[6]['direccionY'] = -1
    vectorDireccion[7]['direccionX'] = -1#diagonal inferior izquierda
    vectorDireccion[7]['direccionY'] = -1

    return vectorDireccion
    #esto deberia ser una tupla ya que no se modificaria nunca

#este reinicia el vector direccion para que sea reutilizable
def reiniciar_vector_direccion(vectorDireccion):
    for i in range(CANTIDAD_DIRECCIONES):
        vectorDireccion[i]['direccionValida'] = False
        vectorDireccion[i]['fichasADarVuelta'] = 0

    return vectorDireccion

#verifica en una unica direccion si es valida. Devuelve un true si lo es.
def verificar_direccion_valida(tablero, vectorDireccion, i, fichaAliada, fichaEnemiga, posX, posY):
    fichasComidas = 0

    if tablero[posX][posY] == ESPACIO_LIBRE and tablero[ posX + vectorDireccion[i]['direccionX'] ][ posY + vectorDireccion[i]['direccionY'] ] == fichaEnemiga:
        fichasComidas+=1
        posX += 2*vectorDireccion[i]['direccionX']
        posY += 2*vectorDireccion[i]['direccionY']

        while (tablero[posX][posY] == fichaAliada or tablero[posX][posY] == fichaEnemiga) and not vectorDireccion[i]['direccionValida'] :
            if tablero[posX][posY] == fichaEnemiga:
                fichasComidas+=1
                posX += vectorDireccion[i]['direccionX']
                posY += vectorDireccion[i]['direccionY']
            elif tablero[posX][posY] == fichaAliada:
                vectorDireccion[i]['direccionValida'] = True
                vectorDireccion[i]['fichasADarVuelta'] = fichasComidas

    return vectorDireccion

#llamara en todas las direcciones a verificar_direccion_valida para devolver una respuesta final si se puede jugar en el casillero
def verificar_casilla_valida(tablero, vectorDireccion, fichaAliada, fichaEnemiga, posX, posY):
    casillaValida = False

    for i in range(CANTIDAD_DIRECCIONES):
        vectorDireccion = verificar_direccion_valida(tablero, vectorDireccion, i, fichaAliada, fichaEnemiga, posX, posY)
        if(vectorDireccion[i]['direccionValida']):
            casillaValida = True

    return casillaValida, vectorDireccion

#verifica que ambos jugadores tengan la oportunidad de jugar, en caso contrario, saltea su turno
def se_puede_jugar(tablero, vectorDireccion, fichaAliada, fichaEnemiga):
    x=1
    y=1
    casillaValida = False

    while (x<DIMENSION and not casillaValida):
        y=1
        while (y<DIMENSION and not casillaValida):
            casillaValida, _ = verificar_casilla_valida(tablero, vectorDireccion, fichaAliada, fichaEnemiga, x, y)
            y+=1
        x+=1

    return casillaValida

#El encargado de invertir las fichas del opoenente pero en una unica direccion
def invertir_fila(tablero, vectorDireccion, i, fichaAliada, fichaEnemiga, posX, posY):
    posX += vectorDireccion[i]['direccionX']
    posY += vectorDireccion[i]['direccionY']

    while (tablero[posX][posY] == fichaEnemiga):
        tablero[posX][posY] = fichaAliada
        posX += vectorDireccion[i]['direccionX']
        posY += vectorDireccion[i]['direccionY']

    return tablero

#si o si siendo una casilla valida, dara vuelta toda ficha del oponente en la direccion valida.
def invertir_fichas(tablero, vectorDireccion, fichaAliada, fichaEnemiga, posX, posY):
    tablero[posX][posY] = fichaAliada

    for i in range (0, DIMENSION):
        if (vectorDireccion[i]['direccionValida']):
            tablero = invertir_fila(tablero, i, fichaAliada, fichaEnemiga, posX, posY)

    return tablero

#la funcion que le permite ingresar al usuario la ficha. Se la pedira hasta que ingrese una casilla valida.
def ingresar_ficha(tablero, vectorDireccion, fichaAliada, fichaEnemiga ):
    casillero = raw_input('Ingrese dos valoes de 1 a 8 representando las posiciones X e Y: ')
    posX = int(casillero[0])
    posY = int(casillero[1])
    casillaValida, vectorDireccion = verificar_casilla_valida(tablero, vectorDireccion, fichaAliada, fichaEnemiga, posX, posY)

    while ( posX<1 or posX>=DIMENSION or posY<1 or posY>=DIMENSION or not casillaValida):
        casillero = raw_input('Posicion no valida, intentelo nuevamente: ')
        posX = int(casillero[0])
        posY = int(casillero[1])
        casillaValida, vectorDireccion = verificar_casilla_valida(tablero, vectorDireccion, fichaAliada, fichaEnemiga, posX, posY)

    return casillaValida, vectorDireccion

#relleno la lista del bot diciendole donde puede comer y cuantas.
def cargar_jugada_bot(tablero, vectorDireccion, jugadaBot, fichaAliada, fichaEnemiga):
    for x in range (1, DIMENSION):
        for y in range (1, DIMENSION):
            casillaValida, vectorDireccion = verificar_casilla_valida(tablero, vectorDireccion, fichaAliada, fichaEnemiga, x, y)
            if(casillaValida):
                jugadaBot[x][y]['posicionX'] = x
                jugadaBot[x][y]['posicionY'] = y
                for k in range (CANTIDAD_DIRECCIONES):
                    jugadaBot[x][y]['fichas'] += vectorDireccion[k]['fichasADarVuelta']

    return jugadaBot