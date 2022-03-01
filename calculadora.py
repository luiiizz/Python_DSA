## Calculadora Python
import os
import math


def menu():
    print("\n----------------------CALCULADORA EM PYTHON-------------------\n")
    print("Escolha o tipo de operação que deseja realizar: ")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raiz quadrada")
    print("6. Sair\n")
    return;


# python calculadora.py
a = math.sqrt(16)

menu()
op = int(input("\nDigite uma opção de 1 a 6: "))
while (op != 6):
    if op != 5:
        valor1 = float(input("\nDigite o primerio valor: "))
        valor2 = float(input("Digite o segundo valor: "))

    if (op == 1):
        soma = valor1 + valor2
        print("\n\n------SOMA------")
        print("\nResultado: %.1f + %.1f = %.1f" % (valor1, valor2, soma))
    elif (op == 2):
        sub = valor1 - valor2
        print("\n\n------SUBTRAÇÃO------")
        print("\nResultado: %.1f - %.1f = %.1f" % (valor1, valor2, sub))
    elif (op == 3):
        mul = valor1 * valor2
        print("\n\n------MULTIPLICAÇÃO------")
        print("\nResultado: %.1f x %.1f = %.1f" % (valor1, valor2, mul))
    elif (op == 4):
        div = valor1 / valor2
        print("\n\n------DIVISÃO------")
        print("\nResultado: %.1f / %.1f = %.1f" % (valor1, valor2, div))
    elif (op == 5):
        print("\n\n------RAIZ QUADRADA------")
        raiz = int(input("\nDigite um valor para calcular sua raiz: "))
        print("\nRaiz quadrada de %d é %.1f" % (raiz, math.sqrt(raiz)))

    s = input("\n\nPressione Space + Enter para limpar")
    if s == " " or s == "  " or s == "   ":
        os.system('cls') or None
    menu()
    op = int(input("\n\nDigite uma opção de 1 a 5: "))

a = "\n\nObrigado por utilizar um produto de Henriks"
print(a.upper())
