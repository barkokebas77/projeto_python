import random

def jogar_forca():
    palavras = []
    palavra_secreta = random.choice(palavras)
    letras_corretas = ['_'] * len(palavra_secreta)
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra secreta tem", len(palavra_secreta), "letras.")

    while tentativas > 0:
        print("Palavra: ", " ".join(letras_corretas))
        print("Tentativas restantes:", tentativas)
        print("Letras erradas:", ", ".join(letras_erradas))

        letra = input("Digite uma letra: ").lower()

        if letra in letras_erradas or letra in letras_corretas:
            print("Você já tentou essa letra.")
        elif letra in palavra_secreta:
            print("Boa! A letra está na palavra.")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_corretas[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1

        if '_' not in letras_corretas:
            print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
            break

    if tentativas == 0:
        print("Você perdeu! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    jogar_forca()