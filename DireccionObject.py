import Constante

class VectorDireccion(object):

    #constructor. Defino las direciones donde se va a poder comer.
    def __init__(self):
        self.vectorDireccion = [{'direccionX': 0, 'direccionY':0, 'direccionValida':False, 'fichasADarVuelta':0} for e in range(Constante.CANTIDAD_DIRECCIONES)]

        self.vectorDireccion[0]['direccionX'] = 0  # derecha
        self.vectorDireccion[0]['direccionY'] = 1
        self.vectorDireccion[1]['direccionX'] = 0  # izquierda
        self.vectorDireccion[1]['direccionY'] = -1
        self.vectorDireccion[2]['direccionX'] = 1  # arriba
        self.vectorDireccion[2]['direccionY'] = 0
        self.vectorDireccion[3]['direccionX'] = -1  # abajo
        self.vectorDireccion[3]['direccionY'] = 0
        self.vectorDireccion[4]['direccionX'] = 1  # diagonal superior derecha
        self.vectorDireccion[4]['direccionY'] = 1
        self.vectorDireccion[5]['direccionX'] = -1  # diagonal inferior derecha
        self.vectorDireccion[5]['direccionY'] = 1
        self.vectorDireccion[6]['direccionX'] = 1  # diagonal superior izquierda
        self.vectorDireccion[6]['direccionY'] = -1
        self.vectorDireccion[7]['direccionX'] = -1  # diagonal inferior izquierda
        self.vectorDireccion[7]['direccionY'] = -1

    # este reinicia el vector direccion para que sea reutilizable
    def reiniciarVectorDireccion(self):
        for i in range(Constante.CANTIDAD_DIRECCIONES):
            self.vectorDireccion[i]['direccionValida'] = False
            self.vectorDireccion[i]['fichasADarVuelta'] = 0

    def setDireccionValida(self, posicion, valor):
        self.vectorDireccion[posicion]['direccionValida'] = valor

    def setFichasADarVuelta(self, posicion, valor):
        self.vectorDireccion[posicion]['fichasADarVuelta'] = valor

    def getOrientacion(self, posicion, horientacion):
        return self.vectorDireccion[posicion][horientacion]

    def getDireccionValida(self, posicion):
        return self.vectorDireccion[posicion]['direccionValida']

    def getFichasADarVuelta(self, posicion):
        return self.vectorDireccion[posicion]['fichasADarVuelta']