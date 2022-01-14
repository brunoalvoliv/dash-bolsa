#Bibliotecas 

import pandas as pd
import numpy as np
import yfinance as yf
import datetime as datetime
import matplotlib.pyplot as plt

plt.style.use('classic')

#Escolhendo período de análise

inicio = datetime.datetime(2019, 1, 1)
fim = datetime.datetime(2021, 12, 31)

#Importando os dados

tickers = ['^BVSP']

dados = yf.download(tickers, start=inicio, end=fim)[['Close', 'Adj Close']]

#Visualização

plt.figure(figsize=(16, 8));
plt.title('Pontos: Ibovespa');
plt.plot(dados['Adj Close'], label='Pontos');
plt.xlabel('Data');
plt.ylabel('Pontos');
plt.legend();
plt.show()

print(dados.head())