import Constante
from TableroObject import Tablero
from BotObject import Bot

#inicializacion
tablero = Tablero()
bot = Bot()

fichaJugador, fichaBot = tablero.elegirColorFicha()

juegoTerminado = False

#las negras juegan pimero
if fichaJugador == Constante.FICHA_BLANCA:
    bot.juega(tablero, fichaBot, fichaJugador)

while (not Tablero.juegoTerminado):
    tablero.reiniciarVectorDireccion()
    tablero.borrarPantalla()
    tablero.dibujar_tablero()

    if tablero.continuarJuego(fichaJugador, fichaBot):
        tablero.ingresarFicha(fichaJugador, fichaBot)
    else:
        print "El jugador no puede jugar en este turno"

    tablero.reiniciarVectorDireccion()

    tablero.dibujar_tablero()
    raw_input("Apriete enter para seguir")

    if tablero.continuarJuego(fichaBot, fichaJugador):
        bot.juega(tablero, fichaBot, fichaJugador)
    else:
        print "El bot no puede jugar este turno"

    raw_input("Apriete enter para seguir")#el bot ya dibuja el tablero

#aca va codigo despues de la partida