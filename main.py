from fastapi import FastAPI

app = FastAPI()

usuarios = {
    1: {"nome": "João", "idade": 30},
    2: {"nome": "Maria", "idade": 25},
    3: {"nome": "Pedro", "idade": 40},
    4: {"nome": "Dougla", "idade": 19}
}

@app.get("/")
def homepage():
    return {"Total de usuários": len(usuarios)}

@app.get("/usuarios/{id_usuario}")
def pegar_usuario(id_usuario: int):
    return usuarios[id_usuario]