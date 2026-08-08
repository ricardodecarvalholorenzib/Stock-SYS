# 📦 Sistema de Gerenciamento de Estoque

> Sistema de gerenciamento de estoque desenvolvido em Python e executado diretamente via terminal.

O projeto permite cadastrar e gerenciar produtos, controlar funcionários, administrar o saldo de caixa do sistema e configurar o perfil do operador com autenticação segura.

---

## ✨ Funcionalidades

### 📦 Estoque
* **Cadastro:** Cadastrar novos produtos com ID único.
* **Visualização:** Consultar o estoque atual e identificar produtos com estoque baixo.
* **Edição:** Alterar nome, quantidade, preço e peso dos produtos.
* **Remoção:** Remover unidades específicas ou excluir produtos do estoque.

### 👥 Funcionários
* **Gestão:** Adicionar, visualizar, editar (nome, salário, cargo, data de nascimento) e remover funcionários.
* **Destaque:** Definir e visualizar o *Funcionário do Mês*.

### 💰 Controle de Caixa
* Adicionar e subtrair valores do saldo.
* Consultar saldo atual em tempo real.
* Adicionar automaticamente ao caixa o valor de produtos removidos/vendidos.

### 🔐 Sistema de Autenticação
* Proteção por senha ao iniciar o sistema.
* Criptografia e armazenamento seguro utilizand **SHA-256**.
* Opção para alterar a senha cadastrada.

### ⚙️ Configurações
* Alterar nome do operador e senha.
* Reiniciar o sistema.
* Excluir todos os dados salvos (Reset).

### 🖥️ Interface no Terminal
* Menu interativo navegável pelas **setas do teclado**.
* Interface estilizada e colorida no terminal.
* Mensagens de confirmação, alertas e exibição de data e horário.

---

## 💾 Armazenamento de Dados

Os dados são armazenados localmente em um arquivo `estoque.json`, garantindo persistência automática após alterações importantes.

O arquivo armazena:
* Nome do operador
* Produtos cadastrados
* Lista de funcionários
* Saldo em caixa
* Dados de autenticação (hash da senha)

---

## 🛠️ Tecnologias Utilizadas

* **[Python 3](https://www.python.org/)** — Linguagem principal
* **`json`** — Persistência de dados
* **`colorama`** — Estilização de cores no terminal
* **`hashlib`** — Criptografia de senhas (SHA-256)
* **`msvcrt`** — Captura de teclas para navegação no menu
* **`datetime`**, **`os`**, **`random`** — Utilitários do sistema

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3** instalado em sua máquina.

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
2. Instalar as dependências
Bash
pip install colorama
3. Executar a aplicação
Bash
python main.py
Observação: Atualmente, o projeto está concentrado em um único arquivo Python. Uma futura atualização irá modularizar o código em diferentes arquivos e pastas para melhorar a organização e manutenção.

📌 Versão Atual: v1.5
Principais novidades da versão:

🎨 Nova interface colorida e menu interativo.

🔒 Sistema de senha com hash SHA-256.

👥 Módulo completo de gerenciamento de funcionários.

⚙️ Novas opções no menu de Configurações e Sair.

🚧 Próximos Passos (Roadmap)
[ ] Separar o código em módulos e pastas (Refatoração).

[ ] Melhorar a validação de entradas do usuário.

[ ] Tratar exceções adicionais e corrigir bugs conhecidos.

[ ] Refatorar funções extensas para código limpo (Clean Code).

[ ] Adicionar novas funcionalidades de relatórios em PDF/CSV.

📚 Objetivo do Projeto
Este projeto foi desenvolvido com o propósito de praticar e aprimorar conceitos fundamentais e intermediários em Python, tais como:

Estruturas de dados (Listas e Dicionários)

Manipulação de arquivos (JSON)

Hashing e Segurança básica (hashlib)

Tratamento de erros e exceções

Construção de menus interativos no terminal

📌 Status do Projeto
🟡 Em desenvolvimento O sistema possui diversas funcionalidades prontas, mas continua recebendo melhorias e refatorações constantes.
