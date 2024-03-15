print('Aula de salvar')
print('apayaye')


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


c = Calculadora(10, 4, .5)


c.div()
