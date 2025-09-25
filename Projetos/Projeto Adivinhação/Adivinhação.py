import random

valor = random.randint(1,11)
vitoria = False

while not vitoria:

    resposta = input("Digite um número entre 1 e 10! ")

    if int(resposta) == valor:
        print("Você acertou!")
        vitoria = True
        print("O valor sorteado foi: " + str(valor))

    else:
        print("Não foi desta vez!")