from modelos.pessoa import Pessoa # Importa a classe Pessoa do pacote pessoa.py

# Subclasse
class Entregador(Pessoa): # A classe Entregador herda as características da classe Pessoa
    def __init__(self, nome, cpf, telefone, veiculo, cnh):
        super().__init__(nome, cpf, telefone) # método para repassar todos os atributos da classe Pessoa
        self.__veiculo = veiculo # atributo da própria classe Entregador
        self.__cnh = cnh # atributo da própria classe Entregador
    
    # Getters
    @property
    def veiculo(self):
        return self.__veiculo
    
    @property
    def cnh(self):
        return self.__cnh