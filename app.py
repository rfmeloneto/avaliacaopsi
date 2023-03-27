import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pymongo
from dash import Input,Output,State


#client = pymongo.MongoClient()
#db = client['avaliacaoaplicada']
#collection = db['autoavaliacao']

app = dash.Dash(__name__ , external_stylesheets=[dbc.themes.SPACELAB])

app.layout = dbc.Container([
    dbc.Row([
    html.Label('Nome'),
    dcc.Input(id='input-nome', type='text'),
    
    html.Label('Cargo'),
    dcc.Input(id='input-cargo', type='text'),
    
    html.Label('Cidade'),
    dcc.Input(id='input-cidade', type='text'),
    ]),

    html.Hr(),

   dbc.Row([  
    html.H3('Escolha uma palavra em cada grupo de palavras, que melhor define você'),
    
    html.Label('1. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g1',
        options=[
            {'label': 'Perfeccionista', 'value': 'Analítico'},
            {'label': 'Agressivo', 'value': 'Dominador'},
            {'label': 'Prestativo', 'value': 'Estável'},
            {'label': 'Emotivo', 'value': 'Influenciador'},
            
        ]
    ),], className= 'mb-3 w-50 bg-secondary text-white'),

    html.Br(),

    html.Label('2. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g2',
        options=[
            {'label': 'Mediador', 'value': 'Estável'},
            {'label': 'Detalhista', 'value': 'Analítico'},
            {'label': 'Animado', 'value': 'Influenciador'},
            {'label': 'Autoconfiante', 'value': 'Dominador'},
            
        ],
    ),], className= 'mb-3 w-50 bg-primary text-white'),

    html.Br(),

    html.Label('3. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g3',
        options=[
            {'label': 'Brincalhão', 'value': 'Influenciador'},
            {'label': 'Dominador', 'value': 'Dominador'},
            {'label': 'Paciente', 'value': 'Estável'},
            {'label': 'Sistemático', 'value': 'Analítico'},
            
        ],
    ),], className= 'mb-3 w-50 bg-info text-white'),

    html.Br(),

    html.Label('4. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g4',
        options=[
            {'label': 'Tranquilo', 'value': 'Estável'},
            {'label': 'Sociável', 'value': 'Influenciador'},
            {'label': 'Energético', 'value': 'Dominador'},
            {'label': 'Metódico', 'value': 'Analítico'},
            
        ],
    ),], className= 'mb-3 w-50 bg-warning text-white'),

    html.Br(),

    html.Label('5. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g5',
        options=[
            {'label': 'Independente', 'value': 'Dominador'},
            {'label': 'Idealista', 'value': 'Influenciador'},
            {'label': 'Amigável', 'value': 'Estável'},
            {'label': 'Servidor', 'value': 'Analítico'},
            
        ],
    ),], className= 'mb-3 w-50 bg-success text-white'),

    html.Br(),

    html.Label('6. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g6',
        options=[
            {'label': 'Exato', 'value': 'Analítico'},
            {'label': 'Espirituoso', 'value': 'Influenciador'},
            {'label': 'Satisfeito', 'value': 'Estável'},
            {'label': 'Autosufificiente', 'value': 'Dominador'},
            
        ],
    ),], className= 'mb-3 w-50 bg-danger text-white'),

    html.Br(),

    html.Label('7. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g7',
        options=[
            {'label': 'Organizado', 'value': 'Analítico'},
            {'label': 'Seguro', 'value': 'Dominador'},
            {'label': 'Tímido', 'value': 'Estável'},
            {'label': 'Espontâneo', 'value': 'Influenciador'},
            
        ]
    ),], className= 'mb-3 w-50 bg-secondary text-white'),

    html.Br(),

    html.Label('8. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g2',
        options=[
            {'label': 'Mediador', 'value': 'Estável'},
            {'label': 'Detalhista', 'value': 'Analítico'},
            {'label': 'Animado', 'value': 'Influenciador'},
            {'label': 'Autoconfiante', 'value': 'Dominador'},
            
        ],
    ),], className= 'mb-3 w-50 bg-primary text-white'),

    html.Br(),

    html.Label('3. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g3',
        options=[
            {'label': 'Brincalhão', 'value': 'Influenciador'},
            {'label': 'Dominador', 'value': 'Dominador'},
            {'label': 'Paciente', 'value': 'Estável'},
            {'label': 'Sistemático', 'value': 'Analítico'},
            
        ],
    ),], className= 'mb-3 w-50 bg-info text-white'),

    html.Br(),

    html.Label('4. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g4',
        options=[
            {'label': 'Tranquilo', 'value': 'Estável'},
            {'label': 'Sociável', 'value': 'Influenciador'},
            {'label': 'Energético', 'value': 'Dominador'},
            {'label': 'Metódico', 'value': 'Analítico'},
            
        ],
    ),], className= 'mb-3 w-50 bg-warning text-white'),

    html.Br(),

    html.Label('5. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g5',
        options=[
            {'label': 'Independente', 'value': 'Dominador'},
            {'label': 'Idealista', 'value': 'Influenciador'},
            {'label': 'Amigável', 'value': 'Estável'},
            {'label': 'Servidor', 'value': 'Analítico'},
            
        ],
    ),], className= 'mb-3 w-50 bg-success text-white'),

    html.Br(),

    html.Label('6. Grupo de Palavras'),
    dbc.Card([
    dcc.RadioItems(
        id='g6',
        options=[
            {'label': 'Exato', 'value': 'Analítico'},
            {'label': 'Espirituoso', 'value': 'Influenciador'},
            {'label': 'Satisfeito', 'value': 'Estável'},
            {'label': 'Autosufificiente', 'value': 'Dominador'},
            
        ],
    ),], className= 'mb-3 w-50 bg-danger text-white'),

    html.Br(),

   ], className='d-flex justify-content-center'),
    
    
],)
if __name__ == '__main__':
    app.run_server(debug=True)
