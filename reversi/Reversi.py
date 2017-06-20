import Constante
from BotObject import Bot
from TableroObject import Tablero

#inicializacion
tablero = Tablero()
bot = Bot()

juegoTerminado = False

def jugar_reversi():
    fichaJugador, fichaBot = tablero.elegirColorFicha()

    #las negras juegan pimero
    if fichaJugador == Constante.FICHA_BLANCA:
        bot.juega(tablero, fichaBot, fichaJugador)

    posX = 0
    posY = 0

    while (not Tablero.juegoTerminado):
        #juega el usuario
        if tablero.continuarJuego(fichaJugador, fichaBot):
            tablero.reiniciar()
            if(posX != 0 and posY != 0) and (posX != None and posY != None):
                print "jugada del bot: " + str(posX) + "," + str(posY)

            tablero.ingresarFicha(fichaJugador, fichaBot)
        else:
            print "El jugador no puede jugar en este turno"

        #juega el bot
        if tablero.continuarJuego(fichaBot, fichaJugador):
            tablero.reiniciar()
            raw_input("Apriete enter para que el bot haga su jugada")
            posX, posY = bot.juega(tablero, fichaBot, fichaJugador)
        else:
            print "El bot no puede jugar este turno"


    return tablero.contarFichas(fichaJugador, fichaBot);
