#!/usr/bin/python3
# -*- coding: utf-8 -*-

# PyTCPScan Version 3.0 (beta)
import os
import time
from colorama import init, Fore, Back, Style # Usando o colorama para inserir cor ao texto do terminal
init()

def banner():
    time.sleep(2) # Aguardar dois segundos para iniciar a aplicação
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
    print(Fore.RED + 
          """
                          Welcome to iPyScan Ver.: 1.3    
                          By: Werdeles Soares (gh05tb0y)    
                          E-Mail: gh05tb0y@disroot.org
          """
        + Fore.RESET + 
                                                   
        """ )



