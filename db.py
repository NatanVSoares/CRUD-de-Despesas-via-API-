import mysql.connector as mysql

def get_db():
    
    conn = mysql.connect(
        host="localhost",
        user="root",
        password="in12345678",
        database="gerenciador_financeiro"
    )
    return conn 


get_db()