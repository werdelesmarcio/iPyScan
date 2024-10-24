
![Logo](images/iPyScan.png)

[![Maintainability](https://api.codeclimate.com/v1/badges/bf596a2940ddf3183bab/maintainability)](https://codeclimate.com/github/werdelesmarcio/PyTCPScan3/maintainability) [![Build status](https://ci.appveyor.com/api/projects/status/050o62vq1v03wv4c?svg=true)](https://ci.appveyor.com/project/werdelesmarcio/pytcpscan3)  [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan3&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_PyTCPScan3)   [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan3&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_PyTCPScan3)   [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan3&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_PyTCPScan3)   ![GitHub License](https://img.shields.io/github/license/werdelesmarcio/PyTCPScan3)


# iPyScan (Version 1.3)
_Repositório para a aplicação iPyScan._

```
                   GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.
```

Consiste em uma aplicação voltada para principalmente para sistemas **GNU/Linux** _(embora o interpretador python3 no windows também execute a aplicação normalmente)_ e tem como finalidade, a execução de scanner de portas, onde irá verificar quais portas estão abertas dentro de um range de portas informados por argumentos e retornar **OPEN**, em caso positivo. 

Os argumentos informados consistem no endereço de host ou IP do alvo que será analisado, seguidos do range de portas inicial e final.

**OBS.: Se sua meta é de escanear apenas uma porta, pode colocar o mesmo valor para os dois ultimos parâmetros.**

## Estrutura do projeto:

```
iPyScan/
│
├── utils/
│   ├── __init__.py          # Torna utils um pacote Python
│   ├── banner.py            # Contém a função banner()
│
├── scanner/
│   ├── __init__.py          # Torna scanner um pacote Python
│   ├── input_validation.py  # Contém validação de argumentos
│   ├── network_utils.py     # Contém as funções de rede como `connect` e `resolve_target`
│   ├── port_scanner.py      # Contém a função de escaneamento `scan_ports`
│
├── main.py                  # Arquivo principal que faz a execução do código
└── README.md                # Descrição do projeto (opcional)
```

O sistema está na versão 1.3 _(beta)_ e ainda encontra-se em fase de desenvolvimento.

## Funcionalidades
Estas são as instruções para que você tenha uma cópia do **iPyScan** em sua máquina para fins de desenvolvimento e teste.
Execute o download ou clone o repositório para a sua máquina e descompacte-o em um local de preferência.

- _Não é necessário instalar o PyTCPScan._
- _Para usar como executável, lembrar de dar permissão de execução (caso esteja usando uma Distribuição GNU/Linux)._
- _Alterações no sistema para funcionalidade multiplataforma._

## Pré-Requisitos

Para rodar esse projeto, você vai precisar se atentar às dependências abaixo:

- Ter instalado em sua máquina o interpretador python na versão 3.xx e o pip3.
- Se estiver rodando uma distro linux, fazer o update e upgrade do sistema antes de rodar.


## Permissões (usuários GNU/Linux)

_Para dar permissão de execução._

```bash
#: > sudo chmod +x pytcpscan.py
```
    
## Execução

_Para executar a aplicação deve passar o argumento com o host do alvo, a porta inicial e a porta final. Ele irá verificar quais portas estão com o Status Open._

**GNU/Linux**
```bash
$: > ./pytcpscan [target] [init_port] [final_port]
```
**Windows**
```powershell
$: > python3 pytcpscan.py [target] [init_port] [final_port]
```

## Exemplo de Resposta
![Example](images/Capture01.png)

## Autores
**Werdeles (gh05tb0y) Soares:** _Desenvolvedor_

### Contatos
Se quiser entrar em contato, crie um **issue** no GitHub ou envie um e-mail para werdelesmarcio@gmail.com. Obrigado!
Usuário do github: [@werdelesmarcio](https://github.com/werdelesmarcio) 

## Licença
Este projeto está sob Licença GPL-3.0. Para mais informações, consulte a documentação de licença no link abaixo.
* [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)

## Detalhes das mudanças:

1- *Modularização por responsabilidade*: Cada módulo contém funções que desempenham tarefas específicas:
  * _banner.py_: Apenas exibe o banner.
  * _input_validation.py_: Valida os argumentos de entrada.
  * _network_utils.py_: Funções relacionadas a redes (conexão e resolução de nomes).
  * _port_scanner.py_: Função que executa o loop de escaneamento.

2- *Facilidade de manutenção*: Agora o código está dividido em partes menores e mais fáceis de gerenciar. Se houver alguma mudança na lógica de rede, por exemplo, ela ficará confinada ao arquivo _network_utils.py_.

3- *Reuso de código*: Caso queira usar o código de conexão em outro projeto, basta importar o módulo adequado (network_utils) sem precisar alterar o código principal.

4- *Legibilidade*: Com funções bem definidas e módulos organizados, o código se torna mais legível e fácil de entender para outras pessoas que venham trabalhar nele.

Agora, cada arquivo é responsável por uma parte do código, o que melhora bastante a organização do projeto!


<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/PyTCPScan3?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/PyTCPScan3?style=for-the-badge">


<img src = "https://github.com/werdelesmarcio/PyTCPScan2/blob/master/Images/SoftwareLivre.png?raw=true" width =120 align="Right">
<img src = "https://github.com/werdelesmarcio/PyTCPScan2/blob/master/Images/PoweredByLinux.png?raw=true" width =80 align="Right">
