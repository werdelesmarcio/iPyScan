#!/usr/bin/python3
# -*- coding: utf-8 -*-

# PyTCPScan Version 3.0 (beta)
from datetime import datetime
import os
import time
from colorama import init, Fore, Back, Style # Usando o colorama para inserir cor ao texto do terminal
init()

def banner():
    time.sleep(2) # Aguardar dois segundos para iniciar a aplicação
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
    data = datetime.now()
    
    print(Fore.RED + 
          """
 Welcome to iPyScan v. 1.0.28. Date: """ + data.strftime('%d/%m/%Y') + """   
 Developed by: Werdeles Soares (gh05tb0y). E-Mail: gh05tb0y@disroot.org                          
          """
        + Fore.RESET)



