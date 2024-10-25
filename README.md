![Logo](images/iPyScan.png)

[![codecov](https://codecov.io/github/werdelesmarcio/iPyScan/graph/badge.svg?token=fPsZjCY1Ji)](https://codecov.io/github/werdelesmarcio/iPyScan) [![Maintainability](https://api.codeclimate.com/v1/badges/925e54560e6c95a08675/maintainability)](https://codeclimate.com/github/werdelesmarcio/iPyScan/maintainability) [![Build status](https://ci.appveyor.com/api/projects/status/6136rh47g98a8cje?svg=true)](https://ci.appveyor.com/project/werdelesmarcio/ipyscan) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_iPyScan&metric=bugs)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_iPyScan) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_iPyScan&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_iPyScan) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_iPyScan&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_iPyScan) ![GitHub License](https://img.shields.io/github/license/werdelesmarcio/PyTCPScan3) ![GitHub commits since latest release](https://img.shields.io/github/commits-since/werdelesmarcio/iPyScan/latest) 
# iPyScan (Version 1.0.26)

Trata-se de uma aplicação voltada principalmente para sistemas **GNU/Linux** _(embora o interpretador Python 3 no Windows também execute a aplicação normalmente)_, com o objetivo de realizar a varredura de portas. A aplicação verifica quais portas estão abertas em um intervalo de portas fornecido por argumentos, retornando **OPEN** em caso positivo.

Os argumentos fornecidos consistem no endereço do host ou IP do alvo a ser analisado, seguido do intervalo de portas inicial e final.

**OBS.: Se o objetivo for escanear apenas uma porta, basta fornecer o mesmo valor para os dois últimos parâmetros.**

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

O sistema está na versão 1.0.2 _(beta)_ e ainda encontra-se em fase de desenvolvimento.

## Funcionalidades
Estas são as instruções para obter uma cópia do iPyScan em sua máquina para fins de desenvolvimento ou uso:

1. Faça o download ou clone o repositório em sua máquina e descompacte-o no local de sua preferência.
- Não é necessário instalar o iPyScan.
- Se for utilizá-lo como executável, lembre-se de conceder permissão de execução (caso esteja usando uma distribuição GNU/Linux).
- O sistema foi ajustado para garantir funcionalidade multiplataforma.

2. Para executar o projeto, atente-se às seguintes dependências:
- Ter o interpretador Python, versão 3.xx, e o pip3 instalados em sua máquina.
- Instalar as dependências listadas no arquivo requirements.txt.
- Se estiver utilizando uma distribuição Linux, recomenda-se realizar o update e o upgrade do sistema antes de rodar o projeto.

## Permissões (usuários GNU/Linux)

_Para dar permissão de execução._

```bash
  #: > sudo chmod +x ipyscan.py
```

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/werdelesmarcio/iPyScan.git
```

Entre no diretório do projeto

```bash
  cd iPyScan
```

Instale as dependências

```bash
  pip3 install requirements.txt
```

Inicie a aplicação. _Para executar a aplicação deve passar o argumento com o host do alvo, a porta inicial e a porta final. Ele irá verificar quais portas estão com o Status Open._

**Linux**
```bash
  $: > ./ipyscan [target] [init_port] [final_port]
```

**Windows**
```powershell
  $: > python3 ipyscan.py [target] [init_port] [final_port]
```

## Screenshot
![Example](images/Screenshot.png)


## Melhorias

1. Modularização por responsabilidade: Cada módulo contém funções que desempenham tarefas específicas:
  - banner.py: Apenas exibe o banner.
  - input_validation.py: Valida os argumentos de entrada.
  - network_utils.py: Funções relacionadas a redes (conexão e resolução de nomes).
  - port_scanner.py: Função que executa o loop de escaneamento.

2. Facilidade de manutenção: Agora o código está dividido em partes menores e mais fáceis de gerenciar. Se houver alguma mudança na lógica de rede, por exemplo, ela ficará confinada ao arquivo network_utils.py.

3. Reuso de código: Caso queira usar o código de conexão em outro projeto, basta importar o módulo adequado (network_utils) sem precisar alterar o código principal.

4. Legibilidade: Com funções bem definidas e módulos organizados, o código se torna mais legível e fácil de entender para outras pessoas que venham trabalhar nele.

Agora, cada arquivo é responsável por uma parte do código, o que melhora bastante a organização do projeto!

## Licença
Este projeto está sob Licença GPL-3.0. Para mais informações, consulte a documentação de licença no link abaixo.
* [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)

## Como contribuir para o projeto

1. Faça um fork do projeto.
2. Crie uma nova branch com as suas alterações ```git checkout -b my-feature ```.
3. Salve as alterações e crie uam mensagem de commit contado quais alterações foram executadas: ```git commit -m "Feature: My features.```.
4. Envie as alterações: ```git push origin my-feature```.

## Contribuidores
Um salve para todos os que contribuem com o projeto.


### Contatos
Se quiser entrar em contato, crie um **issue** no GitHub ou envie um e-mail para gh05tb0y@disroot.org. Obrigado!

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]([https://www.linkedin.com/](https://www.linkedin.com/in/werdeles-soares/))
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/iPyScan?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/iPyScan?style=for-the-badge">


<img src = "https://static.wikia.nocookie.net/lpunb/images/b/b1/Logo_Python.png/revision/latest?cb=20130301171443)?raw=true" width =120 align="Right">
