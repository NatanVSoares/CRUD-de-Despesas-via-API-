
# Projeto!

CRUD de Despesas (via API)

Vamos Executar tudo que Aprendemos no Módulo de Python!

Iremos implementar o Backend de uma Aplicação de Gerenciamento Financeiro utilizando Flask e MySQL.

## Banco de Dados (Primeira Tabela)

1. Crie um banco de dados chamado "gerenciador_financeiro" no MySQL utilizando o "CREATE DATABASE" 

2. Crie uma tabela chamada "despesas" utilizando o "CREATE TABLE" que deve armazenar:

- nome: Nome da despesa
- valor: Valor da despesa
- descricao: Descrição da despesa (Outras informações)
- data_pagamento: Data de pagamento da despesa.
- data_criacao: Data e Hora da criação, deve ter valor padrão a data de agora.


## Setup do Projeto

3. Crie uma Pastinha para o Projeto, e abra com o VSCode

4. No terminal, crie o ambiente virtual com o comando "python -m venv .venv"

5. Ative o ambiente virtual com o comando ".venv\Scripts\activate"


## Conectando com o Python

6. Com o ambiente virtual ativado, instale a biblioteca para interagir com o MySQL

```powershell
pip install mysql-connector-python
```

7. Crie um arquivo "db.py" onde você deve implementar uma função chamada "get_db" que deve connectar com o MySQL através da função "mysql.connect()" do "import mysql.connector as mysql" e retornar a conexão

```python
import mysql.connector as mysql

def get_db():
    ... # Código para connectar com o MySQL e retornar a conexão
```

8. Crie um modulo "despesas" no python.

9. Implemente uma função chamada "listar" no modulo "despesas" que deve utilizar o comando "SELECT" para buscar as despesas do banco de dados.

- Utilize a função "get_db" para buscar a conexão.
- Crie um "cursor" com "conn.cursor()"
- Defina o comando SQL
- Execute o comando SQL
- Utilize a função "cursor.fetchall" para buscar os dados.

10. Implemente uma função chamada "cadastrar" no modulo de despesas, essa função deve receber "nome", "valor", "descricao" e "data_pagamento", e dentro dela você deve utilizar o comando "INSERT" para criar um novo registro no banco de dados.

- Utilize a função "get_db" para buscar a conexão.
- Crie um "cursor" com "conn.cursor()"
- Defina o comando SQL, e utilize o "%s" para informar onde os parâmetros serão informados
- Execute o comando SQL, passando os parâmetros da função.+

# CRUD-de-Despesas-via-API-
 659cc19b914a74b25a626398b0f719259aea26a9
