# 🔢 Validador de CPF em Python

Um validador de CPF robusto e completo, com suporte opcional a banco de dados MongoDB.

---

## Sobre o Projeto

Este projeto consiste em um script Python que valida CPFs brasileiros seguindo todas as regras oficiais (incluindo os dígitos verificadores) e, opcionalmente, salva os dados válidos em um banco de dados MongoDB.

Perfeito para praticar **validação de dados**, **expressões regulares** e **integração com banco de dados**.

---

## Funcionalidades

- Validação completa de CPF (com ou sem pontuação: `.` e `-`)
- Remove automaticamente caracteres não numéricos
- Rejeita CPFs com todos os dígitos iguais (ex: 111.111.111-11)
- Cálculo correto dos dois dígitos verificadores
- Suporte opcional ao MongoDB para salvar CPF + Nome de usuário
- Tratamento de erros e mensagens amigáveis

---

## Tecnologias Utilizadas

- **Python 3**
- `re` (Expressões Regulares)
- `pymongo` (opcional - para integração com MongoDB)

---

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
