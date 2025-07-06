class Peca:
    def __init__(self, tipo, cor):
        self.tipo = tipo  # 'P', 'T', 'C', etc.
        self.cor = cor    # 'branco' ou 'preto'

    def __str__(self):
        return self.tipo
