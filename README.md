# 📚 API REST de Livros com Flask

Este projeto é uma API REST simples e didática desenvolvida com **Python** e **Flask**. Ela simula operações básicas de CRUD (Create, Read, Update, Delete) em um pequeno "banco de dados" em memória contendo informações sobre livros. Ideal para quem está aprendendo desenvolvimento backend com Flask.

---

## 🚀 Funcionalidades da API

A API oferece os seguintes endpoints para manipulação de livros:

| Método | Endpoint        | Descrição                              |
|--------|------------------|------------------------------------------|
| GET    | `/livros`        | Retorna todos os livros.                |
| POST   | `/livros`        | Adiciona um novo livro.                 |
| PUT    | `/livros/<id>`   | Atualiza um livro existente pelo ID.    |
| DELETE | `/livros/<id>`   | Remove um livro pelo ID.                |

---

## 📦 Estrutura do Projeto

```
BookShelf_API/
│
├── app.py          # Arquivo principal da API com Flask
├── README.md       # Documentação do projeto
└── LICENSE         # Licença MIT do projeto
```

---

## 🧰 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Flask](https://flask.palletsprojects.com/)

Instale o Flask com:

```bash
pip install flask
```

---

## ▶️ Como Executar o Projeto

Clone o repositório e execute o arquivo `app.py`:

```bash
git clone git@github.com:EddieNine/BookShelf-API.git
cd BookShelf_API
python app.py
```

A aplicação estará disponível em: `http://127.0.0.1:5000`

---

## 📡 Exemplos de Requisições

### 🔹 GET `/livros`

Retorna todos os livros disponíveis.

**Resposta de exemplo:**
```json
[
  {"id": 1, "titulo": "O Alquimista", "autor": "Paulo Coelho"},
  {"id": 2, "titulo": "1984", "autor": "George Orwell"}
]
```

### 🔹 POST `/livros`

Adiciona um novo livro.

**Requisição:**
```json
{
  "id": 3,
  "titulo": "A Revolução dos Bichos",
  "autor": "George Orwell"
}
```

**Resposta:**
```json
{
  "id": 3,
  "titulo": "A Revolução dos Bichos",
  "autor": "George Orwell"
}
```

### 🔹 PUT `/livros/1`

Atualiza o livro com `id = 1`.

**Requisição:**
```json
{
  "titulo": "O Alquimista - Edição Atualizada",
  "autor": "Paulo Coelho"
}
```

### 🔹 DELETE `/livros/2`

Remove o livro com `id = 2`.

---

## ❗ Tratamento de Erros

- Livro não encontrado:
```json
{
  "erro": "Livro não encontrado"
}
```

---

## 🧠 Conceitos Demonstrados

- Construção de API RESTful com Flask
- Métodos HTTP (GET, POST, PUT, DELETE)
- Manipulação de JSON
- Simulação de banco de dados em memória

---

## 📄 Licença

Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).

---

## ✍️ Autor

**Edcarlos Cruz**  
Desenvolvedor Python & Entusiasta de APIs  
[LinkedIn](https://www.linkedin.com/in/edcarloscruz/) | [GitHub](https://github.com/EddieNine)
