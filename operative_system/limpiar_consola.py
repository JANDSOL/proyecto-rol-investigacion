from .sistema_operativo import SystemOp
from os import system


def clean_screen():
    if SystemOp().__str__() == 'Windows':
        system('cls')
    else:
        system('clear')  # Linux or Mac.
