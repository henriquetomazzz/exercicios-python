from cliente import clientes

def obter_cpf():
    while True:
        cpf = input("Digite o CPF (somente números, 9 dígitos): ")

        cpf = cpf.replace('.', '').replace('-', '')
        
        if len(cpf) == 9 and cpf.isdigit():
            return cpf
        
        else:
            print("\nErro: O CPF deve conter exatamente 9 dígitos numéricos.")

def obter_senha():
    while True:
        senha = input("Digite a sua senha (4 dígitos): ")

        if len(senha) == 4 and senha.isdigit():
            return senha
        else: 
            print("\nERRO: A senha deve conter exatamente 4 dígitos numéricos.")

def validar_usuario(cpf, senha):
    # Supondo que 'clientes' é um dicionário onde as chaves são CPFs e os valores são senhas
    if cpf in clientes and clientes[cpf] == senha:
        return True
    else:
        return False

# Função principal para coleta e validação
def main():
    cpf = obter_cpf()
    senha = obter_senha()

    if validar_usuario(cpf, senha):
        print("Usuário validado com sucesso!")
    else:
        print("CPF ou senha incorretos. Tente novamente.")


'''     
print("Serviços disoniveis")
print("1-Transferir dinheiro")
print("2-Depositar dinheiro")
print("3-Sacar dinheiro")
servico = int(input("Por favor digite o número do serviço desejado: "))

senha = int(input("Digite a"))
valor = float(input("Digite o valor que deseja transferir: "))

if servico == 1: 
    valor
    if valor >= saldo: 
        saldo - valor
        print("Saldo suficiente!")#acrescentar cores
    else: 
        print("Saldo insuficiente!")
    senha  
if servico == 2:

if servico == 3: 
'''
