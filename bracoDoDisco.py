from copy import deepcopy
import numpy as np
import sys
from copy import deepcopy

def firstComeFirstServed(passoApasso = False): #sempre pega o elemento da frente e subtrai com o anterior
    soma = 0
    if passoApasso:
        print(matriz,"\n")
    for i in range(1,len(matriz[1:])):
        if passoApasso:
            print("|"+str(matriz[i])+"-"+str(matriz[i+1])+"| =",abs(matriz[i] - matriz[i+1]))
        soma+= abs(matriz[i] - matriz[i+1])
    return soma

def shortestSeekTimeFirst(passoApasso = False):#sempre pega o elemento de menor distancia ao elemento atual
    soma = 0
    matAux = deepcopy(matriz[1:])

    indice = 0

    while(len(matAux)>1):
        arrayDif = [abs(matAux[i]-matAux[indice]) for i in range(len(matAux)) if i != indice] #array que apresenta o resultado de todas diferenças com o elemento atual
        if passoApasso:
            print(matAux)
            print("Elemento atual:",matAux[indice])
            print("Vetor de diferença:",arrayDif)
            print("Menor diferença:",min(arrayDif))
            print("Elemento de menor diferença:",arrayDif.index(min(arrayDif)),"\n\n")
        del(matAux[indice])
        indice = arrayDif.index(min(arrayDif))#indice do elemento de menor diferenca
        soma += min(arrayDif)

    return soma


def elevador(passoApasso = False):#SCAN
    soma = 0
    matAux = deepcopy(matriz[1:])

    elementoInicial = matAux[0]

    matAux = sorted(matAux) #ordena o vetor

    posDoElementoInicial = matAux.index(elementoInicial) #pos do elemento inicial no vetor ordenado

    voltaDisco = matAux[posDoElementoInicial:]#elementos p tras da pos atual(volta do disco)
    prossegueDisco = matAux[:posDoElementoInicial]#elementos p frente da pos atual()

    if passoApasso:
        print("Matriz inicial",matriz[1:])
        print("Vetor ordenado:",matAux)
        print("Mais externos:",voltaDisco)
        print("Mais internos",prossegueDisco)

    for i in range(len(voltaDisco)-1):
        if passoApasso:
            print("|"+str(voltaDisco[i])+"-"+str(voltaDisco[i+1])+"| =",abs(voltaDisco[i] - voltaDisco[i+1]))  
        soma += abs(voltaDisco[i+1]-voltaDisco[i])
    ultimoElementoVoltaDisco = voltaDisco[-1]

    prossegueDisco.append(ultimoElementoVoltaDisco)#pega o ultimo elemento do volta disco e coloca em prossegue

    prossegueDisco = prossegueDisco[::-1]#inverso do vetor

    for i in range(len(prossegueDisco)-1):
        if passoApasso:
            print("|"+str(prossegueDisco[i])+"-"+str(prossegueDisco[i+1])+"| =",abs(prossegueDisco[i] - prossegueDisco[i+1]))  
        soma += abs(prossegueDisco[i+1]-prossegueDisco[i])
    
    return soma



if __name__=="__main__":
    entrada = sys.argv[1]
    try:
        arquivo = open(entrada,'r')#abre o arquivo
    except:
        print("Arquivo não encontrado!")
        exit(0)

    linhas = arquivo.readlines()#le as linhas do arquivo e coloca na variavel linha

    arquivo.close()#fecha o arquivo

    matriz = []#lista que irá conter os elementos de entrada

    for linha in linhas:
        matriz.append(int(linha.replace("\n","")))
        
    flag = False
    for linha in matriz[1:]:
        if linha > matriz[0]:#verifica se tem algum elemento maior que o tam do disco
            flag = True
            break

    if not flag:# se todos elementos forem menor que o raio do disco
        FCFS = firstComeFirstServed(False)
        SSTF = shortestSeekTimeFirst(False)
        ELEVADOR = elevador(False)
        print("FCFS",FCFS)
        print("SSTF",SSTF)
        print("ELEVADOR",ELEVADOR)
