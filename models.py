from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

#cria a conexão com o banco de dados
db = create_engine("mysql+pymysql://root:123test@localhost:3306/projeto")

#cria a base do banco de dados
Base = declarative_base()

#criar as tabelas/classes do banco de dados
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column("nome", String(100), nullable=False)
    email = Column("email", String(100), unique=True, nullable=False)
    senha = Column("senha", String(100), nullable=False)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    status = Column("status", String(100), nullable=False)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Integer, nullable=False)

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.status = status
        self.usuario = usuario
        self.preco = preco

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String(100), nullable=False)
    tamanho = Column("tamanho", String(100), nullable=False)
    preco_unitario = Column("preco_unitario", Integer, nullable=False)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario,pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

#cria as tabelas no banco de dados