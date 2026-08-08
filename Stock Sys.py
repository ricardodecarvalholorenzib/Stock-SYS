# -----------------------------------------------------------------------------------------------------------------------
# Sistema de Gerenciamento de Estoque de Produto Diversos
# Desenvolvido por: Ricardo de Carvalho
# Atualizações: Nova UI, Menu Interativo, Senha, Funcionários, Novas Opções em 'Configurações' e Novas Opções em 'Sair'
# Versão: 1.5
# -----------------------------------------------------------------------------------------------------------------------

from datetime import datetime
from colorama import Fore, Back, Style, init
import msvcrt
import os
import json
import time
import sys
import random
import hashlib

init(autoreset=True)

def reiniciar_programa():
    os.execl(sys.executable, sys.executable, *sys.argv)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função auxiliar para evitar repetição de código ao salvar
def salvar_dados(operador, produtos, funcionarios, saldo, log):
    pacote_dados = {
        "operador": operador,

        "produtos": produtos,

        "funcionarios": funcionarios,

        "saldo": saldo,

        "log": log
    }
    with open('estoque.json', 'w', encoding='utf-8') as f:
        json.dump(pacote_dados, f, indent=4, ensure_ascii=False)

def menu_interativo(titulo, opcoes):
    selecionado = 0
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{titulo}\n")

        for i, opcao in enumerate(opcoes):
            if i == selecionado:
                print(f" ➤  {opcao}")
            else:
                print(f"   {opcao}")

        tecla = msvcrt.getch()

        if tecla in (b'\x00', b'\xe0'):
            tecla = msvcrt.getch()

        if tecla == b'H':    # Seta para Cima
            selecionado = (selecionado - 1) % len(opcoes)
        elif tecla == b'P':  # Seta para Baixo
            selecionado = (selecionado + 1) % len(opcoes)
        elif tecla == b'\r':  # ENTER
            return selecionado

