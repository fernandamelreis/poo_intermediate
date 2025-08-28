from funcionariobase import FuncionarioBase


class Gerente(FuncionarioBase): #herança da classe Funcionário
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

    @property
    def qtde_gerenciaveis(self):
        return self._qtde_gerenciaveis
    @qtde_gerenciaveis.setter
    def qtde_gerenciaveis(self, qtde_gerenciaveis):
        self._qtde_gerenciaveis = qtde_gerenciaveis
    

    def get_Bonificacao(self):
        return super().get_Bonificacao() #herança do método 
    

    





