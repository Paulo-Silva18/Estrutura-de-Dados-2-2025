# pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Modelo de dados
class Evento(BaseModel):
    id: int
    nome: str
    palestrante: str

# Banco de dados na memória
banco_eventos: List[Evento] = []

@app.get("/eventos")
def listar_eventos():
    return banco_eventos

@app.post("/eventos")
def criar_evento(evento: Evento):
    banco_eventos.append(evento)
    return evento

@app.put("/eventos/{evento_id}")
def atualizar_evento(evento_id: int, evento: Evento):
    # 'enumerate' dá o índice (0, 1, 2...) e o objeto (event)
    for index, event in enumerate(banco_eventos):
        # CORREÇÃO: Usa-se ponto (.) para acessar atributos de objeto, não [""]
        if event.id == evento_id:
            banco_eventos[index] = evento
            return evento
    return {"erro": "Evento não encontrado"}

@app.delete("/eventos/{evento_id}")
def remover_evento(evento_id: int):
    for index, event in enumerate(banco_eventos):
        # CORREÇÃO: Usa-se ponto (.) aqui também
        if event.id == evento_id:
            banco_eventos.pop(index)
            return {"message": "Evento removido com sucesso"}
    return {"erro": "Evento não encontrado"}