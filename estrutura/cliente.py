class Cliente:
    def __init__(self, identificador: int, tempoChegada: int) -> None:
        self.__identificador = identificador
        self.__tempoChegada = tempoChegada
        self.__tempoAtendimento = 0
        self.__tempoSaida = 0
        self.__demoraNaFila = 0
        self.__demoraNoAtendimento = 0
    
    def calcularDemoraNaFila(self):
        self.__demoraNaFila = round((self.__tempoAtendimento - self.__tempoChegada), 2)
    
    def calcularDemoraNoAtendimento(self):
        self.__demoraNoAtendimento = round((self.__tempoSaida - self.__tempoAtendimento), 2)
        
    def status(self):
        print(f'''
>> Cliente {self.__identificador}

Chegada: {self.__tempoChegada}
Atendimento: {self.__tempoAtendimento}
Saida: {self.__tempoSaida}
Demora na fila: {self.__demoraNaFila}
Demora no atendimento: {self.__demoraNoAtendimento}
____________________________________________
              ''')

# __GETTERS__
    def getIdentificador(self):
        return self.__identificador

    def getTempoChegada(self):
        return self.__tempoChegada

    def getTempoAtendimento(self):
        return self.__tempoAtendimento

    def getTempoSaida(self):
        return self.__tempoSaida

    def getDemoraNaFila(self):
        return self.__demoraNaFila

    def getDemoraNoAtendimento(self):
        return self.__demoraNoAtendimento

# __SETTERS__
    def setIdentificador(self, identificador):
        self.__identificador = identificador

    def setTempoChegada(self, tempoChegada):
        self.__tempoChegada = tempoChegada

    def setTempoAtendimento(self, tempoAtendimento):
        self.__tempoAtendimento = tempoAtendimento

    def setTempoSaida(self, tempoSaida):
        self.__tempoSaida = tempoSaida

    def setDemoraNaFila(self, demoraNaFila):
        self.__demoraNaFila = demoraNaFila

    def setDemoraNoAtendimento(self, demoraNoAtendimento):
        self.__demoraNoAtendimento = demoraNoAtendimento