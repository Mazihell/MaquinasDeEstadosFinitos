# -*- coding: utf-8 -*-

#informe o nome do arquivo.txt que deseja efetuar a leitura#
arquivo = open('mef01.txt','r')
separandoLinhas = []
pertence = []
naoPertence = []

for linha in arquivo:
    separandoLinhas.append(linha.replace('\n',''))

del(separandoLinhas[0])

def inicio(valor):
    for linha in range(len(valor)):
        if valor[linha][0] == 'a':
            s0(separandoLinhas[linha],1)
        elif valor[linha][0] != 'a':
            naoPertence.append(valor[linha])

def s0(valor,posicao):
    while valor[posicao] == 'a' and posicao < len(valor) -1:
        posicao += 1
    if valor[posicao] == 'b' and posicao == len(valor) - 1:
        naoPertence.append(valor)
    elif valor[posicao] == 'b' and posicao < len(valor) - 1:
        posicao += 1
        s1(valor,posicao)
    elif valor[posicao] == 'a' and posicao == len(valor) -1:
        naoPertence.append(valor)    

def s1(valor,posicao):
    if valor[posicao] == 'b' and posicao < len(valor) -1:
        posicao += 1
        s2Final(valor,posicao)
    elif valor[posicao] == 'b' and posicao == len(valor) - 1:
        pertence.append(valor)
    elif valor[posicao] == 'a' and posicao < len(valor) - 1:
        naoPertence.append(valor)
    elif valor[posicao] == 'a' and posicao == len(valor) - 1:
        naoPertence.append(valor)

def s2Final(valor,posicao):
    while valor[posicao] == 'b' and posicao < len(valor) - 1:
        posicao += 1
    if valor[posicao] == 'b' and posicao == len(valor) - 1:
        pertence.append(valor)
    elif valor[posicao] == 'a' and posicao == len(valor) -1:
        naoPertence.append(valor)
    elif valor[posicao] == 'a' and posicao < len(valor) -1:
        posicao += 1
        s0(valor,posicao)

inicio(separandoLinhas)
for linha in range(len(pertence)):
    valor = pertence[linha]
    print(valor + ': ' + 'pertence')

for linha in range(len(naoPertence)):
    valor = naoPertence[linha]
    print(valor + ': ' + 'não pertence')

arquivo.close()

