import numpy as np

class Estabelecimento:
    def __init__(self, horizonte: int, capacidade: int, taxaChegada: int, taxaAtendimento: int):
        self.__horizonte = horizonte
        self.__capacidade = capacidade

        self.__taxaChegada = taxaChegada
        self.__taxaAtendimento = taxaAtendimento

        self.__clientes = []
        self.__clientesNoEstabelecimento = []

        self.__fila = []
        self.__tamanhoFila = 0

        self.__vetor_tempo = []
        self.__vetor_demoraFila = []
        self.__vetor_demoraAtendimento = []

        self.__mediaFila = 0
        self.__mediaTempo = 0
        self.__mediaDemoraFila = 0
        self.__mediaDemoraAtendimento = 0

    def statusMedias(self):
        print(f'''
############################################
################ Resultados ################
############################################

Tamanho médio da fila: {self.__mediaFila}
Tempo médio de clientes no estabelecimento: {self.__mediaTempo}
Tempo médio na fila: {self.__mediaDemoraFila}
Tempo médio no atendimento: {self.__mediaDemoraAtendimento}
''')

    def calcularMedias(self):
        fila_np = np.array(self.__fila)
        tempo_np = np.array(self.__vetor_tempo)
        demoraFila_mp = np.array(self.__vetor_demoraFila)
        demoraAtendimento_np = np.array(self.__vetor_demoraAtendimento)

        self.__mediaFila = round(fila_np.mean(), 2)
        self.__mediaTempo = round(tempo_np.mean(), 2)
        self.__mediaDemoraFila = round(demoraFila_mp.mean(), 2)
        self.__mediaDemoraAtendimento = round(demoraAtendimento_np.mean(), 2)

    def statusClientesAtendidos(self):
        print('''
############################################
############ Clientes Atendidos ############
############################################
''')
        for cliente in self.__clientes:
            cliente.status()
        
    def statusClientesNaoAtendidos(self):
        print('''
############################################
########## Clientes Não Atendidos ##########
############################################
''')
        for clienteNãoAtendido in self.__clientesNoEstabelecimento:
            clienteNãoAtendido.status()

    def fecharEstabelecimento(self):
        if len(self.__clientesNoEstabelecimento) != 0:
            for clienteNãoAtendido in self.__clientesNoEstabelecimento:
                self.__removerCliente(clienteNãoAtendido)

        for cliente in self.__clientes:
            self.__vetor_demoraFila.append(cliente.getDemoraNaFila())
            self.__vetor_demoraAtendimento.append(cliente.getDemoraNoAtendimento())
            self.__vetor_tempo.append(round((cliente.getDemoraNaFila() + cliente.getDemoraNoAtendimento()), 2))
    
    def saidaDoCliente(self, indice, tempoSaida):
        self.__clientes[indice].setTempoSaida(tempoSaida)
        self.__clientesNoEstabelecimento.remove(self.__clientes[indice])
        self.__reduzirFila()
    
    def calcularDemora(self, indice):
        self.__clientes[indice].calcularDemoraNaFila()
        self.__clientes[indice].calcularDemoraNoAtendimento()

# __ADICIONAR__
    def adicionarTempoDeAtendimento(self, indice, tempoAtendimento):
        self.__clientes[indice].setTempoAtendimento(tempoAtendimento)

    def adicionarCliente(self, novoCliente):
        self.__clientes.append(novoCliente)
        self.__clientesNoEstabelecimento.append(novoCliente)
    
    def __atualizarFila(self):
        self.__fila.append(self.__tamanhoFila)

    def aumentarFila(self):
        self.__tamanhoFila += 1
        self.__atualizarFila()

# __REMOVER__
    def __removerCliente(self, novoCliente):
        self.__clientes.remove(novoCliente)
    
    def removerClienteNoEstabelecimento(self, novoCliente):
        self.__clientesNoEstabelecimento.remove(novoCliente)

    def __reduzirFila(self):
        self.__tamanhoFila -= 1
        self.__atualizarFila()

# __GETTERS__
    def getHorizonte(self):
        return self.__horizonte
    
    def getCapacidade(self):
        return self.__capacidade

    def getTaxaChegada(self):
        return self.__taxaChegada
    
    def getTaxaAtendimento(self):
        return self.__taxaAtendimento

    def getClientes(self):
        return self.__clientes

    def getClientesNoEstabelecimento(self):
        return self.__clientesNoEstabelecimento
    
    def getFila(self):
        return self.__fila

    def get_vetor_tempo(self):
        return self.__vetor_tempo
    
    def get_vetor_demoraFila(self):
        return self.__vetor_demoraFila
    
    def get_vetor_demoraAtendimento(self):
        return self.__vetor_demoraAtendimento