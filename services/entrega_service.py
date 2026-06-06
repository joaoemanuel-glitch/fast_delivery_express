# Importa as classes EntregaComum, EntregaExpressa e EntregaPremium
from modelos.entrega import EntregaComum, EntregaExpressa, EntregaPremium
from modelos.entregador import Entregador # Importa a classe Entregador do pacote entregador.py

class EntregaService:
    def __init__(self):
        # Lista para armazenar os entregadores
        self.entregadores = []
    
    # Método estático para fabricar a estratégia correta de frete com base na opção do menu
    @staticmethod
    def criar_tipo_entrega(opcao):
        if opcao == "1":
            return EntregaComum()
        elif opcao == "2":
            return EntregaExpressa()
        elif opcao == "3":
            return EntregaPremium()
        return None

    # Cadastra um entregador
    def cadastrar_entregador(self, nome, cpf, telefone, veiculo, cnh):
        # Percorre a lista de entregadores
        for e in self.entregadores:
            if e.cpf == cpf: # Caso já exista um entregador cadastrado com o mesmo CPF
                print("Inválido! Já existe um entregador com este CPF.")
                return None
        
        # Instancia o entregador
        novo = Entregador(nome, cpf, telefone, veiculo, cnh)
        self.entregadores.append(novo) # Adiciona o novo entregador na lista
        return novo # Retorna o novo entregador

    # Lista todos os entregadores
    def listar_todos_entregadores(self):
        return self.entregadores