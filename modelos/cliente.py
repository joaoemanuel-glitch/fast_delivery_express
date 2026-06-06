from modelos.pessoa import Pessoa # Importa a classe Pessoa do pacote pessoa.py

# Subclasse
class Cliente(Pessoa): # A classe Cliente herda as características da classe Pessoa
    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(nome, cpf, telefone) # método para repassar todos os atributos da classe Pessoa
        self.__endereco = endereco # atributo da própria classe Cliente
    
    # Getter
    @property
    def endereco(self):
        return self.__endereco
    
    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf}) - Endereço: {self.endereco}"