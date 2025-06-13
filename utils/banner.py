#!/usr/bin/python3
# -*- coding: utf-8 -*-

# iPyscan Version 1.0.29 (beta)

from datetime import datetime
import time

from colorama import (
    init,
    Fore,
)  # Usando o colorama para inserir cor ao texto do terminal

init()


def clean_screen():
    print("\033c", end="") # Limpa a tela do terminal
    time.sleep(1)
    

def banner():
    time.sleep(2)  # Aguardar dois segundos para iniciar a aplicação
    clean_screen()  # Limpa a tela
    data = datetime.now()

    print(
        Fore.GREEN
        + """
Welcome to iPyScan v. 1.0.28. Date: """
        + data.strftime("%d/%m/%Y")
        + """   
Developed by: gh05tb0y (Werdeles Soares). E-Mail: gh05tb0y@disroot.org                          
"""
        + Fore.RESET
    )
