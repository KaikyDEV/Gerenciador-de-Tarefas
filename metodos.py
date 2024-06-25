class GerenciadorDeTarefas:
    def __init__(self):
        self.lista_de_tarefas = []

    def aplicar_tarefa(self, tarefa):
        self.lista_de_tarefas.append(tarefa)
        print(f'Tarefa: {tarefa} aplicada 👌')

    def remover_tarefa(self, tarefa):
        if tarefa in self.lista_de_tarefas:
            self.lista_de_tarefas.remove(tarefa)
        else:
            print("Tarefa não encontrada!")

    def modificar_tarefa(self, tarefa_antiga, tarefa_nova):
        if tarefa_antiga in self.lista_de_tarefas:
            indice = self.lista_de_tarefas.index(tarefa_antiga)
            self.lista_de_tarefas[indice] = tarefa_nova
            print(f'Tarefa "{tarefa_antiga}" substituida por "{tarefa_nova}".')
        else:
            print(f'Sem conhecimento da tarefa {tarefa_antiga}')

    def mostrar_tarefas(self):
            print(self.lista_de_tarefas)