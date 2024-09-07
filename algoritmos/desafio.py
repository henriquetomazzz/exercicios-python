class Contato:
   
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome} {self.telefone} {self.email}"

    def formatoRegistro(self):
        return f"{self.nome}:{self.telefone}:{self.email}\n"

def menu():
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Sair")
    op = input("Opção: ")
   
    return op

def adicionar(dados):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
   
    dados[telefone] = Contato(nome, telefone, email)

def listar(dados):
    if len(dados) == 0:
        print("Nenhum contato cadastrado!")
    else:
        for contato in sorted(dados.values(), key = lambda x: x.nome):
            print(contato)

def remover(dados):
    telefone = input("Telefone do contato a excluir: ")
    if telefone in dados:
        dados.pop(telefone)
    else:
        print("Telefone não encontrado!")

def salvarDados(dados):
    arquivo = open("contatos.txt", "w")
   
    for contato in dados.values():
        arquivo.write(contato.formatoRegistro())
       
    arquivo.close()

def carregarDados(dados):
    arquivo = open("contatos.txt", "r")
   
    for linha in arquivo:
        nome, telefone, email = linha.strip().split(":")
        dados[telefone] = Contato(nome, telefone, email)
   
    arquivo.close()

dados = {}

carregarDados(dados)

op = menu()
while op != "4":
   
    if op == "1":
        adicionar(dados)
       
    elif op == "2":
        listar(dados)
       
    elif op == "3":
        remover(dados)
   
    else:
        print("Opção inválida!")
   
    op = menu()
   
salvarDados(dados)
