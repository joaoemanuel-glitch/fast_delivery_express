from modelos.cliente import Cliente # Importa a classe Cliente do pacote cliente.py
from interfaces.calculo_frete_interface import CalculoFrete # Importa a classe CalculoFrete

class Pedido:
    # Lista de status que são válidos
    TIPOS_STATUS = ["Em preparação", "Saiu para entrega", "Entregue", "Cancelado"]

    def __init__(self, codigo, cliente, peso, distancia, tipo_entrega): # Atributos
        self.__codigo = codigo
        self.__cliente = cliente
        self.__peso = peso
        self.__distancia = distancia
        self.__tipo_entrega = tipo_entrega
        self.__status = "Em preparação" # Esse é o status inicial de todos os pedidos
        self.__valor_frete = tipo_entrega.calcular_frete(distancia) # Polimorfismo dinâmico

    # Getters
    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def status(self):
        return self.__status

    # Setter para permitir a alteração do status do pedido no menu
    @status.setter
    def status(self, novo_status):
        self.__status = novo_status

    @property
    def valor_frete(self):
        return self.__valor_frete