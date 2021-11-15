# Duas formas para se fazer a leitura de um número inteiro...#

def leiaint(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[31mERRO ! Digite um número inteiro válido.\033[m')
    return valor


a = leiaint('Digite um valor: ')
print(f'{a} É um inteiro!!')


def leiainteiro(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except ValueError:
            print('\033[31mERRO ! Digite um número inteiro válido.\033[m')
    return n


b = leiainteiro('Digite um numero: ')
print(f'{b} É um inteiro!!')
