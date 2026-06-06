from abc import ABC, abstractmethod

# Classe abstrata
class CalculoFrete(ABC):
    # Método obrigatório para calcular o frete
    # Todos os tipos de entrega deverão usar esse método
    @abstractmethod
    def calcular_frete(self, distancia):
        pass