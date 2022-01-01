import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

dataBase = []

for i in range(1, 13):
    cpas = pd.read_csv(f'/home/brunoalvoliver/Documentos/Programação/dash-bolsa/CPAs/CPA{i}.csv', sep=';', encoding='ISO-8859-1', decimal=',')
    dataBase.append(cpas)

app.layout = html.Div(children=[
    dcc.Markdown(
        '''
        # Pró-reitoria (UFC)

        '''
    ),
    dcc.Graph(
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
            ]
        }
    )
]

app.run_server(debug=True)