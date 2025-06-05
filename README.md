# FastAPI Learning Repository

Este repositório foi criado com o objetivo de organizar e documentar meu processo de aprendizado sobre o framework **FastAPI**. Aqui, armazenarei exemplos de código, anotações, projetos e qualquer outro recurso que me ajude a consolidar os conceitos e práticas relacionados ao desenvolvimento com FastAPI.

## Sobre o FastAPI

FastAPI é um framework moderno, rápido (de alta performance), voltado para a construção de APIs utilizando Python. Ele utiliza:

- **Tipagem estática** para validação e documentação automáticas.
- **Pydantic** para validação de dados.
- **Starlette** como base para roteamento e middleware.

Algumas vantagens do FastAPI:
- Fácil de aprender.
- Documentação automática com Swagger UI.
- Compatível com ASGI (para aplicativos modernos e escaláveis).

## Pré-requisitos

Antes de executar os exemplos ou projetos deste repositório, certifique-se de ter o seguinte:

- Python 3.10 ou superior.
- `pip` para gerenciar pacotes Python.
- Instale o FastAPI, Uvicorn e algumas outras dependências necessárias (essas foram as que **eu** utilizei):

```bash
pip install fastapi uvicorn sqlalchemy pydantic passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart
```

## Iniciando um Projeto FastAPI

Exemplo básico de uma aplicação FastAPI com o clássico "Hello, World!":

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

Execute o servidor com o comando:

```bash
uvicorn main:app --reload
```

Acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) para visualizar sua aplicação.

## Recursos Adicionais
Utilizei os seguintes recursos para aprender e aprofundar meus conhecimentos sobre o FastAPI:
- [Documentação Oficial do FastAPI](https://fastapi.tiangolo.com/)
- [Repositório FastAPI no GitHub](https://github.com/tiangolo/fastapi)

## Objetivos do Aprendizado (Marcação conforme concluído)

- [ ] Entender os conceitos básicos do FastAPI.
- [ ] Trabalhar com rotas, requisições e respostas.
- [ ] Aprender sobre validação de dados com Pydantic.
- [ ] Integrar o FastAPI com um banco de dados (SQLite e MySQL).
- [ ] Desenvolver uma API completa para gerenciamento de dados.

## Contribuição

Este é um repositório de aprendizado pessoal, mas sugestões, feedbacks ou melhorias são sempre bem-vindos! Sinta-se à vontade para abrir uma _issue_ ou _pull request_.

## Licença

Este repositório está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
