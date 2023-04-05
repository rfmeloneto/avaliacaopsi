import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pymongo
from dash import Input, Output, State
import dash_table
import time

client = pymongo.MongoClient('mongodb+srv://EgpQLbxVVQvaK899:EgpQLbxVVQvaK899@cluster0.ftsc0.mongodb.net/?retryWrites=true&w=majority')
db = client['avaliacaoaplicada']
nomecol = db['autoavaliacao']
collection = db['grupo']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = html.Div([
    html.H1('Tabela de Nomes'),
    dash_table.DataTable(
        id='table',
        columns=[{'name': 'Nomes', 'id': 'nomes'},
                 {'name': 'CONTATO VISUAL', 'id': 'atributo1', 'editable': True },
                 {'name': 'EXPRESSÃO FACIAL', 'id': 'atributo2', 'editable': True},
                 {'name': 'SORRISO', 'id': 'atributo3', 'editable': True},
                 {'name': 'LATÊNCIA DE RESPOSTA', 'id': 'atributo4', 'editable': True},
                 {'name': 'GESTOS', 'id': 'atributo5', 'editable': True},
                 {'name': 'AUTOMANIPULAÇÃO', 'id': 'atributo6', 'editable': True},
                 {'name': 'POSTURA CORPORAL', 'id': 'atributo7', 'editable': True},
                 {'name': 'VOLUME DE VOZ', 'id': 'atributo8', 'editable': True},
                 {'name': 'ENTONAÇÃO', 'id': 'atributo9', 'editable': True},
                 {'name': 'FLUÊNCIA DA FALA', 'id': 'atributo10', 'editable': True},
                 {'name': 'SENSO DE HUMOR', 'id': 'atributo11', 'editable': True},
                 {'name': 'VERBALIZAÇÕES DERROTISTAS', 'id': 'atributo12', 'editable': True},
                 {'name': 'VERBALIZAÇÕES POSITIVAS', 'id': 'atributo13', 'editable': True},
                 {'name': 'HABILIDADE SOCIAL', 'id': 'atributo14', 'editable': True},
                 {'name': 'MOTIVAÇÃO PARA ATIVIDADE', 'id': 'atributo15', 'editable': True},
                 {'name': 'INICIATIVA NA EXECUÇÃO', 'id': 'atributo16', 'editable': True},
                 {'name': 'COMUNICAÇÃO FLUÍDA COM OS COLEGAS', 'id': 'atributo17', 'editable': True},
                 {'name': 'COMPORTAMENTO DE LIDERANÇA', 'id': 'atributo18', 'editable': True},
                 {'name': 'HABILIDADE DE INFLUENCIAR O GRUPO', 'id': 'atributo19', 'editable': True},
                 {'name': 'HABILIDADE TÉCNICA', 'id': 'atributo20', 'editable': True}],
        data=[],
        editable=True,
        persistence=True,
    ),
    dbc.Button('Salvar', id='save-button', n_clicks=0, className='m-3'),
    html.Div(id='output')
])

@app.callback(Output('table', 'data'),
              Input('table', 'data_timestamp'))
def update_table(data_timestamp):
    nomes = nomecol.find({}, {'_id': 0, 'nome': 1})
    return [{'nomes': nome['nome'], 'atributo1': '', 'atributo2': '', 'atributo3': '', 'atributo4': '', 'atributo5': '',
              'atributo6': '', 'atributo7': '', 'atributo8': '', 'atributo9': '', 'atributo10': '', 'atributo11': '',
                'atributo12': '', 'atributo13': '', 'atributo14': '', 'atributo15': '', 'atributo16': '', 'atributo17': '',
                  'atributo18': '', 'atributo19': '', 'atributo20': ''} for nome in nomes]


@app.callback(Output('output', 'children'),
              Input('save-button', 'n_clicks'),
              State('table', 'data'))
def save_data(n_clicks, data):
    if n_clicks > 0:
        for row in data:
            query = {'nome': row['nomes']}
            update = {'$set': {'atributo1': row['atributo1'],
                               'atributo2': row['atributo2'],
                               'atributo3': row['atributo3'],
                               'atributo4': row['atributo4'],
                               'atributo5': row['atributo5'],
                               'atributo6': row['atributo6'],
                               'atributo7': row['atributo7'],
                               'atributo8': row['atributo8'],
                               'atributo9': row['atributo9'],
                               'atributo10': row['atributo10'],
                               'atributo11': row['atributo11'],
                               'atributo12': row['atributo12'],
                               'atributo13': row['atributo13'],
                               'atributo14': row['atributo14'],
                               'atributo15': row['atributo15'],
                               'atributo16': row['atributo16'],
                               'atributo17': row['atributo17'],
                               'atributo18': row['atributo18'],
                               'atributo19': row['atributo19'],
                               'atributo20': row['atributo20']}}
            collection.update_one(query, update, upsert=True)
        return 'Dados salvos com sucesso!'

if __name__ == '__main__':
    app.run_server(debug=True)
