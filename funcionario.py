class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario 

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def get_Bonificacao(self): #método privado 
        return self._salario * 0.10
    


