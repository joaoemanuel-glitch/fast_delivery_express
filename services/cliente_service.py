from modelos.cliente import Cliente # Importa a classe Cliente do pacote cliente.py

class ClienteService:
    def __init__(self):
        # Armazena todos os clientes
        # Os clientes são acessados pelo seu CPF
        self.clientes = []

    # Cadastra um cliente
    def cadastrar_cliente(self, nome, cpf, telefone, endereco):
        # Caso o usuário cadastre um cliente com um CPF que já foi cadastrado
        if self.buscar_por_cpf(cpf):
            print("Inválido! Já existe um cliente cadastrado com este CPF.")
            return None
        
        novo = Cliente(nome, cpf, telefone, endereco) # instancia o novo cliente
        self.clientes.append(novo) # adicionando o cliente na lista de clientes
        return novo

    # Busca por um cliente através do CPF
    def buscar_por_cpf(self, cpf):
        # Percorre a lista de clientes
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente # Retorna o cliente procurado
        return None # Retorna None se não achar nenhum cliente

    # Lista todos os clientes armazenados em self.clientes
    def listar_todos(self):
        return self.clientes