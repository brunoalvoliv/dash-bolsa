from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

dataBase = []

for i in range(1, 13):
    cpas = pd.read_csv(f'/home/brunoalvoliver/Documentos/Programação/dash-bolsa/CPAs/CPA{i}.csv', sep=';', encoding='ISO-8859-1', decimal=',')
    dataBase.append(cpas)

#print(dataBase[0])

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] #utilizar uma Tag style (mudar a aprẽncia do dash)

app = Dash(__name__) #, external_stylesheets=external_stylesheets

app.layout = html.Div([

        html.Div([
            html.H2(children='Pró-reitoria e Extensão (UFC)',
                    style={
                        'textAlign': 'center',
                    }
            ),
            #html.Img(src='/home/brunoalvoliver/Documentos/Programação/dash-bolsa/assets/image-removebg-preview (1).png')
            ], className='banner'),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[0][dataBase[0].columns[0]], 
                    'type': 'box',
                    'name': dataBase[0].columns[0]
                    },
                    {'y': dataBase[0][dataBase[0].columns[1]], 
                    'type': 'box',
                    'name': dataBase[0].columns[1]
                    },
                    {'y': dataBase[0][dataBase[0].columns[2]], 
                    'type': 'box',
                    'name': dataBase[0].columns[2]
                    },
                    {'y': dataBase[0][dataBase[0].columns[3]], 
                    'type': 'box',
                    'name': dataBase[0].columns[3]
                    },
                    {'y': dataBase[0][dataBase[0].columns[4]], 
                    'type': 'box',
                    'name': dataBase[0].columns[4]
                    },
                    {'y': dataBase[0][dataBase[0].columns[5]], 
                    'type': 'box',
                    'name': dataBase[0].columns[5]
                    },
                    {'y': dataBase[0][dataBase[0].columns[6]], 
                    'type': 'box',
                    'name': dataBase[0].columns[6]
                    },
                    {'y': dataBase[0][dataBase[0].columns[7]], 
                    'type': 'box',
                    'name': dataBase[0].columns[7]
                    },
                    {'y': dataBase[0][dataBase[0].columns[8]], 
                    'type': 'box',
                    'name': dataBase[0].columns[8]
                    },
                    {'y': dataBase[0][dataBase[0].columns[9]], 
                    'type': 'box',
                    'name': dataBase[0].columns[9]
                    },
                    {'y': dataBase[0][dataBase[0].columns[10]], 
                    'type': 'box',
                    'name': dataBase[0].columns[10]
                    },
                    {'y': dataBase[0][dataBase[0].columns[11]], 
                    'type': 'box',
                    'name': dataBase[0].columns[11]
                    },
                    {'y': dataBase[0][dataBase[0].columns[12]], 
                    'type': 'box',
                    'name': dataBase[0].columns[12]
                    },
                    {'y': dataBase[0][dataBase[0].columns[13]], 
                    'type': 'box',
                    'name': dataBase[0].columns[13]
                    },
                    {'y': dataBase[0][dataBase[0].columns[14]], 
                    'type': 'box',
                    'name': dataBase[0].columns[14]
                    },
                    {'y': dataBase[0][dataBase[0].columns[15]], 
                    'type': 'box',
                    'name': dataBase[0].columns[15]
                    },
                    {'y': dataBase[0][dataBase[0].columns[16]], 
                    'type': 'box',
                    'name': dataBase[0].columns[16]
                    },
                    {'y': dataBase[0][dataBase[0].columns[17]], 
                    'type': 'box',
                    'name': dataBase[0].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação de Turma pelo Discente - Nível Positivo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[1][dataBase[1].columns[0]], 
                    'type': 'box',
                    'name': dataBase[1].columns[0]
                    },
                    {'y': dataBase[1][dataBase[1].columns[1]], 
                    'type': 'box',
                    'name': dataBase[1].columns[1]
                    },
                    {'y': dataBase[1][dataBase[1].columns[2]], 
                    'type': 'box',
                    'name': dataBase[1].columns[2]
                    },
                    {'y': dataBase[1][dataBase[1].columns[3]], 
                    'type': 'box',
                    'name': dataBase[1].columns[3]
                    },
                    {'y': dataBase[1][dataBase[1].columns[4]], 
                    'type': 'box',
                    'name': dataBase[1].columns[4]
                    },
                    {'y': dataBase[1][dataBase[1].columns[5]], 
                    'type': 'box',
                    'name': dataBase[1].columns[5]
                    },
                    {'y': dataBase[1][dataBase[1].columns[6]], 
                    'type': 'box',
                    'name': dataBase[1].columns[6]
                    },
                    {'y': dataBase[1][dataBase[1].columns[7]], 
                    'type': 'box',
                    'name': dataBase[1].columns[7]
                    },
                    {'y': dataBase[1][dataBase[1].columns[8]], 
                    'type': 'box',
                    'name': dataBase[1].columns[8]
                    },
                    {'y': dataBase[1][dataBase[1].columns[9]], 
                    'type': 'box',
                    'name': dataBase[1].columns[9]
                    },
                    {'y': dataBase[1][dataBase[1].columns[10]], 
                    'type': 'box',
                    'name': dataBase[1].columns[10]
                    },
                    {'y': dataBase[1][dataBase[1].columns[11]], 
                    'type': 'box',
                    'name': dataBase[1].columns[11]
                    },
                    {'y': dataBase[1][dataBase[1].columns[12]], 
                    'type': 'box',
                    'name': dataBase[1].columns[12]
                    },
                    {'y': dataBase[1][dataBase[1].columns[13]], 
                    'type': 'box',
                    'name': dataBase[1].columns[13]
                    },
                    {'y': dataBase[1][dataBase[1].columns[14]], 
                    'type': 'box',
                    'name': dataBase[1].columns[14]
                    },
                    {'y': dataBase[1][dataBase[1].columns[15]], 
                    'type': 'box',
                    'name': dataBase[1].columns[15]
                    },
                    {'y': dataBase[1][dataBase[1].columns[16]], 
                    'type': 'box',
                    'name': dataBase[1].columns[16]
                    },
                    {'y': dataBase[1][dataBase[1].columns[17]], 
                    'type': 'box',
                    'name': dataBase[1].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação de Turma pelo Discente - Nível Negativo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[2][dataBase[2].columns[0]], 
                    'type': 'box',
                    'name': dataBase[2].columns[0]
                    },
                    {'y': dataBase[2][dataBase[2].columns[1]], 
                    'type': 'box',
                    'name': dataBase[2].columns[1]
                    },
                    {'y': dataBase[2][dataBase[2].columns[2]], 
                    'type': 'box',
                    'name': dataBase[2].columns[2]
                    },
                    {'y': dataBase[2][dataBase[2].columns[3]], 
                    'type': 'box',
                    'name': dataBase[2].columns[3]
                    },
                    {'y': dataBase[2][dataBase[2].columns[4]], 
                    'type': 'box',
                    'name': dataBase[2].columns[4]
                    },
                    {'y': dataBase[2][dataBase[2].columns[5]], 
                    'type': 'box',
                    'name': dataBase[2].columns[5]
                    },
                    {'y': dataBase[2][dataBase[2].columns[6]], 
                    'type': 'box',
                    'name': dataBase[2].columns[6]
                    },
                    {'y': dataBase[2][dataBase[2].columns[7]], 
                    'type': 'box',
                    'name': dataBase[2].columns[7]
                    },
                    {'y': dataBase[2][dataBase[2].columns[8]], 
                    'type': 'box',
                    'name': dataBase[2].columns[8]
                    },
                    {'y': dataBase[2][dataBase[2].columns[9]], 
                    'type': 'box',
                    'name': dataBase[2].columns[9]
                    },
                    {'y': dataBase[2][dataBase[2].columns[10]], 
                    'type': 'box',
                    'name': dataBase[2].columns[10]
                    },
                    {'y': dataBase[2][dataBase[2].columns[11]], 
                    'type': 'box',
                    'name': dataBase[2].columns[11]
                    },
                    {'y': dataBase[2][dataBase[2].columns[12]], 
                    'type': 'box',
                    'name': dataBase[2].columns[12]
                    },
                    {'y': dataBase[2][dataBase[2].columns[13]], 
                    'type': 'box',
                    'name': dataBase[2].columns[13]
                    },
                    {'y': dataBase[2][dataBase[2].columns[14]], 
                    'type': 'box',
                    'name': dataBase[2].columns[14]
                    },
                    {'y': dataBase[2][dataBase[2].columns[15]], 
                    'type': 'box',
                    'name': dataBase[2].columns[15]
                    },
                    {'y': dataBase[2][dataBase[2].columns[16]], 
                    'type': 'box',
                    'name': dataBase[2].columns[16]
                    },
                    {'y': dataBase[2][dataBase[2].columns[17]], 
                    'type': 'box',
                    'name': dataBase[2].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação de Turma pelo Docente - Nível Positivo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[3][dataBase[3].columns[0]], 
                    'type': 'box',
                    'name': dataBase[3].columns[0]
                    },
                    {'y': dataBase[3][dataBase[3].columns[1]], 
                    'type': 'box',
                    'name': dataBase[3].columns[1]
                    },
                    {'y': dataBase[3][dataBase[3].columns[2]], 
                    'type': 'box',
                    'name': dataBase[3].columns[2]
                    },
                    {'y': dataBase[3][dataBase[3].columns[3]], 
                    'type': 'box',
                    'name': dataBase[3].columns[3]
                    },
                    {'y': dataBase[3][dataBase[3].columns[4]], 
                    'type': 'box',
                    'name': dataBase[3].columns[4]
                    },
                    {'y': dataBase[3][dataBase[3].columns[5]], 
                    'type': 'box',
                    'name': dataBase[3].columns[5]
                    },
                    {'y': dataBase[3][dataBase[3].columns[6]], 
                    'type': 'box',
                    'name': dataBase[3].columns[6]
                    },
                    {'y': dataBase[3][dataBase[3].columns[7]], 
                    'type': 'box',
                    'name': dataBase[3].columns[7]
                    },
                    {'y': dataBase[3][dataBase[3].columns[8]], 
                    'type': 'box',
                    'name': dataBase[3].columns[8]
                    },
                    {'y': dataBase[3][dataBase[3].columns[9]], 
                    'type': 'box',
                    'name': dataBase[3].columns[9]
                    },
                    {'y': dataBase[3][dataBase[3].columns[10]], 
                    'type': 'box',
                    'name': dataBase[3].columns[10]
                    },
                    {'y': dataBase[3][dataBase[3].columns[11]], 
                    'type': 'box',
                    'name': dataBase[3].columns[11]
                    },
                    {'y': dataBase[3][dataBase[3].columns[12]], 
                    'type': 'box',
                    'name': dataBase[3].columns[12]
                    },
                    {'y': dataBase[3][dataBase[3].columns[13]], 
                    'type': 'box',
                    'name': dataBase[3].columns[13]
                    },
                    {'y': dataBase[3][dataBase[3].columns[14]], 
                    'type': 'box',
                    'name': dataBase[3].columns[14]
                    },
                    {'y': dataBase[3][dataBase[3].columns[15]], 
                    'type': 'box',
                    'name': dataBase[3].columns[15]
                    },
                    {'y': dataBase[3][dataBase[3].columns[16]], 
                    'type': 'box',
                    'name': dataBase[3].columns[16]
                    },
                    {'y': dataBase[3][dataBase[3].columns[17]], 
                    'type': 'box',
                    'name': dataBase[3].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação de Turma pelo Docente - Nível Negativo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[4][dataBase[4].columns[0]], 
                    'type': 'box',
                    'name': dataBase[4].columns[0]
                    },
                    {'y': dataBase[4][dataBase[4].columns[1]], 
                    'type': 'box',
                    'name': dataBase[4].columns[1]
                    },
                    {'y': dataBase[4][dataBase[4].columns[2]], 
                    'type': 'box',
                    'name': dataBase[4].columns[2]
                    },
                    {'y': dataBase[4][dataBase[4].columns[3]], 
                    'type': 'box',
                    'name': dataBase[4].columns[3]
                    },
                    {'y': dataBase[4][dataBase[4].columns[4]], 
                    'type': 'box',
                    'name': dataBase[4].columns[4]
                    },
                    {'y': dataBase[4][dataBase[4].columns[5]], 
                    'type': 'box',
                    'name': dataBase[4].columns[5]
                    },
                    {'y': dataBase[4][dataBase[4].columns[6]], 
                    'type': 'box',
                    'name': dataBase[4].columns[6]
                    },
                    {'y': dataBase[4][dataBase[4].columns[7]], 
                    'type': 'box',
                    'name': dataBase[4].columns[7]
                    },
                    {'y': dataBase[4][dataBase[4].columns[8]], 
                    'type': 'box',
                    'name': dataBase[4].columns[8]
                    },
                    {'y': dataBase[4][dataBase[4].columns[9]], 
                    'type': 'box',
                    'name': dataBase[4].columns[9]
                    },
                    {'y': dataBase[4][dataBase[4].columns[10]], 
                    'type': 'box',
                    'name': dataBase[4].columns[10]
                    },
                    {'y': dataBase[4][dataBase[4].columns[11]], 
                    'type': 'box',
                    'name': dataBase[4].columns[11]
                    },
                    {'y': dataBase[4][dataBase[4].columns[12]], 
                    'type': 'box',
                    'name': dataBase[4].columns[12]
                    },
                    {'y': dataBase[4][dataBase[4].columns[13]], 
                    'type': 'box',
                    'name': dataBase[4].columns[13]
                    },
                    {'y': dataBase[4][dataBase[4].columns[14]], 
                    'type': 'box',
                    'name': dataBase[4].columns[14]
                    },
                    {'y': dataBase[4][dataBase[4].columns[15]], 
                    'type': 'box',
                    'name': dataBase[4].columns[15]
                    },
                    {'y': dataBase[4][dataBase[4].columns[16]], 
                    'type': 'box',
                    'name': dataBase[4].columns[16]
                    },
                    {'y': dataBase[4][dataBase[4].columns[17]], 
                    'type': 'box',
                    'name': dataBase[4].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação da Coord. Curso/Discente - Nível Positivo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[5][dataBase[5].columns[0]], 
                    'type': 'box',
                    'name': dataBase[5].columns[0]
                    },
                    {'y': dataBase[5][dataBase[5].columns[1]], 
                    'type': 'box',
                    'name': dataBase[5].columns[1]
                    },
                    {'y': dataBase[5][dataBase[5].columns[2]], 
                    'type': 'box',
                    'name': dataBase[5].columns[2]
                    },
                    {'y': dataBase[5][dataBase[5].columns[3]], 
                    'type': 'box',
                    'name': dataBase[5].columns[3]
                    },
                    {'y': dataBase[5][dataBase[5].columns[4]], 
                    'type': 'box',
                    'name': dataBase[5].columns[4]
                    },
                    {'y': dataBase[5][dataBase[5].columns[5]], 
                    'type': 'box',
                    'name': dataBase[5].columns[5]
                    },
                    {'y': dataBase[5][dataBase[5].columns[6]], 
                    'type': 'box',
                    'name': dataBase[5].columns[6]
                    },
                    {'y': dataBase[5][dataBase[5].columns[7]], 
                    'type': 'box',
                    'name': dataBase[5].columns[7]
                    },
                    {'y': dataBase[5][dataBase[5].columns[8]], 
                    'type': 'box',
                    'name': dataBase[5].columns[8]
                    },
                    {'y': dataBase[5][dataBase[5].columns[9]], 
                    'type': 'box',
                    'name': dataBase[5].columns[9]
                    },
                    {'y': dataBase[5][dataBase[5].columns[10]], 
                    'type': 'box',
                    'name': dataBase[5].columns[10]
                    },
                    {'y': dataBase[5][dataBase[5].columns[11]], 
                    'type': 'box',
                    'name': dataBase[5].columns[11]
                    },
                    {'y': dataBase[5][dataBase[5].columns[12]], 
                    'type': 'box',
                    'name': dataBase[5].columns[12]
                    },
                    {'y': dataBase[5][dataBase[5].columns[13]], 
                    'type': 'box',
                    'name': dataBase[5].columns[13]
                    },
                    {'y': dataBase[5][dataBase[5].columns[14]], 
                    'type': 'box',
                    'name': dataBase[5].columns[14]
                    },
                    {'y': dataBase[5][dataBase[5].columns[15]], 
                    'type': 'box',
                    'name': dataBase[5].columns[15]
                    },
                    {'y': dataBase[5][dataBase[5].columns[16]], 
                    'type': 'box',
                    'name': dataBase[5].columns[16]
                    },
                    {'y': dataBase[5][dataBase[5].columns[17]], 
                    'type': 'box',
                    'name': dataBase[5].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação da Coord. Curso/Discente - Nível Negativo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[7][dataBase[7].columns[0]], 
                    'type': 'box',
                    'name': dataBase[7].columns[0]
                    },
                    {'y': dataBase[7][dataBase[7].columns[1]], 
                    'type': 'box',
                    'name': dataBase[7].columns[1]
                    },
                    {'y': dataBase[7][dataBase[7].columns[2]], 
                    'type': 'box',
                    'name': dataBase[7].columns[2]
                    },
                    {'y': dataBase[7][dataBase[7].columns[3]], 
                    'type': 'box',
                    'name': dataBase[7].columns[3]
                    },
                    {'y': dataBase[7][dataBase[7].columns[4]], 
                    'type': 'box',
                    'name': dataBase[7].columns[4]
                    },
                    {'y': dataBase[7][dataBase[7].columns[5]], 
                    'type': 'box',
                    'name': dataBase[7].columns[5]
                    },
                    {'y': dataBase[7][dataBase[7].columns[6]], 
                    'type': 'box',
                    'name': dataBase[7].columns[6]
                    },
                    {'y': dataBase[7][dataBase[7].columns[7]], 
                    'type': 'box',
                    'name': dataBase[7].columns[7]
                    },
                    {'y': dataBase[7][dataBase[7].columns[8]], 
                    'type': 'box',
                    'name': dataBase[7].columns[8]
                    },
                    {'y': dataBase[7][dataBase[7].columns[9]], 
                    'type': 'box',
                    'name': dataBase[7].columns[9]
                    },
                    {'y': dataBase[7][dataBase[7].columns[10]], 
                    'type': 'box',
                    'name': dataBase[7].columns[10]
                    },
                    {'y': dataBase[7][dataBase[7].columns[11]], 
                    'type': 'box',
                    'name': dataBase[7].columns[11]
                    },
                    {'y': dataBase[7][dataBase[7].columns[12]], 
                    'type': 'box',
                    'name': dataBase[7].columns[12]
                    },
                    {'y': dataBase[7][dataBase[7].columns[13]], 
                    'type': 'box',
                    'name': dataBase[7].columns[13]
                    },
                    {'y': dataBase[7][dataBase[7].columns[14]], 
                    'type': 'box',
                    'name': dataBase[7].columns[14]
                    },
                    {'y': dataBase[7][dataBase[7].columns[15]], 
                    'type': 'box',
                    'name': dataBase[7].columns[15]
                    },
                    {'y': dataBase[7][dataBase[7].columns[16]], 
                    'type': 'box',
                    'name': dataBase[7].columns[16]
                    },
                    {'y': dataBase[7][dataBase[7].columns[17]], 
                    'type': 'box',
                    'name': dataBase[7].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação do Desempenho Docente/Discente',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[8][dataBase[8].columns[0]], 
                    'type': 'box',
                    'name': dataBase[8].columns[0]
                    },
                    {'y': dataBase[8][dataBase[8].columns[1]], 
                    'type': 'box',
                    'name': dataBase[8].columns[1]
                    },
                    {'y': dataBase[8][dataBase[8].columns[2]], 
                    'type': 'box',
                    'name': dataBase[8].columns[2]
                    },
                    {'y': dataBase[8][dataBase[8].columns[3]], 
                    'type': 'box',
                    'name': dataBase[8].columns[3]
                    },
                    {'y': dataBase[8][dataBase[8].columns[4]], 
                    'type': 'box',
                    'name': dataBase[8].columns[4]
                    },
                    {'y': dataBase[8][dataBase[8].columns[5]], 
                    'type': 'box',
                    'name': dataBase[8].columns[5]
                    },
                    {'y': dataBase[8][dataBase[8].columns[6]], 
                    'type': 'box',
                    'name': dataBase[8].columns[6]
                    },
                    {'y': dataBase[8][dataBase[8].columns[7]], 
                    'type': 'box',
                    'name': dataBase[8].columns[7]
                    },
                    {'y': dataBase[8][dataBase[8].columns[8]], 
                    'type': 'box',
                    'name': dataBase[8].columns[8]
                    },
                    {'y': dataBase[8][dataBase[8].columns[9]], 
                    'type': 'box',
                    'name': dataBase[8].columns[9]
                    },
                    {'y': dataBase[8][dataBase[8].columns[10]], 
                    'type': 'box',
                    'name': dataBase[8].columns[10]
                    },
                    {'y': dataBase[8][dataBase[8].columns[11]], 
                    'type': 'box',
                    'name': dataBase[8].columns[11]
                    },
                    {'y': dataBase[8][dataBase[8].columns[12]], 
                    'type': 'box',
                    'name': dataBase[8].columns[12]
                    },
                    {'y': dataBase[8][dataBase[8].columns[13]], 
                    'type': 'box',
                    'name': dataBase[8].columns[13]
                    },
                    {'y': dataBase[8][dataBase[8].columns[14]], 
                    'type': 'box',
                    'name': dataBase[8].columns[14]
                    },
                    {'y': dataBase[8][dataBase[8].columns[15]], 
                    'type': 'box',
                    'name': dataBase[8].columns[15]
                    },
                    {'y': dataBase[8][dataBase[8].columns[16]], 
                    'type': 'box',
                    'name': dataBase[8].columns[16]
                    },
                    {'y': dataBase[8][dataBase[8].columns[17]], 
                    'type': 'box',
                    'name': dataBase[8].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação da Infraest./Discente - Nível Positivo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[9][dataBase[9].columns[0]], 
                    'type': 'box',
                    'name': dataBase[9].columns[0]
                    },
                    {'y': dataBase[9][dataBase[9].columns[1]], 
                    'type': 'box',
                    'name': dataBase[9].columns[1]
                    },
                    {'y': dataBase[9][dataBase[9].columns[2]], 
                    'type': 'box',
                    'name': dataBase[9].columns[2]
                    },
                    {'y': dataBase[9][dataBase[9].columns[3]], 
                    'type': 'box',
                    'name': dataBase[9].columns[3]
                    },
                    {'y': dataBase[9][dataBase[9].columns[4]], 
                    'type': 'box',
                    'name': dataBase[9].columns[4]
                    },
                    {'y': dataBase[9][dataBase[9].columns[5]], 
                    'type': 'box',
                    'name': dataBase[9].columns[5]
                    },
                    {'y': dataBase[9][dataBase[9].columns[6]], 
                    'type': 'box',
                    'name': dataBase[9].columns[6]
                    },
                    {'y': dataBase[9][dataBase[9].columns[7]], 
                    'type': 'box',
                    'name': dataBase[9].columns[7]
                    },
                    {'y': dataBase[9][dataBase[9].columns[8]], 
                    'type': 'box',
                    'name': dataBase[9].columns[8]
                    },
                    {'y': dataBase[9][dataBase[9].columns[9]], 
                    'type': 'box',
                    'name': dataBase[9].columns[9]
                    },
                    {'y': dataBase[9][dataBase[9].columns[10]], 
                    'type': 'box',
                    'name': dataBase[9].columns[10]
                    },
                    {'y': dataBase[9][dataBase[9].columns[11]], 
                    'type': 'box',
                    'name': dataBase[9].columns[11]
                    },
                    {'y': dataBase[9][dataBase[9].columns[12]], 
                    'type': 'box',
                    'name': dataBase[9].columns[12]
                    },
                    {'y': dataBase[9][dataBase[9].columns[13]], 
                    'type': 'box',
                    'name': dataBase[9].columns[13]
                    },
                    {'y': dataBase[9][dataBase[9].columns[14]], 
                    'type': 'box',
                    'name': dataBase[9].columns[14]
                    },
                    {'y': dataBase[9][dataBase[9].columns[15]], 
                    'type': 'box',
                    'name': dataBase[9].columns[15]
                    },
                    {'y': dataBase[9][dataBase[9].columns[16]], 
                    'type': 'box',
                    'name': dataBase[9].columns[16]
                    },
                    {'y': dataBase[9][dataBase[9].columns[17]], 
                    'type': 'box',
                    'name': dataBase[9].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação da Infraest./Discente - Nível Negativo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[10][dataBase[10].columns[0]], 
                    'type': 'box',
                    'name': dataBase[10].columns[0]
                    },
                    {'y': dataBase[10][dataBase[10].columns[1]], 
                    'type': 'box',
                    'name': dataBase[10].columns[1]
                    },
                    {'y': dataBase[10][dataBase[10].columns[2]], 
                    'type': 'box',
                    'name': dataBase[10].columns[2]
                    },
                    {'y': dataBase[10][dataBase[10].columns[3]], 
                    'type': 'box',
                    'name': dataBase[10].columns[3]
                    },
                    {'y': dataBase[10][dataBase[10].columns[4]], 
                    'type': 'box',
                    'name': dataBase[10].columns[4]
                    },
                    {'y': dataBase[10][dataBase[10].columns[5]], 
                    'type': 'box',
                    'name': dataBase[10].columns[5]
                    },
                    {'y': dataBase[10][dataBase[10].columns[6]], 
                    'type': 'box',
                    'name': dataBase[10].columns[6]
                    },
                    {'y': dataBase[10][dataBase[10].columns[7]], 
                    'type': 'box',
                    'name': dataBase[10].columns[7]
                    },
                    {'y': dataBase[10][dataBase[10].columns[8]], 
                    'type': 'box',
                    'name': dataBase[10].columns[8]
                    },
                    {'y': dataBase[10][dataBase[10].columns[9]], 
                    'type': 'box',
                    'name': dataBase[10].columns[9]
                    },
                    {'y': dataBase[10][dataBase[10].columns[10]], 
                    'type': 'box',
                    'name': dataBase[10].columns[10]
                    },
                    {'y': dataBase[10][dataBase[10].columns[11]], 
                    'type': 'box',
                    'name': dataBase[10].columns[11]
                    },
                    {'y': dataBase[10][dataBase[10].columns[12]], 
                    'type': 'box',
                    'name': dataBase[10].columns[12]
                    },
                    {'y': dataBase[10][dataBase[10].columns[13]], 
                    'type': 'box',
                    'name': dataBase[10].columns[13]
                    },
                    {'y': dataBase[10][dataBase[10].columns[14]], 
                    'type': 'box',
                    'name': dataBase[10].columns[14]
                    },
                    {'y': dataBase[10][dataBase[10].columns[15]], 
                    'type': 'box',
                    'name': dataBase[10].columns[15]
                    },
                    {'y': dataBase[10][dataBase[10].columns[16]], 
                    'type': 'box',
                    'name': dataBase[10].columns[16]
                    },
                    {'y': dataBase[10][dataBase[10].columns[17]], 
                    'type': 'box',
                    'name': dataBase[10].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação da Infraest./Docente - Nível Positivo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
        html.Hr(),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {'y': dataBase[11][dataBase[11].columns[0]], 
                    'type': 'box',
                    'name': dataBase[11].columns[0]
                    },
                    {'y': dataBase[11][dataBase[11].columns[1]], 
                    'type': 'box',
                    'name': dataBase[11].columns[1]
                    },
                    {'y': dataBase[11][dataBase[11].columns[2]], 
                    'type': 'box',
                    'name': dataBase[11].columns[2]
                    },
                    {'y': dataBase[11][dataBase[11].columns[3]], 
                    'type': 'box',
                    'name': dataBase[11].columns[3]
                    },
                    {'y': dataBase[11][dataBase[11].columns[4]], 
                    'type': 'box',
                    'name': dataBase[11].columns[4]
                    },
                    {'y': dataBase[11][dataBase[11].columns[5]], 
                    'type': 'box',
                    'name': dataBase[11].columns[5]
                    },
                    {'y': dataBase[11][dataBase[11].columns[6]], 
                    'type': 'box',
                    'name': dataBase[11].columns[6]
                    },
                    {'y': dataBase[11][dataBase[11].columns[7]], 
                    'type': 'box',
                    'name': dataBase[11].columns[7]
                    },
                    {'y': dataBase[11][dataBase[11].columns[8]], 
                    'type': 'box',
                    'name': dataBase[11].columns[8]
                    },
                    {'y': dataBase[11][dataBase[11].columns[9]], 
                    'type': 'box',
                    'name': dataBase[11].columns[9]
                    },
                    {'y': dataBase[11][dataBase[11].columns[10]], 
                    'type': 'box',
                    'name': dataBase[11].columns[10]
                    },
                    {'y': dataBase[11][dataBase[11].columns[11]], 
                    'type': 'box',
                    'name': dataBase[11].columns[11]
                    },
                    {'y': dataBase[11][dataBase[11].columns[12]], 
                    'type': 'box',
                    'name': dataBase[11].columns[12]
                    },
                    {'y': dataBase[11][dataBase[11].columns[13]], 
                    'type': 'box',
                    'name': dataBase[11].columns[13]
                    },
                    {'y': dataBase[11][dataBase[11].columns[14]], 
                    'type': 'box',
                    'name': dataBase[11].columns[14]
                    },
                    {'y': dataBase[11][dataBase[11].columns[15]], 
                    'type': 'box',
                    'name': dataBase[11].columns[15]
                    },
                    {'y': dataBase[11][dataBase[11].columns[16]], 
                    'type': 'box',
                    'name': dataBase[11].columns[16]
                    },
                    {'y': dataBase[11][dataBase[11].columns[17]], 
                    'type': 'box',
                    'name': dataBase[11].columns[17]
                    },
                ],
                'layout': {
                    'title': 'Avaliação da Infraest./Docente - Nível Negativo',
                    'paper_bgcolor': 'E3E6E6',
                }
            }
        ),
    ]
)

app.run_server(debug=True)