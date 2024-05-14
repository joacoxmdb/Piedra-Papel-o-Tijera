import random

ti = "Tijera"
pa = "Papel"
pi = "Piedra"

def juego(): 
    usuario = input("Seleccione 'pi' para piedra, 'ti' para tijera, 'pa' para papel.\n").lower()
    computadora = random.choice([pi, pa, ti])
    
    if usuario == computadora:
        return '¡Empate!'

    ## Regla del juego
    if ganaste(usuario, computadora):
        return '¡Ganaste!'
    
    return '¡Perdiste! La computadora eligio: ' + computadora 
    
def ganaste(jugador, computadora):
    if ((jugador == 'pi' and computadora == ti) 
        or (jugador == 'pa' and computadora == pi) 
        or (jugador =='ti' and computadora == pa)):
        return True
    else: 
        return False
    



print(juego())