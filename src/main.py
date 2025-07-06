from tabuleiro import Tabuleiro
from movimentos import movimento_valido

def main():
    tabuleiro = Tabuleiro()
    turno = "branco"

    while True:
        tabuleiro.exibir()
        print(f"Turno: {turno.capitalize()}")

        origem = input("Digite a posição de origem (ex: 6 0): ")
        destino = input("Digite a posição de destino (ex: 4 0): ")

        try:
            origem_linha, origem_coluna = map(int, origem.split())
            destino_linha, destino_coluna = map(int, destino.split())
        except:
            print("Entrada inválida! Use o formato: linha coluna (ex: 6 0)")
            continue

        if not tabuleiro.verificar_peca_turno(origem_linha, origem_coluna, turno):
            print("Você só pode mover suas próprias peças!")
            continue

        if movimento_valido(origem_linha, origem_coluna, destino_linha, destino_coluna):
            tabuleiro.mover(origem_linha, origem_coluna, destino_linha, destino_coluna)
            turno = "preto" if turno == "branco" else "branco"
        else:
            print("Movimento inválido! Tente novamente.")

if __name__ == "__main__":
    main()
