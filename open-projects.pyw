import json
import os
import sys
import subprocess
import time

def carregar_projetos():
    try:
        with open('caminhos.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        input("Erro: Arquivo 'caminhos.json' não encontrado. Pressione Enter para sair...")
        sys.exit(1)
    except json.JSONDecodeError:
        input("Erro: Arquivo 'caminhos.json' mal formatado. Pressione Enter para sair...")
        sys.exit(1)

def listar_projetos(projetos):
    print("\nProjetos disponíveis:")
    for i, projeto in enumerate(projetos.keys(), start=1):
        print(f"{i}- {projeto}")
    print("0- Sair")

def selecionar_projeto(projetos):
    while True:
        try:
            escolha = input("\nDigite o número do projeto que deseja abrir: ")
            if escolha == '0':
                return None
            escolha = int(escolha)
            projeto = list(projetos.keys())[escolha - 1]
            return projeto
        except (ValueError, IndexError):
            print("Opção inválida. Por favor, digite um número da lista.")

def abrir_projeto_no_vscode(projeto, projetos):
    paths = projetos[projeto].get('paths', [])
    if not paths:
        input(f"O projeto '{projeto}' não possui caminhos definidos. Pressione Enter para continuar...")
        return
    
    print(f"\nAbrindo projeto '{projeto}' no VSCode...")
    for path in paths:
        if not os.path.exists(path):
            print(f"  Aviso: Caminho não encontrado - {path}")
            continue
        
        comando = f'code "{path}"'
        print(f"  Executando: {comando}")
        subprocess.Popen(comando, shell=True)

def criar_terminal():
    # Configura o terminal com um título personalizado
    os.system('title Gerenciador de Projetos - VSCode')
    # Limpa a tela (funciona no Windows)
    os.system('cls')

def main():
    criar_terminal()
    print("=== Abridor de Projetos no VSCode ===")
    print("Este aplicativo abre todos os caminhos de um projeto no VSCode.\n")
    
    projetos = carregar_projetos()
    
    while True:
        listar_projetos(projetos)
        projeto_selecionado = selecionar_projeto(projetos)
        
        if projeto_selecionado is None:
            print("Saindo...")
            break
            
        abrir_projeto_no_vscode(projeto_selecionado, projetos)

# Adicione esta função
def fechar_terminal():
    """Fecha o terminal CMD"""
    time.sleep(3)
    os.system("taskkill /f /im cmd.exe")

if __name__ == "__main__":
    # Verifica se está rodando como .pyw e abre um novo terminal se necessário
    if sys.executable.endswith('pythonw.exe'):
        subprocess.Popen(['cmd', '/k', sys.executable.replace('pythonw.exe', 'python.exe'), __file__])
    else:
        try:
            main()
        finally:
            fechar_terminal()