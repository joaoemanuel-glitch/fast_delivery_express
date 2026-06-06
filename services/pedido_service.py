from modelos.pedido import Pedido # Importa a classe Pedido do pacote pedido.py
from modelos.cliente import Cliente # Importa a classe Cliente do pacote cliente.py

class PedidoService:
    
    def __init__(self):
        # Lista que armazena os pedidos que são acessados pelo seu código
        self.pedidos = []

    # criar um pedido
    def criar_pedido(self, codigo, cliente, peso, distancia, tipo_entrega):
        # Instancia o novo pedido
        novo_pedido = Pedido(codigo, cliente, peso, distancia, tipo_entrega)
        self.pedidos.append(novo_pedido) # adiciona o novo pedido na lista de pedidos
        return novo_pedido # retorna o novo pedido

    # listar todos os pedidos
    def listar_todos(self):
        return self.pedidos # retorna todos os pedidos que estão armazenados na lista

    def buscar_por_codigo(self, codigo):
        # Percorre a lista de pedidos
        for p in self.pedidos:
            if p.codigo == codigo:
                return p # retorna o pedido com o código que foi informado
        return None