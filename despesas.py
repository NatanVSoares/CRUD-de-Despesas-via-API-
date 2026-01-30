from db import get_db

def listar():
    conn = get_db()
    cursor = conn.cursor(dictionary=True) 
    
    sql = '''
        SELECT id," \
         " nome," \
         " valor, " \
         "descricao," \
         " data_pagamento," \
         " data_criacao FROM despesas'''
    cursor.execute(sql)
    
    resultados = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return resultados

def cadastrar(nome, valor, descricao, data_pagamento):
    conn = get_db()
    cursor = conn.cursor()
    
    sql = """
        INSERT INTO despesas (nome, valor, descricao, data_pagamento) 
        VALUES (%s, %s, %s, %s)
    """
    valores = (nome, valor, descricao, data_pagamento)
    
    cursor.execute(sql, valores)
    conn.commit() # Importante: Sem o commit, os dados não são salvos no MySQL!
    
    cursor.close()
    conn.close()
    print("Despesa cadastrada com sucesso!")