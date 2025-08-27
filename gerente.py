from funcionario import Funcionario

class Gerente(Funcionario): #herança da classe Funcionário
    def __init__(self, nome, cpf, salario, senha, qtde_gerenciaveis):
        super().__init__(nome, cpf, salario) #estabelecendo herança
        self._senha = senha
        self._qtde_gerenciaveis = qtde_gerenciaveis
    
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha

    
    def get_Bonificacao(self):
        return super().get_Bonificacao() + 100 
    

    





