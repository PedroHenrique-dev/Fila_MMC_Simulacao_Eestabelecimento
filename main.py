from estrutura import *

import numpy as np
import simpy as sp

horizonte = 100
capacidade = 1
taxaChegada = 2
taxaAtendimento = 3

_estabelecimento = Estabelecimento(horizonte, capacidade, taxaChegada, taxaAtendimento)

def geraChegadas(env):
    global _estabelecimento
    global servidorRes

    indiceClientes = 0
    while True:
        yield env.timeout(np.random.exponential(_estabelecimento.getTaxaAtendimento()))
        
        indiceClientes += 1
        _estabelecimento.aumentarFila()
        
        tempoChegada = round(env.now, 2)
        objCliente = Cliente(indiceClientes, tempoChegada)
        _estabelecimento.adicionarCliente(objCliente)
        
        env.process(atendimentoServidor(env, indiceClientes-1))

def atendimentoServidor(env, indice):
    global _estabelecimento
    global servidorRes

    request = servidorRes.request()
    yield request
    
    tempoAtendimento = round(env.now, 2)
    _estabelecimento.adicionarTempoDeAtendimento(indice, tempoAtendimento)
    
    yield env.timeout(np.random.exponential(_estabelecimento.getTaxaAtendimento()))
    
    tempoSaida = round(env.now, 2)
    _estabelecimento.saidaDoCliente(indice, tempoSaida)
    
    yield servidorRes.release(request)
    
    _estabelecimento.calcularDemora(indice)

env = sp.Environment() 
servidorRes = sp.Resource(env, capacity = _estabelecimento.getCapacidade())
env.process(geraChegadas(env))
env.run(until = _estabelecimento.getHorizonte())
_estabelecimento.fecharEstabelecimento()

_estabelecimento.statusClientesAtendidos()
if len(_estabelecimento.getClientesNoEstabelecimento()) != 0:
    _estabelecimento.statusClientesNaoAtendidos()

_estabelecimento.calcularMedias()
_estabelecimento.statusMedias()