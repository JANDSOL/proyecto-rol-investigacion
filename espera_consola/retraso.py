from time import sleep
from operative_system.limpiar_consola import clean_screen


def espera_consola(segundos=2, limpiar_pantalla=True):
    print('')
    for num in reversed(range(1, segundos+1)):
        if num != 1: print("Espera", num, "segundos...")
        else: print("Espera", num, "segundo...")
        sleep(1)

    if limpiar_pantalla:
        clean_screen()
