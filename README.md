# Desafio Xadrez 🏁♟️

## 📚 Descrição
Este projeto foi desenvolvido para o desafio da disciplina, com o objetivo de implementar um jogo de **xadrez simplificado** utilizando a linguagem Python, com código bem estruturado, dividido em arquivos, e fácil de entender.

O jogo permite:
- Exibir o tabuleiro de xadrez.
- Movimentar as peças manualmente pelo terminal.
- Alternar automaticamente o turno entre os jogadores **branco** e **preto**.
- Validar se o jogador está tentando mover suas próprias peças.
- Validar movimentos básicos (não mover para a mesma posição).

## 💻 Tecnologias utilizadas
- Python 3
- Terminal (modo texto)
- VS Code

## 📂 Estrutura do Projeto

## ▶️ Como executar o projeto
1. Clone o repositório:
```bash
git clone [cole aqui o link do seu repositório]
cd xadrez/src
python main.py
Digite a posição de origem (ex: 6 0):
## 🎮 Como jogar
- O tabuleiro será exibido no terminal.
- As peças **maiúsculas** representam o jogador **branco**.
- As peças **minúsculas** representam o jogador **preto**.
- O jogo informará de quem é o turno.

### Exemplo de jogada:
Quando solicitado:
```text
Digite a posição de origem (ex: 6 0):
6 0
Digite a posição de destino (ex: 4 0):
4 0
Só é possível mover as peças do seu turno.

O turno alterna automaticamente entre branco e preto.

Movimentos inválidos (como mover para a mesma posição ou mover peças do adversário) não são aceitos.

Por enquanto, qualquer movimento de deslocamento é aceito (não há validação específica
├── src/
│   ├── main.py          # Arquivo principal: executa o jogo e controla os turnos
│   ├── tabuleiro.py     # Gerencia o tabuleiro e as movimentações das peças
│   ├── peca.py          # Estrutura das peças (pode ser expandida)
│   └── movimentos.py    # Valida os movimentos básicos
├── README.md            # Documentação do projeto
## 🔧 Melhorias futuras (opcional)
- Criar regras completas para o movimento de cada peça.
- Implementar captura de peças.
- Detectar xeque e xeque-mate.
- Criar sistema de vitória.

## 👨‍💻 Desenvolvido por
Lukas Monteiro

