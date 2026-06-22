#O bloco 'with' garante que o arquivo seja fechado automaticamente após o uso.
#Usa 'a' (append) para adicionar novos dados sem apagar os antigos.

def salvar_dados(opcao):
    with open("dados_menu.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Opção escolhida: {opcao}\n")
    print("Dados salvos com sucesso!\n")

#Usa 'r' (read) para ler o conteúdo do arquivo.
#O bloco 'try-except' evita que o programa quebre caso o arquivo ainda não exista.

def ler_dados():
    try:
        with open("dados_menu.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip() == "":
                print("O arquivo está vazio.\n")
            else:
                print("\n--- DADOS SALVOS ---")
                print(conteudo)
                print("---------------------\n")
    except FileNotFoundError:
        print("Nenhum dado salvo ainda. O arquivo não foi criado.\n")

#Estrutura principal do programa
def main():
    #A estrutura de repetição 'while True' cria um loop infinito que só para quando o usuário digitar a opção 3 (Sair).
    while True:
        print("Menu:")
        print("1. Ler")
        print("2. Salvar")
        print("3. Sair")

        escolha = input("Digite uma opção do menu (1-3): ")

        #A estrutura de decisão 'if-elif-else' desvia o fluxo do programa com base na entrada digitada pelo usuário.
        if escolha == "1":
            ler_dados()
        elif escolha == "2":
            #Exemplo estático da funcionalidade de salvar (lê a opção do teclado para salvar)
            opcao_salvar = input("Digite o dado que deseja salvar (ex: 1 ou 2): ")
            salvar_dados(opcao_salvar)
        elif escolha == "3":
            print("Saindo do programa. Até logo!")
            break  #Interrompe o laço 'while' e encerra a aplicação
        else:
            print("Opção inválida! Por favor, digite 1, 2 ou 3.\n")

#Executa a função principal
if __name__ == "__main__":
    main()