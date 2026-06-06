# Superclasse
class Pessoa:
    def __init__(self, nome, cpf, telefone): # atributos da classe Pessoa
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
    
    # Getters para acessar os atributos de fora da classe
    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def telefone(self):
        return self.__telefone