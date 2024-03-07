import math

num = int(input("Digite um número inteiro para calcular a sequência de Fibonacci: "))

anterior = 0
atual = 1
prox = 0
i = 0

for i in range(num):
    print(atual)

    prox = anterior + atual
    anterior = atual
    atual = prox


def numPerfeito(n):
    raiz = int(math.sqrt(n))
    raiz *= raiz

    if raiz != n:
        return False

    return True


def isFibonacci(n):
    a = numPerfeito(n)

    if a:
        print("Pertence a sequência!")
    else:
        print("Não pertence a sequência!")


isFibonacci(num)
