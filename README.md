# 📦 Stock-SYS

Sistema de gerenciamento de estoque desenvolvido em **Python** para execução no terminal.

O projeto foi criado para praticar estruturas de dados, persistência em JSON, tratamento de erros, menus interativos e organização de uma aplicação de linha de comando.

> 🟡 **Status:** em desenvolvimento — versão 1.5.

## ✨ Funcionalidades

- 📦 Cadastro, edição e remoção de produtos
- 🔎 Consulta do estoque e aviso de estoque baixo
- 👥 Cadastro e gerenciamento de funcionários
- 💰 Controle de caixa
- 🔐 Senha protegida por hash SHA-256
- ⚙️ Configurações do operador
- 💾 Salvamento automático em `estoque.json`
- ⌨️ Navegação pelo teclado usando as setas e `ENTER`
- 🎨 Interface colorida no terminal

## 🛠️ Tecnologias

- Python 3
- `colorama` — cores no terminal
- `json` — armazenamento dos dados
- `hashlib` — hash da senha
- `msvcrt` — leitura das teclas no Windows
- Bibliotecas padrão: `datetime`, `os`, `random`, `sys` e `time`

## ▶️ Como executar

### Pré-requisito

Tenha o **Python 3** instalado.

### Dependência externa

O projeto utiliza apenas uma biblioteca externa:

```bash
pip install colorama
```

### Executar

O arquivo principal atualmente se chama `Stock Sys.py`:

```bash
python "Stock Sys.py"
```

> ⚠️ O projeto utiliza `msvcrt`, portanto a navegação por teclado foi feita pensando principalmente em **Windows**.

## 💾 Dados locais

Na primeira execução, o programa cria e utiliza o arquivo `estoque.json` para guardar os dados do sistema.

Esse arquivo contém informações como produtos, funcionários, saldo e o hash da senha. **Não compartilhe um `estoque.json` real**, principalmente se ele contiver dados pessoais ou informações de uso do sistema.

## 📁 Estrutura atual

```text
Stock-SYS/
├── Stock Sys.py
├── README.md
└── .gitignore
```

O projeto ainda está concentrado em um único arquivo Python. Uma próxima etapa natural é separar as funcionalidades em módulos.

## 🚧 Próximos passos

- [ ] Separar o sistema em módulos
- [ ] Melhorar validações e tratamento de exceções
- [ ] Refatorar funções muito extensas
- [ ] Adicionar relatórios
- [ ] Melhorar testes e organização do projeto

## 📚 Objetivo

Projeto de estudo para praticar Python criando uma aplicação de terminal mais completa, em vez de apenas pequenos exercícios isolados.
