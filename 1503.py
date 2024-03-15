class Calculadora:
    def __init__(self, *args):
        self.args = args


    def somar(self):
        print(sum(self.args))


    def subtrair(self):
        c = 0
        for arg in self.args:
            c-= arg

        print(c+ 2*self.args[0])

    def mul(self):
        c = 1
        for arg in self.args:
            c*=arg
        print(c)


    def div(self):
        c = self.args[0]
        for arg in self.args:
            c/=arg
        print(c*self.args[0])




lista = []
lista2 = ['s','S', 'n','N']
n = ['n','N']
while True:
    numero = float(input('Digite um numero: '))
    lista.append(numero)
    yn = str(input('Deseja continuar[s/n]: '))
    while yn not in lista2:
        print('Digite apenas s ou n')
        yn = str(input('Deseja continuar[s/n]: '))
    if yn in n:
        break

operacoes = ['+','-','*','/']
while True:
    operacao = str(input('Qual operacao realizar com os numeros  (+,-,*,/): '))
    if operacao not in operacoes:
        print('digite apenas + - * / ')
    elif operacao in operacoes:
        break


c = Calculadora(*lista)

if operacao == '+':
    c.somar()

elif operacao == '-':
    c.subtrair()

elif operacao == '/':
    c.div()

elif operacao == '*':
    c.mul()


