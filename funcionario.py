from funcionariobase import FuncionarioBase

class Funcionario(FuncionarioBase):
    def get_Bonificacao(self): #método privado 
        return self._salario * 0.10
    


