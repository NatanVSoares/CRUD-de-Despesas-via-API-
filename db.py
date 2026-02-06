import mysql.connector as mysql


def get_db():
    conn = mysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='in12345678',
        db='gerenciador_financeiro'
    )
    return conn


if __name__ == '__main__':
    get_db()
    print('Banco de Dados Conectado')