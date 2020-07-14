# GESTÃO DE CLIENTES

> O Gestão de Clientes é uma aplicação que busca facilitar o controle dos dados pessoais e de contatos de uma cartela de clientes.

![](https://user-images.githubusercontent.com/63860290/86917309-3fec5a80-c0fb-11ea-94af-05556b1f4cfe.png)

Este projeto faz parte do meu portfólio pessoal e foi criado com o objetivo de estudar os recursos de Class Based View do framework Django em uma implementação de um sistema simples de CRUD.

### SOBRE

Após efetuar o login, o usuário pode:

- Crie o cadastro de um cliente clicando em Novo Cliente
- Na tela inicial, fazer a busca por um cliente cadastrado através do seu nome;
- Também na tela inicial, ter acesso as informações do cliente cadastrado e possa:
    - visualizar o seu cadastro completo e:
        - enviar uma mensagem por whatsapp;
        - enviar uma mensagem por email.
    - atualizar o seu cadastro;
    - excluir o cadastro;
    - clonar o cadastro.

### TECNOLOGIAS

- Python
- Django
- SQlite
- Bootstrap4

### EXECUTANDO PROJETO LOCALMENTE:

Clone o repositório.

```python
git clone https://github.com/veronicaasilva/django-crud-cbv.git
cd django-crud-cbv
```

Crie um virtualenv com Python 

```python
python3 -m venv venv
. venv/bin/activate
```

Instale as dependências.

```python
pip install -r requirements.txt
```

Crie o banco de dados:

```python
python manage.py migrate
```

Execute o servidor de desenvolvimento:

```python
python manage.py runserver
```
