
from typing import Optional
from datetime import date
from pydantic import BaseModel


class DespesaIn(BaseModel):
    nome: str
    valor: float
    descricao: Optional[str] = None
    data_pagamento: date


