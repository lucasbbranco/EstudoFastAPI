from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(id_usuario):
    token = f"bastasu63khaf09745{id_usuario}dbofia"
    return token
@auth_router.get("/")
async def get_auth():
    return {"message": "Api CORRETA."}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Usuário já existe com este email. Tente novamente com outro email.")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"message": "Usuário criado com sucesso."}

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == login_schema.email).first()


    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado.")

    if not bcrypt_context.verify(login_schema.senha, usuario.senha):
        raise HTTPException(status_code=400, detail="Senha incorreta.")

    else:
        access_token = criar_token(usuario.id)
        return {"access_token": access_token,
                "token_type": "Bearer"}