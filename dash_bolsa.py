from dash import Dash
from dash_html_components import H1, H3, Div, P
from dash_core_components import Graph
import pandas as pd

dataBase = []

for i in range(1, 13):
    cpas = pd.read_csv(f'/home/brunoalvoliver/Documentos/Programação/dash-bolsa/CPAs/CPA{i}.csv', sep=';', encoding='ISO-8859-1', decimal=',')
    dataBase.append(cpas)

#print(dataBase[0])

external_stylesheets = [] #utilizar uma Tag style (mudar a aprẽncia do dash)

app = Dash(__name__, external_stylesheets=external_stylesheets) 

app.layout = Div(
    children = [
        H1('Dash Pró-reitoria (UFC)'),
        P('Esse Dash tem como objetivo proporcionar a visualização das pesquisas respondidas pelos discentes.'),
        H3('Gráfico Box-plot'),
        Graph(
            figure={
                'data': [
                    {'y': dataBase[0]['FEAAC'], 
                    'type': 'box',
                    'name': 'FEAAC'
                    },
                    {'y': dataBase[0]['LABOMAR'], 
                    'type': 'box',
                    'name': 'LABOMAR'
                    },
                    {'y': dataBase[0]['CH'], 
                    'type': 'box',
                    'name': 'CH'
                    },
                ],
                'layout': {

                }
            }
        )

    ]
)

app.run_server(debug=True)