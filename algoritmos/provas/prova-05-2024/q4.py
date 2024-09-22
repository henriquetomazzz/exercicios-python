#############################
##        Classes          ##
#############################

class Fila:

    def __init__(self):
        self.valores = []

    def adicionar(self, x):
        self.valores.append(x)

    def remover(self):
        if len(self.valores) == 0:
            return None
        return self.valores.pop(0)

    def tamanho(self):
        return len(self.valores)

    def __str__(self):
        return ", ".join(self.valores)

class FilaAtendimento:

    def __init__(self):
        self.filaRegular = Fila()
        self.filaPrioridade = Fila()
        self.vezPrioridade = True

    def exibirTamanhoFila(self):
        print("Prioritários: ", self.filaPrioridade.tamanho())
        print("Regulares: ", self.filaRegular.tamanho())

    def exibirFila(self):
        print("Prioritários:", self.filaPrioridade)
        print("Regulares:", self.filaRegular)

    def chamarPaciente(self):

        if self.vezPrioridade or self.filaRegular.tamanho() == 0:
            if self.filaPrioridade.tamanho() > 0:
                print(self.filaPrioridade.remover())
            else:
                print("Não há pacientes a atender!")
        else:
            print(self.filaRegular.remover())

        self.vezPrioridade = not self.vezPrioridade

    def adicionarPaciente(self):
        tipo = input("Tipo de paciente (1 - Prioridade, 2 - Regular): ")

        if tipo == "1" or tipo == "2":
            nome = input("Nome: ")

            if tipo == "1":
                self.filaPrioridade.adicionar(nome)
            else:
                self.filaRegular.adicionar(nome)
        else:
            print("Tipo de paciente deve ser preenchido com 1 ou 2.")
            self.adicionarPaciente()
#############################
##         Funções          ##
#############################

def menu():
    print("1 - Tamanho fila")
    print("2 - Fila")
    print("3 - Chamar paciente")
    print("4 - Adicionar paciente")
    print("5 - Sair")
    op = int(input("Opção: "))
    if op >= 1 and op <= 5:
        return op
    else:
        print("Opção inválida!")
        return menu()

#############################
##  Programa Principal     ##
#############################

atendimento = FilaAtendimento()

op = menu()
while op != 5:
    
    if op == 1:
      atendimento.exibirTamanhoFila()

    elif op == 2:
        atendimento.exibirFila()

    elif op == 3:
        atendimento.chamarPaciente()

    elif op == 4:
        atendimento.adicionarPaciente()

op = menu()