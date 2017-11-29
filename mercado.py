# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:56:27 2017

@author: pc
"""
import pandas as pd

dados = pd.read_csv('mercado.csv', header = None)
transacoes = []
for i in range(0,10):
    transacoes.append([str(dados.values[i,j]) for j in range(0,4)])
    