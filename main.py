from funcionario import Funcionario
from gerente import Gerente

if __name__ == '__main__':


    func1 = Funcionario("João da Silva", "111.111.111-11", 1200.00)
    print(func1.get_Bonificacao())

    ger1 = Gerente("José Souza", "222.222.222-22", 5000.00, "12345678", 21)
    print(ger1.get_Bonificacao())
