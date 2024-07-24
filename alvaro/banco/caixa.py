class Conta:
    def __init__(self, nome, cpf, saldo_inicial=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        return self.saldo

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Saldo: R${self.saldo:.2f}"


class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, nome, cpf, saldo_inicial=0):
        if any(conta.cpf == cpf for conta in self.contas):
            print("Erro: CPF já cadastrado.")
            return
        nova_conta = Conta(nome, cpf, saldo_inicial)
        self.contas.append(nova_conta)
        print("Conta criada com sucesso!")

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta registrada.")
        for conta in self.contas:
            print(conta)

    def encontrar_conta(self, cpf):
        for conta in self.contas:
            if conta.cpf == cpf:
                return conta
        print("Conta não encontrada.")
        return None


def menu():
    banco = Banco()

    while True:
        print("---"*20)
        print("\033[1mMenu:\033[m")
        print("---"*20)
        print("1. Criar conta")
        print("2. Consultar saldo")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Listar contas")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            saldo_inicial = float(input("Saldo inicial (0 se não tiver): "))
            banco.criar_conta(nome, cpf, saldo_inicial)
        
        elif opcao == '2':
            cpf = input("CPF da conta: ")
            conta = banco.encontrar_conta(cpf)
            if conta:
                print(f"Saldo: R${conta.consultar_saldo():.2f}")
        
        elif opcao == '3':
            cpf = input("CPF da conta: ")
            valor = float(input("Valor do depósito: "))
            conta = banco.encontrar_conta(cpf)
            if conta:
                conta.depositar(valor)
        
        elif opcao == '4':
            cpf = input("CPF da conta: ")
            valor = float(input("Valor do saque: "))
            conta = banco.encontrar_conta(cpf)
            if conta:
                conta.sacar(valor)
        
        elif opcao == '5':
            banco.listar_contas()
        
        elif opcao == '6':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()