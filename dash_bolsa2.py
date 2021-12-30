from dash import Dash
from dash_html_components import H1, H3, Div, P
from dash_core_components import Graph, Dropdown, Checklist #Slider
from dash.dependencies import Input, Output

import pandas as pd
from random import randint

N = 20

database = {
    'index': list(range(N)),
    'maiores': [randint(1, 1000) for _ in range(N)],
    'menores': [randint(1, 1000) for _ in range(N)],
    'bebes': [randint(1, 1000) for _ in range(N)],
}

#print(dataBase[0])

external_stylesheets = [] #utilizar uma Tag style (mudar a aprẽncia do dash)

app = Dash(__name__, external_stylesheets=external_stylesheets) 

app.layout = Div(
    children = [
        H1('Evento X'),
        P('Pessoas que foram à semana da educação financeira'),
        H3('Escolha o tipo do gráfico:'),
        Dropdown(
            id='meu_dropdown',
            options=[
                {'label': 'Linha', 'value': 'line'},
                {'label': 'Barra', 'value': 'bar'},
            ],
            value='line'
        ),
        Checklist(
            id='meu_check_list',
            options=[
                {'label': 'Menores de idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'},
            ],
            value=['bebes']
        ),
        Graph(
            id='meu_grafico',
            config={'displayModeBar': False}, #tirar os ícones dos gráfico
        ),
    ],
)
   
@app.callback(
    Output('meu_grafico', 'figure'),
    [
        Input('meu_check_list', 'value'),
        Input('meu_dropdown', 'value'),
    ]
)
def my_callback(input_data, graph_type):
    grafico = {
        'data': []
    }
    for x in input_data:
        grafico['data'].append(
            {
                'y': database[x], 
                'x': database['index'],
                'name': x,
                'type': graph_type
            },
        )
    return grafico

app.run_server(debug=True)