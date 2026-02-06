import despesas
from fastapi import FastAPI
from schemas import DespesaIn


app = FastAPI()


@app.get('/despesas')
def listar_despesas():
    return despesas.listar()

@app.post('/despesas')
def cadastrar_despesa(body: DespesaIn):
    despesas.cadastrar(body) 
    return {'message': 'Despesa cadastrada com sucesso.'}
