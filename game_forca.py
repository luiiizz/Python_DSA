# -*- coding: utf-8 -*-
# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>JOGO DA FORCA<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''', 2]


# Classe
class Game_forca:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.letras_corretas = []
        self.letras_erradas = []

    # Método para adivinhar a letra
    def hipotese(self, letra):
        if letra in self.word and letra not in self.letras_corretas:
            self.letras_corretas.append(letra)
        elif letra not in self.word and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def terminou(self):
        if self.venceu() == True or len(self.letras_erradas) == 6:
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def venceu(self):
        if "_" not in self.oculta():
            return True
        else:
            return False

        # Método para não mostrar a letra no board

    def oculta(self):
        oc = ""
        for l in self.word:
            if l not in self.letras_corretas:
                oc += "_"
            else:
                oc += l
        return oc

    # Método para checar o status do game e imprimir o board na tela
    def game_status(self):
        print(board[len(self.letras_erradas)])
        print("\nPalavra: " + self.oculta())
        print("\nLetras Erradas: ")
        for l in self.letras_erradas:
            print(l)
        print()
        print("Letras corretas: ")
        for l in self.letras_corretas:
            print(l)
        print()


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    jogo = Game_forca(rand_word())

    while not jogo.terminou():
        jogo.game_status()
        ll = input("\nDigite um letra: ")
        jogo.hipotese(ll)

    jogo.game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if jogo.venceu():
        print("#################################")
        print("¨¨¨¨PARABÉNS VOÇÊ VENCEU!!!!!¨¨¨¨")
        print("#################################")
    else:
        print("#################################")
        print("¨¨¨¨¨¨¨¨¨¨¨¨GAME OVER¨¨¨¨¨¨¨¨¨¨¨¨")
        print("#################################")
        try:
            print("\nA palavra era: %s" % rand_word())
        except:
            print("\nPalavra não encontrada")

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa

print("\nPRONTO PARA JOGAR!!!!!")
inicio = input("\nDigite 'C' para Começar ou 'S' para Sair: ")
while inicio == "C" or inicio == 'c':
    if __name__ == "__main__":
        main()
    inicio = input("Pressione 'C' para recomeçar (era bom ir estudar) ou 'S' para Sair: ")
