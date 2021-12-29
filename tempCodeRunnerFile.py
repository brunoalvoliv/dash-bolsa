import pandas as pd

dataBase = []

for i in range(1, 13):
    cpas = pd.read_csv(f'/home/brunoalvoliver/Documentos/Programação/dash-bolsa/CPAs/CPA{i}.csv')
    dataBase.append(cpas)

print(dataBase[0])