![Logo](images/iPyScan.png)

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/werdelesmarcio/iPyScan/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/werdelesmarcio/iPyScan/tree/main) [![Maintainability](https://api.codeclimate.com/v1/badges/925e54560e6c95a08675/maintainability)](https://codeclimate.com/github/werdelesmarcio/iPyScan/maintainability) [![Build status](https://ci.appveyor.com/api/projects/status/6136rh47g98a8cje?svg=true)](https://ci.appveyor.com/project/werdelesmarcio/iPyScan) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_iPyScan&metric=bugs)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_iPyScan) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_iPyScan&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_iPyScan) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_iPyScan&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_iPyScan) ![GitHub License](https://img.shields.io/github/license/werdelesmarcio/iPyScan) ![GitHub commits since latest release](https://img.shields.io/github/commits-since/werdelesmarcio/iPyScan/latest) 

# iPyScan

**iPyScan** é um scanner de portas TCP moderno escrito em Python 3. Ele oferece suporte a varredura multithread, captura de banners de serviços, exportação em JSON/CSV e uma interface de linha de comando completa.

Trata-se de uma aplicação voltada principalmente para sistemas **GNU/Linux** _(embora o interpretador Python 3 no Windows também execute a aplicação normalmente)_, com o objetivo de realizar a varredura de portas. A aplicação verifica quais portas estão abertas em um intervalo de portas fornecido por argumentos, retornando **OPEN** em caso positivo.
Os argumentos fornecidos consistem no endereço do host ou IP do alvo a ser analisado, seguido do intervalo de portas inicial e final.
   
   > OBS.: Se o objetivo for escanear apenas uma porta, basta fornecer o mesmo valor para os dois últimos parâmetros.


## Estrutura do projeto:
```
PyScan/
├── ipyscan/                       # Pacote principal renomeado
│   ├── main.py                    # Permite rodar com python -m ipyscan
│   ├── scanner/
│   │   └── input_validation.py
│   │   └── network_utils.py
│   │   └── port_scanner.py
│   ├── utils/
│   │   └── banner.py
│   │   └── exporter.py
│   └── ipyscan.py                 # Renomeie como ipyscan/main.py
├── tests/
│   └── test_core.py
├── pyproject.toml                 # Configuração moderna
├── setup.cfg                      # Metadados do projeto
├── README.md
├── LICENSE                        # MIT ou GPL
```


![banner](https://img.shields.io/badge/python-3.7%2B-blue)
![status](https://img.shields.io/badge/status-stable-brightgreen)

---

## 🚀 Funcionalidades

- ✅ Escaneamento de portas TCP (com multithread)
- ✅ Captura de banner de serviços (HTTP, FTP, SSH, etc)
- ✅ Exportação em JSON ou CSV
- ✅ Interface via `argparse`
- ✅ Testes automatizados com `unittest`
- ✅ Pronto para instalação via `pip`

---

## 📦 Instalação local

```bash
git clone https://github.com/seu-usuario/ipyscan.git
cd ipyscan
pip install .
```

---

## ⚖️ Uso básico

```bash
ipyscan --target 127.0.0.1 --ports 20-80 --threads 100 --output json
```

### Argumentos
| Flag        | Descrição                          | Exemplo            |
|-------------|-----------------------------------|---------------------|
| `--target`  | IP ou hostname do alvo            | `127.0.0.1`         |
| `--ports`   | Faixa de portas (ex: `20-80`)     | `20-100`            |
| `--threads` | Número de threads (default: 100) | `--threads 200`     |
| `--output`  | Formato de exportação            | `json` ou `csv`     |

---

## 📅 Exemplo de Saída JSON
```json
[
  {
    "port": 22,
    "banner": "SSH-2.0-OpenSSH_8.4"
  },
  {
    "port": 80,
    "banner": "HTTP/1.1 200 OK"
  }
]
```

---

## 💡 Roadmap de melhorias
- [x] Banner grabbing com heurísticas por porta
- [x] Testes automatizados com `unittest`
- [x] Exportação JSON/CSV
- [ ] Scan UDP
- [ ] Modo silencioso `--quiet`
- [ ] Interface web (Flask ou GUI)

---

## 🌐 Licença
Este projeto está sob Licença GPL-3.0. Para mais informações, consulte a documentação de licença no link abaixo.
   - [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
---

## 🚀 Contribuição

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue antes.

---

> Desenvolvido por Werdeles Marcio - 2025


## Screenshot
![Example](images/Screenshot.png)


## Colaboradores
Um praise para os cúbicos que contribuíram neste projeto 👏
<div align=center>
<table border="0px">
  <tr>
    <td align="center"><a href="https://github.com/werdelesmarcio"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/36682515?v=4" width="100px;" alt=""/><br /><b>Werdeles Soares</b></a><br /><sub>💻 Desenvolvedor</sub></td>
    <td align="center"><a href="https://github.com/fabi-goncalves"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/186219541?v=4" width="100px;" alt=""/><br /><b>Fabi Gonçalves</b></a><br /><sub>👨‍💻 Colaboradora</sub></td>    
    <td align="center"><a href="https://github.com/matholiveira91"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/37408291?v=4" width="100px;" alt=""/><br /><b>Matheus Oliveira</b></a><br /><sub>👨‍💻 Colaborador</sub></td>
  </tr>
</table>
</div>

## Como contribuir para o projeto
Caso tenha alguma dúvida confira este [guia de como contribuir no GitHub](./CONTRIBUTING.md)

## Contatos
Se quiser entrar em contato, crie um **issue** no GitHub ou envie um e-mail para gh05tb0y@disroot.org. Obrigado!

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](<[https://www.linkedin.com/](https://www.linkedin.com/in/werdeles-soares/)>)
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/iPyScan?style=for-the-badge"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/iPyScan?style=for-the-badge">

<img src = "https://static.wikia.nocookie.net/lpunb/images/b/b1/Logo_Python.png)?raw=true" width =120 align="Right">
