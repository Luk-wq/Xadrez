class Tabuleiro:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()

    def criar_tabuleiro(self):
        return [
            ["T", "C", "B", "Q", "K", "B", "C", "T"],
            ["P"] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            ["p"] * 8,
            ["t", "c", "b", "q", "k", "b", "c", "t"]
        ]

    def exibir(self):
        print("\n   0   1   2   3   4   5   6   7")
        print("  ---------------------------------")
        for i, linha in enumerate(self.tabuleiro):
            print(f"{i} | " + " | ".join(linha) + " |")
            print("  ---------------------------------")

    def mover(self, origem_linha, origem_coluna, destino_linha, destino_coluna):
        peca = self.tabuleiro[origem_linha][origem_coluna]

        if peca == " ":
            print("Não há peça nessa posição.")
            return

        self.tabuleiro[destino_linha][destino_coluna] = peca
        self.tabuleiro[origem_linha][origem_coluna] = " "
        print(f"Peça {peca} movida!")

    def verificar_peca_turno(self, linha, coluna, turno):
        peca = self.tabuleiro[linha][coluna]
        if peca == " ":
            return False
        if turno == "branco" and peca.islower():
            return False
        if turno == "preto" and peca.isupper():
            return False
        return True
