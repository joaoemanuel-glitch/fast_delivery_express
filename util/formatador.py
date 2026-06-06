class Formatador:
    
    @staticmethod
    def formatar_moeda(valor):
        # Transforma o número em uma string de dinheiro (R$ X,XX)
        return f"R$ {valor:.2f}".replace('.', ',')

    @staticmethod
    def texto_titulo(texto):
        # Deixa o texto em caixa alta e limpa espaços inúteis nas pontas
        return texto.strip().upper()