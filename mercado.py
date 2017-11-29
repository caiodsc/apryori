# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:56:27 2017

@author: pc
"""
import pandas as pd
import pprint 

pp = pprint.PrettyPrinter()

dados = pd.read_csv('mercado2.csv', header = None)
transacoes = []
for i in range(0,7501):
    transacoes.append([str(dados.values[i,j]) for j in range(0,20)])

from apryori import apriori
regras = apriori(transacoes, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

resultados = list(regras)
#resultados    

resultados2 = [list(x) for x in resultados]
#pp.pprint(resultados2)


resultadoFormatado = []
for j in range(0, 3):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])
resultadoFormatado    
pp.pprint(resultadoFormatado)
