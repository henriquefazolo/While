'''
Crie um código utilizando LAÇO WHILE:
Enquanto a1=0 for menor que 5, incrementando 1 a cada laço, mostre na tela o seu número.
Enquanto a2=0 for menor que 3, incrementando 1 a cada laço, mostre na tela o seu número multiplicado por 10.
Enquanto a3=20  for maior que 10, decrementando 1 a cada laço, mostre na tela o seu número.
Para a4=0 enquanto a4 menor que 10, incrementando 1, mostre na tela o seu número

'''


def incrementar(n, maximo, incremento=1):
    """
    Exibe o valor de n até o valor do maximo seja atingido em cada incremento.

    :param n: valor inteiro
    :param maximo: valor maximo a ser atingido
    :param incremento: valor a ser incrementado, pradão +1
    """
    while n < maximo:
        n += incremento
        print(n)
    print()


def decrementar(n, minimo, decremento=-1):
    """
    Exibe o valor de n até o valor do minimo seja atingido em cada decremento.

    :param n: valor inteiro
    :param minimo: valor minimo a ser atingido
    :param decremento: valor a ser decrementado, padrao -1
    """
    while n > minimo:
        n -= decremento
        print(n)
    print()


class LacoWhile:
    def __init__(self):
        self.a1 = 0
        self.a2 = 0
        self.a3 = 20
        self.a4 = 0


a = LacoWhile()

incrementar(a.a1, 5, 1)
incrementar(a.a2, 3, 1)
decrementar(a.a3, 10, 1)
incrementar(a.a4, 10, 1)
