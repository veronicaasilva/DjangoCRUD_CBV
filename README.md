# READ.ME

### Gestão de Clientes

O Gestão de Clientes é uma aplicação que busca facilitar o controle dos dados pessoais e de contatos dos clientes.

Este projeto faz parte do meu portfólio pessoal e foi criado com o objetivo de estudar os recursos de Class Based View do framework Django.

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
- Bootstrap4
- Heroku

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