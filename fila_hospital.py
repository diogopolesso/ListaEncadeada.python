class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.contador_verde = 1
        self.contador_amarelo = 201

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A/V): ").strip().upper()
        if cor not in ('A', 'V'):
            print("Cor inválida!")
            return
        
        if cor == 'A':
            numero = self.contador_amarelo
            self.contador_amarelo += 1
        else:
            numero = self.contador_verde
            self.contador_verde += 1
        
        novo_nodo = Nodo(numero, cor)
        
        if not self.head:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        else:
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        if not self.head:
            print("Nenhum paciente na fila.")
            return
        atual = self.head
        while atual:
            print(f"Cartão {atual.numero} - Cor {atual.cor}")
            atual = atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
            return
        print(f"Chamando paciente com cartão número {self.head.numero}")
        self.head = self.head.proximo

    def menu(self):
        while True:
            print("\n1 – Adicionar paciente à fila")
            print("2 – Mostrar pacientes na fila")
            print("3 – Chamar paciente")
            print("4 – Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.imprimirListaEspera()
            elif opcao == '3':
                self.atenderPaciente()
            elif opcao == '4':
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida! Tente novamente.")

# Execução do programa
fila_hospital = ListaEncadeada()
fila_hospital.menu()
