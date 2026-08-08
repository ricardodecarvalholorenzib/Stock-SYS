📦 Sistema de Gerenciamento de Estoque

Sistema de gerenciamento de estoque desenvolvido em Python, executado diretamente pelo terminal.

O projeto permite cadastrar e gerenciar produtos, controlar funcionários, administrar o saldo do sistema e configurar o perfil do operador.

✨ Funcionalidades
📦 Estoque
Cadastrar novos produtos
Visualizar o estoque atual
Identificar produtos com estoque baixo
Editar produtos cadastrados
Alterar nome, quantidade, preço e peso
Remover unidades de um produto
Remover produtos do estoque
Identificar produtos através de IDs
👥 Funcionários
Adicionar funcionários
Visualizar funcionários cadastrados
Editar funcionários
Alterar nome, salário, cargo e data de nascimento
Remover funcionários
Definir o funcionário do mês
Visualizar o funcionário do mês
💰 Controle de Caixa
Adicionar valores ao saldo
Subtrair valores do saldo
Consultar o saldo atual
Adicionar o valor de produtos removidos ao caixa
🔐 Sistema de Senha
Criar uma senha para o perfil
Solicitar a senha ao iniciar o sistema
Alterar a senha
Armazenar a senha utilizando SHA-256
⚙️ Configurações
Alterar nome do operador
Alterar senha
Excluir todos os dados do sistema
Reiniciar o sistema
🖥️ Interface
Menu interativo
Navegação através das setas do teclado
Interface colorida no terminal
Mensagens de confirmação e alerta
Exibição de data e horário
💾 Armazenamento

Os dados do sistema são armazenados localmente em um arquivo JSON chamado estoque.json.

O arquivo armazena informações como:

Nome do operador
Produtos
Funcionários
Saldo
Dados de autenticação

O sistema salva os dados automaticamente após alterações importantes.

🛠️ Tecnologias
Python 3
JSON
Colorama
hashlib
msvcrt
datetime
os
random
🚀 Como executar
1. Instale o Python

Tenha o Python 3 instalado no computador.

2. Instale as dependências
pip install colorama
3. Execute o programa
python main.py

Observação: atualmente, o projeto está concentrado em um único arquivo Python. Uma futura atualização pretende separar o código em diferentes arquivos e pastas para melhorar sua organização e manutenção.

📌 Versão atual

v1.5

Principais atualizações
Nova interface
Menu interativo
Sistema de senha
Gerenciamento de funcionários
Novas opções em Configurações
Novas opções no menu Sair
🚧 Próximos passos
 Separar o código em módulos e pastas
 Organizar melhor a estrutura do projeto
 Corrigir bugs existentes
 Melhorar a validação de entradas
 Refatorar funções muito extensas
 Melhorar a interface
 Adicionar novas funcionalidades
📚 Objetivo

Este projeto foi desenvolvido como uma forma de praticar e aprimorar conhecimentos em Python.

Durante o desenvolvimento foram utilizados conceitos como:

Funções
Loops
Estruturas condicionais
Tratamento de exceções
Listas e dicionários
Manipulação de arquivos
JSON
Hashing
Entrada e saída de dados
Menus interativos
Persistência de dados
📌 Status

🟡 Em desenvolvimento

O sistema possui diversas funcionalidades implementadas, mas continua recebendo melhorias, correções e refatorações.

Desenvolvido por Ricardo de Carvalho
