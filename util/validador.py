class Validador:

    @staticmethod
    def validar_texto(texto: str) -> bool:
        # Verifica se o usuário digitou alguma coisa ou se apenas apertou Enter
        if not texto or texto.strip() == "":
            return False
        return True

    @staticmethod
    def validar_numero_positivo(valor_str: str) -> float:
        # Tenta converter a string para número. Se der erro ou for menor ou igual a zero, retorna 0.0
        try:
            valor = float(valor_str)
            if valor > 0:
                return valor
            return 0.0
        except ValueError:
            return 0.0