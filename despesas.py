import db
from schemas import DespesaIn


def listar():
    conn = db.get_db()
    
    sql = '''
        SELECT id, nome, valor, descricao, data_pagamento, data_criacao
        FROM despesas
    '''

    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(sql)
        dados = cursor.fetchall()

    conn.close()
    return dados


def cadastrar(despesa: DespesaIn):
    conn = db.get_db()

    sql = '''
        INSERT INTO despesas (nome, valor, descricao, data_pagamento)
        VALUES (%s, %s, %s, %s)
    '''

    with conn.cursor(dictionary=True) as cursor:
        args = (despesa.nome, despesa.valor, despesa.descricao, despesa.data_pagamento)
        cursor.execute(sql, args)

    conn.commit()
    conn.close()