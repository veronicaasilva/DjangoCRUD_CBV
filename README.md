##GESTÃO CLIENTES
> O Gestão de Clientes é uma aplicação que busca facilitar o controle dos dados pessoais e de contatos dos clientes.

![](https://user-images.githubusercontent.com/63860290/86915880-19c5bb00-c0f9-11ea-8343-2cf71e53f35b.png)

O objetivo foi desenvolvedor uma aplicação simples para implementação de um CRUD explorando os recursos de Class Based View do framework Django. 
    
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