def criptografar(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def time_clear():
    time.sleep(2)
    limpar_tela()

try:
    with open('estoque.json', 'r', encoding='utf-8') as f:
        dados_salvos = json.load(f)
        if isinstance(dados_salvos, dict):
            estoque = dados_salvos.get("produtos", [])
            nome_usuario = dados_salvos.get("operador", "")
            saldo = float(dados_salvos.get("saldo", 0))
            funcionarios = dados_salvos.get("funcionarios", [])
            senhas = dados_salvos.get("log", [])
        else:
            estoque = dados_salvos
            nome_usuario = ""
            funcionarios = []
            saldo = 0
            senhas = []

except (FileNotFoundError, json.JSONDecodeError):
    estoque = []

    funcionarios = []

    nome_usuario = ""

    saldo = 0

    senhas = []
# -----------------------------------------------

if not nome_usuario:
    
    nome_usuario = input("Olá! Bem-vindo ao sistema. Qual é o seu nome? ")
    
    time.sleep(1)
    
    senha_original = input("\nInsira a sua nova senha para desbloquear o aplicativo com segurança\n" +
                           Fore.CYAN + "============================== ou =================================\n" +
                           Fore.WHITE + "Deixe em Branco para não colocar nenhum tipo de senha!\n"
                           " ➤  ")

    if not senha_original:
        print(Fore.BLUE + "\n⚠️  Não iremos adicionar senha no seu perfil!")
        input("\nPressione ENTER para continuar...")
    
    else:
        senhas = criptografar(senha_original)

    time.sleep(1)
    
    salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
else:
    print(Back.GREEN + Fore.BLACK +  f"Bem-vindo de volta, {nome_usuario}!")
    
    time.sleep(2)
    
    if not senhas:
        print("\nEntrando no sistema...")
        time.sleep(2)
        limpar_tela()
    
    else:
        while True:
                conf_senha = input("\nInsira a sua senha atual para acessar o sistema --> ")

                if senhas == criptografar(conf_senha):
                    print(Fore.GREEN + "\n✅ Senha validada!")
                    input("\nPressione ENTER para entrar no sistema...")
                    break
                else:
                    print(Fore.RED + "\n❌ Erro! Senha inválida. Tente novamente")
                    time.sleep(1)
while True:
    hoje = datetime.today()
    agora = datetime.now()
    limpar_tela()
    opcao = menu_interativo(Fore.RED + f"    --- Gerenciador de Vendas | Operador: {nome_usuario} ---\n\n" + Fore.LIGHTRED_EX + f"                -  MENU PRINCIPAL  -\n\n                     {hoje.strftime('%d/%m/%Y')}\n                       {agora.strftime('%H:%M')}\n\n" + Fore.BLACK + "-" * 55, ["1 - Cadastrar Novo Produto", "2 - Informações de Estoque", "3 - Editar/Remover Produto", "4 - Configurações", "5 - Gerenciar Caixa", "6 - Funcionários", "7 - Sair do Sistema",])

    # -----------------------------------------
    # OPÇÃO 1: CADASTRAR NOVO PRODUTO
    # -----------------------------------------
    if opcao == 0:
            limpar_tela()              
            cad_prod = menu_interativo(Fore.RED + "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" +
                                    Fore.RED + "|                ---       " + Fore.LIGHTRED_EX + Style.BRIGHT + "CADASTRO DE PRODUTO" + Style.RESET_ALL + Fore.RED + "          ---               |\n" + 
                                    Fore.RED + "|_________________________________________________________________________|", ["1 - Adicionar Produto", "2 - Voltar"])
            limpar_tela()
            if cad_prod == 0:
                nome_prod = input("Nome do produto: ").strip().capitalize()
                
                if nome_prod:
                    while True:
                        try:
                            preco_input = input(f"\nPreço de {nome_prod} (ex: 5.50): ").replace(',', '.')
                            preco = float(preco_input) if preco_input else 0.0
                            break
                        except ValueError:
                            print(Fore.YELLOW + "\n⚠️  Erro! Insira somente números.")

                    
                    kg_or_g_y_n = menu_interativo("Gostaria de adicionar medidas de peso (quilograma, grama, litros ou ml) no seu produto?\n*dica: só use em alimentos como carnes, doces etc", ["SIM", "NÃO"])
                    k_or_g = ""
                    if kg_or_g_y_n == 0:
                        k_or_g = input("\nInsira a quantidade de peso (exemplo: 4 g, 4 l, 4 ml e 4 kg): ")
                    if kg_or_g_y_n == 1:
                        print(Fore.BLUE + "\n⚠️  Não iremos inserir o peso.")
                        time.sleep(1)

                    qtd_input = input(f"\nQuantidade em estoque de {nome_prod}: ")
                    try:
                        qtd = int(qtd_input) if qtd_input else 0
                    except ValueError:
                        print(Fore.RED + "❌ Número inválido!")
                        continue

                    novo_produto = {
                        "nome": nome_prod, 
                        "quantidade": qtd, 
                        "preco": preco,
                        "peso": k_or_g,
                        "id": random.randint(1000, 10000)
                    }
                    
                    estoque.append(novo_produto)
                    salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

                    print(Fore.GREEN + f"\n✅ Sucesso: {nome_prod} foi adicionado e salvo!")
                    time_clear()
                    ver_prod = menu_interativo("Selecione:", ["Ver informações do produto", "Voltar ao menu"])
                    if ver_prod == 0: time_clear(); print(Fore.RED + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n|            INFORMAÇÕES DO PRODUTO    |\n|____________________________________|\n\n" + Fore.BLACK + "-" * 120 + Fore.BLUE + "\n\n|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" + Fore.LIGHTBLUE_EX + f"       Produto: {nome_prod}  |  Qtd: {qtd_input:^5}  |  Preço: R${preco:.2f}  |  Peso: {k_or_g}\n" + Fore.BLUE + "|___________________________________________________________________________________________|\n"); Fore.BLACK + print("-" * 120); input("\nPressione ENTER para continuar...")
                else:
                    print(Fore.RED + "\n❌ Erro: O nome do produto não pode estar vazio.")
                    input("\nPressione ENTER para continuar...")
            
            elif cad_prod == 1:
                print("Saindo...")
                time.sleep(1)

    # -----------------------------------------
    # OPÇÃO 2: LISTAR ESTOQUE ATUAL
    # -----------------------------------------
    elif opcao == 1:

            time_clear()
            print(Fore.RED  +  "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" +
                  Fore.LIGHTRED_EX +  fr"""               \\\\ ESTOQUE ATUAL ( {len(estoque)} item(s) ) \\\\               """ +
                  Fore.RED  +  "\n|___________________________________________________________________|\n")

            if not estoque:
                print(Fore.YELLOW + "               ⚠️  O estoque está vazio no momento\n")
            else:
                
                for i, item in enumerate(estoque):
                    
                    estoque_baixo = item['quantidade'] <= 5
                    item_upper = item['nome'].upper()

                    print(Fore.BLACK + "-" * 100)

                    if estoque_baixo:    
                            print(Fore.YELLOW + f"⚠️  AVISO! ITEM '{item_upper}' (ID: {item['id']}) ESTÁ COM ESTOQUE BAIXO!")

                    print(Fore.BLUE + f"\n\n|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" +
                          Fore.LIGHTBLUE_EX + f"        ID: #{item['id']} |   Produto: {item['nome']}  |  Qtd: {item['quantidade']:^5}  |  Preço: R${item['preco']:.2f}  |  Peso: {item['peso']}\n" +
                          Fore.BLUE + f"|_____________________________________________________________________________________________________________|\n")  
            time.sleep(1.5)
            print(Fore.BLACK + "-" * 100)

            input("\nPressione ENTER para voltar ao menu...")
            limpar_tela()

    # -----------------------------------------
    # OPÇÃO 3: EDITAR OU REMOVER PRODUTO
    # -----------------------------------------
    elif opcao == 2:
            time_clear()
            print(Fore.RED + "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" +
                  Fore.RED + "|" + Fore.LIGHTRED_EX + "  ---   EDITAR OU REMOVER PRODUTOS PRODUTOS ---" + Fore.RED + "  |\n" +
                  Fore.RED + "|_________________________________________________|\n\n")
            
            if not estoque:
                input(Fore.YELLOW + "\n         ⚠️  Não há produtos no estoque!\n\n" + Fore.BLACK + "-" * 55 + Fore.WHITE + "\n\n       Pressione ENTER para voltar ao menu...")
                continue

            # Lista os produtos com seus ID's
            for item in estoque:
                print(Fore.BLACK + "-" * 100 +
                      Fore.BLUE + f"\n\n|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" +
                      Fore.LIGHTBLUE_EX + f"            ID: #{item['id']} |   Produto: {item['nome']}   |   Qtd: {item['quantidade']}   |   Preço: R${item['preco']:.2f}   |   Peso: {item['peso']}\n" +
                      Fore.BLUE + f"|_____________________________________________________________________________________________________________|\n")        

            indice_input = input(
                Fore.BLACK + "-" * 100 +
                Fore.WHITE + "\n\nDigite o ID do produto que deseja gerenciar "
                "(ou ENTER para cancelar): "
            )

            if not indice_input.isdigit():
                continue

            id_produto = int(indice_input)

            produto_alvo = None

            for item in estoque:
                if item['id'] == id_produto:
                    produto_alvo = item
                    break

            if produto_alvo:
                print("-" * 20)
                acao = menu_interativo(f"\nSelecionado: {produto_alvo['nome']}\nO que deseja fazer?", ["1 - Alterar Nome", "2 - Alterar Quantidade", "3 - Alterar Preço", "4 - Remover Produto", "5 - Alterar Peso", "6 - Sair"])                    
                print("-" * 20)

                if acao == 0:
                    time_clear()
                    novo_nome = input(Fore.RED + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n        Nome atual do seu produto: '{produto_alvo['nome']}'\n|________________________________________________________|\n\n" + Fore.WHITE + "Insira o novo nome do seu produto: ").strip().capitalize()
                    
                    if novo_nome:
                        produto_alvo['nome'] = novo_nome 
                        print(Fore.GREEN + f"\n✅ Nome atualizado para: '{produto_alvo['nome']}'!")
                        input("\nPressione ENTER para continuar...")

                        salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
                
                elif acao == 1:
                    time_clear()
                    nova_qtd = input(Fore.RED + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n      Quantidade atual do seu produto: {produto_alvo['quantidade']} unidades\n|________________________________________________________|" + Fore.WHITE + f"\n\nInsira a nova quantidade do produto '{produto_alvo['nome']}': ").strip()
                    
                    if nova_qtd.isdigit(): 
                        produto_alvo['quantidade'] = int(nova_qtd) 
                        print(Fore.GREEN + f"\n✅ Quantidade atualizada para: {produto_alvo['quantidade']} quantidades!")
                        input("\nPressione ENTER para continuar...")
                        salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
                        continue
                
                elif acao == 2:
                    time_clear() 
                    novo_preco = input(Fore.RED + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n        Preço atual: {produto_alvo['preco']:.2f}\n|________________________________________________________|" + Fore.WHITE + f"\n\nInsira o novo preço do seu produto '{produto_alvo['nome']}': ").replace(',', '.').strip() 
                    
                    try: 
                        produto_alvo['preco'] = float(novo_preco) 
                        print(Fore.GREEN + f"\n✅ Preço atualizado para: R${produto_alvo['preco']:.2f}!")
                        input("\nPressione ENTER para continuar...")
                        salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

                    except ValueError:
                        print(Fore.RED + "\n❌ Erro: Valor inválido.")

                elif acao == 3:
                    unit_or_int = menu_interativo(Fore.MAGENTA + "❓ Você gostaria de remover unidades do seu produto ou retirar ele do estoque completamente?", ["1 - Remover Unidades", "2 - Remover Item Geral"])
                    
                    if unit_or_int == 0:
                        while True:
                            try:
                                qtd_prod_ex = int(Fore.MAGENTA + input(f"\n❓ Quantas unidades você gostaria de remover de {produto_alvo['nome']}? (estoque atual: {produto_alvo['quantidade']}) "))
                                break
                            except ValueError:
                                print(Fore.YELLOW + "\n\n⚠️  Digite somente números!")

                        rs = produto_alvo['preco'] * qtd_prod_ex


                        confirmaçao_preco_imbutido = Fore.MAGENTA + menu_interativo(f"\n❓ Gostaria de adicionar o preço de R${rs:.2f} do produto {produto_alvo['nome']} a sua caixa? ", ["SIM", "NÃO"])

                        if confirmaçao_preco_imbutido == 0:
                            saldo += produto_alvo['preco'] * qtd_prod_ex


                        elif confirmaçao_preco_imbutido == 1:
                            print(Fore.GREEN + "\n✅ Não iremos imbutir o preço do produto a sua caixa.\n")
                        
                        confirmacao = Fore.MAGENTA + menu_interativo(f"\n❓ Tem certeza que deseja remover {qtd_prod_ex} unidades do seu produto {produto_alvo['nome']}?", ["SIM", "NÃO"])
                        
                        if confirmacao == "0":
                            if qtd_prod_ex > produto_alvo['quantidade']:
                                print(Fore.YELLOW + "\n⚠️  Quantidade inválida!")
                            
                            else:
                                produto_alvo['quantidade'] -= qtd_prod_ex
                                print(Fore.GREEN + f"\n🗑️  {qtd_prod_ex} unidade(s) removida(s) com sucesso!")
                                salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
                    
                    elif unit_or_int == 1:
                            estoque.remove(produto_alvo)
                            print(Fore.GREEN + f"\n🗑️  Produto {produto_alvo['nome']} removido do estoque com sucesso!")
                            salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

                elif acao == 4:
                    time_clear()
                    novo_peso = input(Fore.RED + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n        Peso atual: {produto_alvo['peso']}\n|________________________________________________________|" + Fore.WHITE + f"\n\nInsira o novo peso do seu produto '{produto_alvo['nome']}': ")
                    if novo_peso:
                        time.sleep(1)
                        produto_alvo['peso'] = novo_peso 
                        print(Fore.GREEN + f"\n✅ Peso atualizado para: {produto_alvo['peso']}!")
                        input("\nPressione ENTER para continuar...")
                        salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

                elif acao == 5:
                    print("\nSaindo...")
                    time.sleep(2)
                    continue
                        
                    
            else:
                print("")
                

    # -----------------------------------------
    # OPÇÃO 4: CONFIGURAÇÕES
    # -----------------------------------------
    elif opcao == 3:
            limpar_tela()
            edit_perfil = menu_interativo(Fore.RED + "             |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n             |" + Fore.LIGHTRED_EX + "  --- EDITAR PERFIL ---  " + Fore.RED + "|\n             |_________________________|" + Fore.WHITE + "\n\nEscolha uma opção para editar:", ["1 - Mudar Nome", "2 - Trocar Senha", "3 - Excluir Dados " + Fore.RED + "(IMPOSSÍVEL RECUPERAR!)", "4 - Voltar"])
            
            if edit_perfil == 0:
                time_clear()
                novo_nome = input("Digite o novo nome de operador (ou deixe em branco para cancelar): ").strip()
                
                if novo_nome:
                    nome_usuario = novo_nome
                    salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
                    print(Fore.GREEN + f"\n✅ Nome alterado para {nome_usuario} com sucesso!")
                
                input("\nPressione ENTER para voltar ao menu...")
            
            elif edit_perfil == 1:
                limpar_tela()
                
                while True:
                    inserir_ou_sair = menu_interativo("Escolha uma das opções:", ["Inserir senha atual para edita-lá (não se aplica se o usuário não tiver uma senha válida)", "Voltar"])

                    if inserir_ou_sair == 0:
                
                        if not senhas:
                            time.sleep(1)

                            nova_senha2 = input("\nDigite a sua nova senha (ou deixe em branco para cancelar): ").strip()

                            if not nova_senha2:
                                print(Fore.BLUE + "\n⚠️  Não será adicionado senha no seu perfil!")
                                input("\n\nPressione ENTER para continuar...")
                            
                            else:
                                senhas = criptografar(nova_senha2)
                                salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

                                print(Fore.GREEN + "\n✅ Senha alterada com sucesso")
                                time.sleep(3)
                                break

                        else:    
                            time_clear()
                            
                            senha_atual = input(Fore.CYAN +"❗ Digite a sua senha atual para troca-lá: ")
                            

                            if senhas == criptografar(senha_atual):
                                time.sleep(1)
                                print(Fore.GREEN + "\n✅ Senha correta!")
                                time.sleep(1)

                                nova_senha = input(Fore.CYAN + "\n❗  Digite a nova senha (ou deixe em branco para cancelar): ").strip()

                                if not nova_senha:
                                    print(Fore.YELLOW + "\n⚠️  Não será adicionado senha no seu perfil!")
                                    input("\n\nPressione ENTER para continuar...")
                                
                                else:
                                    senhas = criptografar(nova_senha)
                                    salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

                                    print(Fore.GREEN + "\n✅ Senha alterada com sucesso!")
                                    time.sleep(3)
                                    break
                            
                            else:
                                print(Fore.YELLOW + "\n⚠️  Senha incorreta!")
                                time.sleep(2)
                                continue
                                

                    elif inserir_ou_sair == 1:
                        print("\nSaindo...")
                        time.sleep(2)
                        break

            elif edit_perfil == 2:
                limpar_tela()

                confirmacao_limpar_dados = menu_interativo(Fore.RED + "!!! Tem certeza que quer resetar todo o sistema (TODOS OS DADOS SERÃO APAGADOS, NÃO SENDO POSSÍVEL RECUPERAR) !!!", {"SIM", "NÃO"})
                if confirmacao_limpar_dados == 1:
                    print("\nLimpando dados...")
                    time.sleep(5)
                    if os.path.exists('estoque.json'):
                        os.remove('estoque.json')
                    print("\nTodos os dados foram limpos!")
                    input("\n\nPressione ENTER para reiniciar o sistema...")
                    reiniciar_programa()


    # -----------------------------------------
    # OPÇÃO 5: LISTAR LUCROS
    # -----------------------------------------
    elif opcao == 4:
            reg_lucros = menu_interativo("Selecione:", ["Adicionar Lucro", "Subtrair Lucro", "Lucro Líquido", "Voltar"])
            if reg_lucros == 0:
                limpar_tela()
                while True:
                    try:
                        numero_vendas = Fore.MAGENTA + float(input("❓ Qual é o valor que você gostaria de adicionar na sua carteira?\n➤  ").replace(",", "."))
                        break
                    except ValueError:
                        print(Fore.YELLOW + "⚠️  Digite Somente números!")

                saldo += float(numero_vendas)

                time.sleep(1)
                print(f"Você adicionou R${numero_vendas:.2f} ao seu saldo.\n")
                time_clear()
                print(f"Saldo atual: R${saldo:.2f}")
                salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
                time.sleep(2)


            elif reg_lucros == 1:
                    if saldo <= 0:
                        print(Fore.YELLOW + "⚠️  Você não tem dinheiro para subtrair!")
                        time.sleep(2)
                    else:
                        print(Fore.MAGENTA + f"❓ Quanto você gostaria de subtrair do seu lucro? (Lucro Atual: R${saldo:.2f})")
                        
                        sub_preço = float(input("> ").replace(",", "."))
                        
                        if sub_preço > saldo:
                            print(Fore.YELLOW + "⚠️  Você não tem saldo suficiente!")
                        
                        else:
                            saldo -= float(sub_preço)
                        print(f"Novo saldo: R${saldo:.2f}")
                        salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
                        time.sleep(2)
            

            elif reg_lucros == 2:
                print(f"Saldo Atual: R${saldo:.2f}")
                time.sleep(3)

            elif reg_lucros == 3:
                print("Saindo...")
                time.sleep(2)

    # -----------------------------------------
    # OPÇÃO 6: FUNCIONÁRIOS
    # -----------------------------------------
    elif opcao == 5:
        print("\nCarregando...")
        time.sleep(2)
        opcao_funcionarios = menu_interativo("Escolha uma opção:", ["1 - Mostrar Ficha de Funcionários", "2 - Editar Funcionários", "3 - Funcionário do Mês", "4 - Adicionar Funcionários", "5 - Voltar"])
        if opcao_funcionarios == 0:
            time.sleep(0.5)
            if not funcionarios:
                time_clear()
                print(Fore.YELLOW + "⚠️  Você não tem funcionários registrados.\n")
                time.sleep(2)
                input("\nPressione ENTER para seguir...")
            else:
                limpar_tela()
                
                print(Fore.RED  +  "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" +
                    Fore.LIGHTRED_EX  +  fr"""                  \\\\ LISTA DE FUNCIONÁRIO(S) ATUAL ({len(funcionarios)} funcionário(s)) \\\\        """ +
                    Fore.RED  +  "\n|_________________________________________________________________________________________________|\n")
                
                print(Fore.BLACK + "-" * 100)

                for p, item in enumerate(funcionarios):
                    print(Fore.BLUE + f"\n|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n    [{p}] 🙍 Funcionário: {item['nome']}  |  Data de Nascimento: {item['idade']:^5}  |  Salário: R${item['salario']:.2f}  |  Cargo: {item['cargo']}\n|_________________________________________________________________________________________________________________________|\n")
                    print(Fore.BLACK + "-" * 100)

                input("\n\nPressione ENTER para voltar ao menu...")
                time_clear()

        elif opcao_funcionarios == 1:
            
            time.sleep(1)
            if not funcionarios:
                time_clear()
                print(Fore.YELLOW + "⚠️  Você não tem funcionários registrados!\n")
                time.sleep(2)
                input("Pressione ENTER para seguir...")
            
            else:
                limpar_tela()
                print(Fore.RED  +  "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" +
                    Fore.LIGHTRED_EX  +  fr"""                \\\\ LISTA DE FUNCIONÁRIO(S) ATUAL ({len(funcionarios)} funcionário(s)) \\\\        """ +
                    Fore.RED  +  "\n|_________________________________________________________________________________________________|\n")

                print(Fore.BLACK + "-" * 100)

                for p, item in enumerate(funcionarios):
                    print(Fore.BLUE + f"\n|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n    [{p}] 🙍 Funcionário: {item['nome']}  |  Data de Nascimento: {item['idade']:^5}  |  Salário: R${item['salario']:.2f}  |  Cargo: {item['cargo']}\n|_________________________________________________________________________________________________________________________|\n")
                    print(Fore.BLACK + "-" * 100)
                
                indice_input_fun = input("\nDigite o número do funcionário que deseja editar (ou ENTER para cancelar): ")
                
                if not indice_input_fun.isdigit():
                    continue
            
                indice2 = int(indice_input_fun)
                
                if 0 <= indice2 < len(funcionarios):
                    funcionario_alvo = funcionarios[indice2]                
                    acao_fun = menu_interativo(f"Selecionado: {funcionario_alvo['nome']}\n\nO que deseja fazer?", ["1 - Alterar Nome do Funcionário", "2 - Alterar Salário", "3 - Alterar Cargo", "4 - Alterar Data de Nascimento", "5 - Remover Funcionário", "6 - Voltar ao Menu"])
                    
                    if acao_fun == 0:
                        time_clear()
                        novo_nome_fun = input(Fore.RED + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n    Nome atual do seu funcionário(a): {funcionario_alvo['nome']}\n|____________________________________________________|\n" + Fore.WHITE + "\nSelecione o novo nome dele(a): ").strip().capitalize()
                        
                        if novo_nome_fun:
                            funcionario_alvo['nome'] = novo_nome_fun
                            time.sleep(0.5)
                            print(Fore.GREEN + f"\n✅ Nome atualizado para: '{funcionario_alvo['nome']}' com sucesso!")
                            salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
                            input("\nPressione ENTER para continuar...")

                        else:
                            print(Fore.RED + "❌ Erro: Valor inválido!\n")
                            time.sleep(1)
                            input("\nPressione ENTER para continuar...")

                    elif acao_fun == 1:
                        limpar_tela()
                        novo_salario_fun = input(Fore.BLUE + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n    Salário atual do seu funcionário(a): R${funcionario_alvo['salario']:.2f}\n|____________________________________________________|\n" + Fore.WHITE + "\nSelecione o novo salário dele(a): ").strip().capitalize().replace(',', '.')
                        
                        try:
                            funcionario_alvo['salario'] = float(novo_salario_fun)
                            print(Fore.GREEN + f"\n✅ Salário atualizado para: R${funcionario_alvo['salario']:.2f}!")
                            salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
                            input("\n\nPressione ENTER para continuar...")
                        
                        except ValueError:
                            print(Fore.RED + "❌ Erro: Valor inválido.\n")
                            time.sleep(1)
                            input("\n\nPressione ENTER para continuar...")

                    elif acao_fun == 2:
                        limpar_tela()
                        novo_cargo_fun = input(Fore.BLUE + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n    Cargo atual do seu funcionário(a): {funcionario_alvo['cargo']}\n|____________________________________________________|\n" + Fore.WHITE + "\nSelecione o novo cargo dele(a): ").strip().capitalize()
                        if novo_cargo_fun:
                            funcionario_alvo['cargo'] = novo_cargo_fun
                            time_clear()

                            print(Fore.WHITE + "\nCarregando...")
                            print(Fore.GREEN + f"\n✅ Cargo atualizado para: '{funcionario_alvo['cargo']}' com sucesso!")
                            input("\nPressione ENTER para continuar...")
                            salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

                        else:
                            print(Fore.RED + "❌ Erro: Valor inválido!\n")
                            time.sleep(1)
                            input("\nPressione ENTER para continuar...")


                    elif acao_fun == 3:
                        limpar_tela()
                        nova_data_nascimento_fun = input(Fore.BLUE + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n    Data de nascimento atual do seu funcionário(a): {funcionario_alvo['idade']}\n|____________________________________________________|n" + Fore.WHITE + "\nSelecione a nova data de nascimento dele(a): ").strip().capitalize()
                        if nova_data_nascimento_fun:
                            funcionario_alvo['idade'] = nova_data_nascimento_fun
                            time_clear()
                            print(Fore.WHITE + "Carregando...\n")
                            print(Fore.GREEN + f"✅ Data de nascimento atualizada para: {funcionario_alvo['idade']} com sucesso!")
                            time.sleep(1)
                            salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)
                            input("\nPressione ENTER para continuar...")

                        else:
                            print(Fore.RED + "❌ Erro: Valor inválido!\n")

                            input("\nPressione ENTER para continuar...")

                    elif acao_fun == 4:
                        time_clear()
                        remover_conf = menu_interativo(Fore.YELLOW + f"⚠️  Tem certeza de quer remover '{funcionario_alvo['nome']}' da sua lista de funcionários?", ["SIM", "NÃO"])

                        if remover_conf == 0:
                            print(f"\nRemovendo {funcionario_alvo['nome']}...")
                            funcionarios.remove(funcionario_alvo)
                            
                            time.sleep(2)
                            print(Fore.GREEN + "\n✅ Funcionário removido com sucesso!")
                            time.sleep(2)
                            salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

                        elif remover_conf == 1:
                            print("Voltando ao Menu...")
                            time.sleep(2)

        elif opcao_funcionarios == 2:
            ver_funcionario_do_mes = menu_interativo("Selecione:", ["1 - Adicionar o novo melhor funcionário do mês", "2 - Ver o melhor funcionário do mês", "3 - Voltar"])
            time_clear()
            
            if ver_funcionario_do_mes == 0:
                if not funcionarios:
                    print(Fore.YELLOW + "⚠️  Você não tem funcionários registrados! Registre algum para habilitar essa opção.\n")
                    time.sleep(1)
                    input("\nPressione ENTER para continuar...")
                
                else:
                    print(Fore.RED + "                              |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n                              |      LISTA FUNCIONÁRIOS      |\n                              |______________________________|\n\n")
                    for p, item in enumerate(funcionarios):
                            print(Fore.BLACK + "-" * 125)
                            print(Fore.BLUE + f"\n|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n    [{p}] 🙍 Funcionário: {item['nome']}  |  Data de Nascimento: {item['idade']:^5}  |  Salário: R${item['salario']:.2f}  |  Cargo: {item['cargo']}\n|_________________________________________________________________________________________________________________________|\n")
                            print(Fore.BLACK + "-" * 125)
                    indice_input_fun_best = input("\nDigite o número do funcionário que deseja colocar como 'Melhor Funcionário do Mês' (ou ENTER para cancelar): ")
                
                    if not indice_input_fun_best.isdigit():
                        continue
            
                    indice3 = int(indice_input_fun_best)
                
                    if 0 <= indice3 < len(funcionarios):
                        funcionario_alvo_best_of_month = funcionarios[indice3]                
                    limpar_tela()
                    acao_fun_month = input(f"Selecionado: {funcionario_alvo_best_of_month['nome']}\n\nTem certeza que quer adicionar {funcionario_alvo_best_of_month['nome']} como funcionário(a) do mês? (S/N): ").lower()

                    while True:
                        if acao_fun_month in ["s", "sim", "ss"]:
                            for funcionario in funcionarios:
                                funcionario['best_month'] = False
                                funcionario_alvo_best_of_month['best_month'] = True

                            time_clear()
                            
                            print(Fore.WHITE + "Carregando...\n")
                            print(Fore.GREEN + f"✅ {funcionario_alvo_best_of_month['nome']} é o novo melhor funcionário do mês!")
                            
                            input("\nPressione ENTER para continuar...")
                            break

                        elif acao_fun_month in ["n", "não", "nn"]:
                            print(Fore.RED + f"❌ O funcionário {funcionario_alvo_best_of_month['nome']} não irá ser adicionado como o melhor funcionário do mês.\n")
                            input("\nPressione ENTER para continuar...")
                            break

                        else:
                            print(Fore.YELLOW + "⚠️  Digite algo válido como 'S' ou 'N'")
                        salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

            elif ver_funcionario_do_mes == 1:
                melhor = None

                for funcionario in funcionarios:
                    if funcionario.get("best_month") == True:
                        melhor = funcionario
                        break

                if melhor:
                    print(Fore.YELLOW + "🏆 O melhor funcionário do mês é:")
                    time.sleep(0.5)
                    print(Fore.GREEN + f"🎉 {melhor['nome']}! Parabéns a ele(a)")
                else:
                    print(Fore.YELLOW + "⚠️  Nenhum funcionário do mês foi definido ainda.\n")

                input("\nPressione ENTER para continuar...")



        elif opcao_funcionarios == 3:
            time.sleep(1)
            confirmacao_in_funci = menu_interativo("Tem certeza que quer adicionar um funcionário a sua equipe?", ["SIM", "NÃO"])
            time_clear()
            time.sleep(1)
            if confirmacao_in_funci == 0:
                time.sleep(1)
                print(Fore.RED + "|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n" +
                      Fore.LIGHTRED_EX + fr"|       \\\\ ADICIONAR FUNCIONÁRIOS \\\\      |" +
                      Fore.RED + "\n|_____________________________________________|\n\n")

                print(Fore.BLACK + "-" * 50)

                nome_funcionario = input("\n\nNome do seu funcionário\n➤  ")
                time.sleep(1)
                idade_funcionario = input(f"\nData de nascimento do(a) {nome_funcionario} (ex.: 11/05/2000)\n➤  ")
                
                time.sleep(1)
                while True:
                    try:
                        salario = float(input("\nSalário do seu funcionário\n➤  ").replace(",", "."))
                        break
                    except ValueError:
                        print(Fore.RED + "\nErro! Insira somente números!")

                time.sleep(1)
                funcao = input("\nQual cargo o seu funcionário tem?\n➤  ")

                time.sleep(2)
                print("\nCarregando...")
                
                time.sleep(2)
                limpar_tela()
                
                ficha_tecnica = {
                "nome": nome_funcionario,
                "idade": idade_funcionario,
                "salario": salario,
                "cargo": funcao,
                "best_month": False,
                "cpu": random.randint(10, 10000)
                }

                funcionarios.append(ficha_tecnica)

                salvar_dados(nome_usuario, estoque, funcionarios, saldo, senhas)

                print(Fore.MAGENTA + f"|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n                                         Ficha Técnica do seu Funcionário:\n\n  Nome: {nome_funcionario}  \n\n  Data de Nascimento: {idade_funcionario}  \n\n  Salário: R${salario:.2f}  \n\n  Cargo: {funcao}  \n\n|________________________________________________________________________________________________________________|\n\n")
                
                print(Fore.BLACK + "-" * 100)
                
                input("\n\nPressione ENTER para continuar...")

        elif opcao_funcionarios == 4:
            print("\nVoltando...")
            time.sleep(2)
            continue

    # -----------------------------------------
    # OPÇÃO 7: SAIR
    # -----------------------------------------
    elif opcao == 6:
            time.sleep(1)
            sair_options = menu_interativo("Selecione:", ["Desligar sistema", "Reiniciar Sistema", "Suspender Sistema"])

            if sair_options == 0:
                time_clear()
                print(Fore.BLUE + f"\nSaindo... Adeus {nome_usuario} 👋")
                time.sleep(2)
                break

            elif sair_options == 1:
                time_clear()
                print(Fore.BLUE + "\nReiniciando sistema...")
                time.sleep(3)
                reiniciar_programa()

            elif sair_options == 2:
                time_clear()
                print(Fore.YELLOW + "Sistema em modo suspensão 🌙")
                time.sleep(1)
                input("Pressione ENTER para voltar ao menu...")
                continue
