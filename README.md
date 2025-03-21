﻿# Desafio Login - Fidelity Pesquisas Cadastrais

Este repositório contém a solução para o desafio técnico proposto pela Fidelity Pesquisas Cadastrais. A aplicação foi desenvolvida utilizando o framework Django e um banco de dados relacional (SQLite). O projeto consiste em uma tela de login, uma tela de registro e uma tela de menu, seguindo os requisitos especificados.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado os seguintes itens:

- [Python](https://www.python.org/) (versão 3.8 ou superior)
- [Django](https://www.djangoproject.com/) (instalado via pip)
- [Git](https://git-scm.com/) (opcional, para clonar o repositório)

## Como Configurar o Projeto

### Clone o repositório (se ainda não o fez):


```
git clone https://github.com/pnascimentodev/desafio-login.git
cd desafio-login
```

### Crie um ambiente virtual (recomendado):

```
python -m venv venv
```

```
source venv/bin/activate
```  
# No Windows use: 

```
venv\Scripts\activate
```

### Instale as dependências:

```
pip install -r requirements.txt
```

### Execute as migrações do banco de dados:

```
python manage.py migrate
```

### Como Executar a Aplicação
### Inicie o servidor:

```
python manage.py runserver
```

O servidor estará disponível em http://127.0.0.1:8000/.


## Acesse a aplicação:
 Login: Acesse http://127.0.0.1:8000/login/ para fazer login.

 Registro: Acesse http://127.0.0.1:8000/registrar/ para criar uma nova conta.

 Menu: Após o login, o usuário será redirecionado para http://127.0.0.1:8000/menu/.
