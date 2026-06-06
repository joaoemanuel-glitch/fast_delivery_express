import os # Para importar os comando de limpeza de tela

class Menu:
    @staticmethod
    def limpar_tela():
        # Executa o comando de limpar o terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        # Se o sistema operacional for Windows, usa cls, se for Linux, usa clear

    # Métodos estáticos apenas para imprimir as opções textuais na tela e capturar o input
    @staticmethod
    # Menu principal
    def principal():
        print("\n=== FASTDELIVERY EXPRESS ===")
        print("1. Menu de Clientes")
        print("2. Menu de Entregadores")
        print("3. Menu de Pedidos")
        print("0. Sair")
        return input("Escolha uma opção: ")

    @staticmethod
    # Menu de clientes
    def clientes():
        print("\n--- CLIENTES ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Buscar por CPF")
        print("0. Voltar")
        return input("Opção: ")

    @staticmethod
    # Menu de entregadores
    def entregadores():
        print("\n--- ENTREGADORES ---")
        print("1. Cadastrar Entregador")
        print("2. Listar Entregadores")
        print("0. Voltar")
        return input("Opção: ")

    @staticmethod
    # Menu de pedidos
    def pedidos():
        print("\n--- PEDIDOS ---")
        print("1. Criar Pedido")
        print("2. Listar Pedidos")
        print("3. Atualizar Status")
        print("0. Voltar")
        return input("Opção: ")