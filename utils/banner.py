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
           _  _____          _____                    
          (_)|  __ \        / ____|                   
           _ | |__) |_   _ | (___    ___  __ _  _ __  
          | ||  ___/| | | | \___ \  / __|/ _` || '_ \ 
          | || |    | |_| | ____) || (__| (_| || | | |
          |_||_|     \__, ||_____/  \___|\__,_||_| |_|
                      __/ |                           
                     |___/                            
        """
        + Fore.RESET + 
                
        """ 
                          Welcome to iPyScan Ver.: 1.3    
                          By: Werdeles Soares \033[31m(gh05tb0y)\033[0;0m    
                          E-Mail: gh05tb0y@disroot.org         
        """ )



