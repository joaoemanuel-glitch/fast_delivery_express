from interfaces.calculo_frete_interface import CalculoFrete # Importa a classe CalculoFrete

class EntregaComum(CalculoFrete): # herança e polimorfismo
    def calcular_frete(self, distancia): # método obrigatório da classe CalculoFrete
        return distancia * 1.5 # taxa simples

class EntregaExpressa(CalculoFrete): # herança e polimorfismo
    def calcular_frete(self, distancia): # método obrigatório da classe CalculoFrete
        return distancia * 3 # taxa maior

class EntregaPremium(CalculoFrete): # herança e polimorfismo
    def calcular_frete(self, distancia): # método obrigatório da classe CalculoFrete
        return (distancia * 5) + 20 # taxa vip