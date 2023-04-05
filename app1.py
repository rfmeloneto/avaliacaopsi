import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pymongo
from dash import Input, Output, State
from datetime import datetime
import os
import requests

client = pymongo.MongoClient('mongodb+srv://EgpQLbxVVQvaK899:EgpQLbxVVQvaK899@cluster0.ftsc0.mongodb.net/?retryWrites=true&w=majority')
db = client['avaliacaoaplicada']
collection = db['autoavaliacao']
collection.create_index('nome', unique=True)

response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/TO/municipios')

if response.status_code == 200:
    data = response.json()
    municipio = [ i['nome'] for i in data]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])

app.layout = html.Div([
    
dbc.Container([
    dbc.Row([
        
        html.Label('Nome'),
        dbc.Input(id='input-nome', type='text'),

        html.Label('Cargo'),
        dbc.Input(id='input-cargo', type='text'),

        html.Label('Cidade'),
        dcc.Dropdown(municipio, id='input-cidade', className='text-black' , placeholder='Selecione a cidade', style={'backgroundColor': 'rgba(255, 255, 255, 0)'}),

        html.Label('Instituição'),
        dbc.Input(id='input-instituicao', type='text'),
    ]),

    html.Hr(),
    
    dbc.Row([
        html.H3('Escolha uma palavra em cada grupo de palavras, que melhor define você' , className='text-center mb-3'),
    ]),

    dbc.Row([
    
        dbc.Col([
            html.Div([html.Label('1. Grupo de Palavras')],className='text-center mb-3'),
            dbc.Card([
            dcc.RadioItems(
                id='q1',
                options=[
                    {'label': 'Perfeccionista', 'value': 'Analítico'},
                    {'label': 'Agressivo', 'value': 'Dominador'},
                    {'label': 'Prestativo', 'value': 'Estável'},
                    {'label': 'Emotivo', 'value': 'Influenciador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px',},
            )], className='mb-3 w-100  text-white shadow-lg'),

            html.Div([html.Label('2. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q2',
                options=[
                    {'label': 'Mediador', 'value': 'Estável'},
                    {'label': 'Detalhista', 'value': 'Analítico'},
                    {'label': 'Animado', 'value': 'Influenciador'},
                    {'label': 'Autoconfiante', 'value': 'Dominador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            )], className='mb-3 w-100 text-white shadow-lg'),

            html.Div([html.Label('3. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q3',
                options=[
                    {'label': 'Brincalhão', 'value': 'Influenciador'},
                    {'label': 'Dominador', 'value': 'Dominador'},
                    {'label': 'Paciente', 'value': 'Estável'},
                    {'label': 'Sistemático', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            )], className='mb-3 w-100 bg-info text-white shadow-lg'),

             html.Div([html.Label('4. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q4',
                options=[
                    {'label': 'Tranquilo', 'value': 'Estável'},
                    {'label': 'Sociável', 'value': 'Influenciador'},
                    {'label': 'Energético', 'value': 'Dominador'},
                    {'label': 'Metódico', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            )], className='mb-3 w-100 bg-warning text-white shadow-lg'),

              html.Div([html.Label('5. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q5',
                options=[
                    {'label': 'Independente', 'value': 'Dominador'},
                    {'label': 'Idealista', 'value': 'Influenciador'},
                    {'label': 'Amigável', 'value': 'Estável'},
                    {'label': 'Servidor', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            )], className='mb-3 w-100 bg-success text-white shadow-lg'),

             html.Div([html.Label('6. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q6',
                options=[
                    {'label': 'Exato', 'value': 'Analítico'},
                    {'label': 'Espirituoso', 'value': 'Influenciador'},
                    {'label': 'Satisfeito', 'value': 'Estável'},
                    {'label': 'Autosufificiente', 'value': 'Dominador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-danger text-white shadow-lg'),

             html.Div([html.Label('7. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q7',
                options=[
                    {'label': 'Organizado', 'value': 'Analítico'},
                    {'label': 'Seguro', 'value': 'Dominador'},
                    {'label': 'Tímido', 'value': 'Estável'},
                    {'label': 'Espontâneo', 'value': 'Influenciador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-warning text-white shadow-lg'),

             html.Div([html.Label('8. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q8',
                options=[
                    {'label': 'Previsível', 'value': 'Estável'},
                    {'label': 'Crítico', 'value': 'Analítico'},
                    {'label': 'Tagarela', 'value': 'Influenciador'},
                    {'label': 'Sarcástico', 'value': 'Dominador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-primary text-white shadow-lg'),

                    html.Div([html.Label('9. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q9',
                options=[
                    {'label': 'Preciso', 'value': 'Analítico'},
                    {'label': 'Comunicativo', 'value': 'Influenciador'},
                    {'label': 'Acolhedor', 'value': 'Estável'},
                    {'label': 'Destemido', 'value': 'Dominador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-info text-white shadow-lg'),

            html.Div([html.Label('10. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q10',
                options=[
                    {'label': 'Impaciente', 'value': 'Dominador'},
                    {'label': 'Bem-humorado', 'value': 'Influenciador'},
                    {'label': 'Generoso', 'value': 'Estável'},
                    {'label': 'Lógico', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-warning text-white shadow-lg'),

        ], sm=12, md=6, lg=4, xl=3),

        dbc.Col([

            html.Div([html.Label('11. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q11',
                options=[
                    {'label': 'Franco', 'value': 'Dominador'},
                    {'label': 'Ordeiro', 'value': 'Analítico'},
                    {'label': 'Otimista', 'value': 'Influenciador'},
                    {'label': 'Calmo', 'value': 'Estável'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-success text-white shadow-lg'),

            
        html.Div([html.Label('12. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q12',
                options=[
                    {'label': 'Procrastinador', 'value': 'Estável'},
                    {'label': 'Importuno', 'value': 'Influenciador'},
                    {'label': 'Impaciente', 'value': 'Dominador'},
                    {'label': 'Inseguro', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-danger text-white shadow-lg'),

            html.Div([html.Label('13. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q13',
                options=[
                    {'label': 'Incerto', 'value': 'Estável'},
                    {'label': 'Preocupado', 'value': 'Analítico'},
                    {'label': 'Discutidor', 'value': 'Dominador'},
                    {'label': 'Desorganizado', 'value': 'Influenciador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-primary text-white shadow-lg'),

        html.Div([html.Label('14. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q14',
                options=[
                    {'label': 'Perseverante', 'value': 'Estável'},
                    {'label': 'Mandão', 'value': 'Dominador'},
                    {'label': 'Pessimista', 'value': 'Analítico'},
                    {'label': 'Desorganizado', 'value': 'Influenciador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-warning text-white shadow-lg'),

        html.Div([html.Label('15. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q15',
                options=[
                    {'label': 'Indisciplinado', 'value': 'Influenciador'},
                    {'label': 'Questionador', 'value': 'Dominador'},
                    {'label': 'Insesível', 'value': 'Analítico'},
                    {'label': 'Reprimido', 'value': 'Estável'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-info text-white shadow-lg'),

             html.Div([html.Label('16. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q16',
                options=[
                    {'label': 'Lento', 'value': 'Estável'},
                    {'label': 'Direto', 'value': 'Dominador'},
                    {'label': 'Desobediente', 'value': 'Influenciador'},
                    {'label': 'Cético', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-warning text-white shadow-lg'),

             html.Div([html.Label('17. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q17',
                options=[
                    {'label': 'Tranquilo', 'value': 'Estável'},
                    {'label': 'Decidido', 'value': 'Dominador'},
                    {'label': 'Entusiasmado', 'value': 'Influenciador'},
                    {'label': 'Exigente', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-success text-white shadow-lg'),

            html.Div([html.Label('18. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q18',
                options=[
                    {'label': 'Paciente', 'value': 'Estável'},
                    {'label': 'Desligado', 'value': 'Influenciador'},
                    {'label': 'Intolerante', 'value': 'Dominador'},
                    {'label': 'Introvertido', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-primary text-white shadow-lg'),

            html.Div([html.Label('19. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q19',
                options=[
                    {'label': 'Pessimista', 'value': 'Analítico'},
                    {'label': 'Carismático', 'value': 'Influenciador'},
                    {'label': 'Reservado', 'value': 'Estável'},
                    {'label': 'Competitivo', 'value': 'Dominador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-warning text-white shadow-lg'),

            html.Div([html.Label('20. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q20',
                options=[
                    {'label': 'Complacente', 'value': 'Estável'},
                    {'label': 'Manipulador', 'value': 'Dominador'},
                    {'label': 'Resmungão', 'value': 'Analítico'},
                    {'label': 'Desordenado', 'value': 'Influenciador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-info text-white shadow-lg'),

        ], sm=12, md=6, lg=4, xl=3),
        dbc.Col([

            html.Div([html.Label('21. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q21',
                options=[
                    {'label': 'Brincalhão', 'value': 'Influenciador'},
                    {'label': 'Serene', 'value': 'Estável'},
                    {'label': 'Enérgico', 'value': 'Dominador'},
                    {'label': 'Autodisciplinado', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-warning text-white shadow-lg'),
            
            html.Div([html.Label('22. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q22',
                options=[
                    {'label': 'Vingativo', 'value': 'Dominador'},
                    {'label': 'Engraçado', 'value': 'Influenciador'},
                    {'label': 'Amigável', 'value': 'Estável'},
                    {'label': 'Disciplinado', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-success text-white shadow-lg'),

             html.Div([html.Label('23. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q23',
                options=[
                    {'label': 'Exigente', 'value': 'Dominador'},
                    {'label': 'Acomodado', 'value': 'Estável'},
                    {'label': 'Superficial', 'value': 'Influenciador'},
                    {'label': 'Centralizador', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-danger text-white shadow-lg'),

            html.Div([html.Label('24. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q24',
                options=[
                    {'label': 'Orgulhoso', 'value': 'Dominador'},
                    {'label': 'Aventureiro', 'value': 'Influenciador'},
                    {'label': 'Conformado', 'value': 'Estável'},
                    {'label': 'Cauteloso', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-primary text-white shadow-lg'),

            html.Div([html.Label('25. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q25',
                options=[
                    {'label': 'Cauteloso', 'value': 'Analítico'},
                    {'label': 'Passivo', 'value': 'Estável'},
                    {'label': 'Precipitado', 'value': 'Influenciador'},
                    {'label': 'Acelerado', 'value': 'Dominador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-warning text-white shadow-lg'),

            html.Div([html.Label('26. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q26',
                options=[
                    {'label': 'Teimoso', 'value': 'Dominador'},
                    {'label': 'Inconveniente', 'value': 'Influenciador'},
                    {'label': 'Minucioso', 'value': 'Analítico'},
                    {'label': 'Acomodado', 'value': 'Estável'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-info text-white shadow-lg'),

            html.Div([html.Label('27. Grupo de Palavras')],className='text-center mb-3'),

        dbc.Card([
            dcc.RadioItems(
                id='q27',
                options=[
                    {'label': 'Ambicioso', 'value': 'Dominador'},
                    {'label': 'Leal', 'value': 'Estável'},
                    {'label': 'Comunicativo', 'value': 'Influenciador'},
                    {'label': 'Discreto', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-success text-white shadow-lg'),

            html.Div([html.Label('28. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q28',
                options=[
                    {'label': 'Complacente', 'value': 'Estável'},
                    {'label': 'Frio', 'value': 'Dominador'},
                    {'label': 'Impulsivo', 'value': 'Influenciador'},
                    {'label': 'Controlador', 'value': 'Analítico'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-warning text-white shadow-lg'),

            html.Div([html.Label('29. Grupo de Palavras')],className='text-center mb-3'),
        dbc.Card([
            dcc.RadioItems(
                id='q29',
                options=[
                    {'label': 'Submisso', 'value': 'Estável'},
                    {'label': 'Negativo', 'value': 'Ananlítico'},
                    {'label': 'Ingênuo', 'value': 'Influenciador'},
                    {'label': 'Ousado', 'value': 'Dominador'},

                ],labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ), ], className='mb-3 w-100 bg-info text-white shadow-lg'),

        ],sm=12, md=6, lg=4, xl=3)
    ], className='d-flex justify-content-center'),


    ]),

html.Div(id='status'),

html.Div([dbc.Button('Enviar', id='enviar', className='m-3', size='lg')], className='d-flex justify-content-center'),

])


@app.callback(
    Output('status', 'children'),
    [Input('enviar', 'n_clicks')],
    [State('input-nome', 'value'),
     State('input-cargo', 'value'),
     State('input-cidade', 'value'),
     State('input-instituicao', 'value'),
     State('q1', 'value'),
     State('q2', 'value'),
     State('q3', 'value'),
     State('q4', 'value'),
     State('q5', 'value'),
     State('q6', 'value'),
     State('q7', 'value'),
     State('q8', 'value'),
     State('q9', 'value'),
     State('q10', 'value'),
     State('q11', 'value'),
     State('q12', 'value'),
     State('q13', 'value'),
     State('q14', 'value'),
     State('q15', 'value'),
     State('q16', 'value'),
     State('q17', 'value'),
     State('q18', 'value'),
     State('q19', 'value'),
     State('q20', 'value'),
     State('q21', 'value'),
     State('q22', 'value'),
     State('q23', 'value'),
     State('q24', 'value'),
     State('q25', 'value'),
     State('q26', 'value'),
     State('q27', 'value'),
     State('q28', 'value'),
     State('q29', 'value'),]
)
def save_data(n_clicks, nome, cargo, cidade, instituicao, q1, q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29):
    if n_clicks:
        instituicao = instituicao.upper()
        try:
            current_date = datetime.now().strftime('%d/%m/%Y')
            collection.insert_one({
                'nome': nome,
                'cargo': cargo,
                'cidade': cidade,
                'instituicao': instituicao,
                'q1': q1,
                'q2': q2,
                'q3': q3,
                'q4': q4,
                'q5': q5,
                'q6': q6,
                'q7': q7,
                'q8': q8,
                'q9': q9,
                'q10': q10,
                'q11': q11,
                'q12': q12,
                'q13': q13,
                'q14': q14,
                'q15': q15,
                'q16': q16,
                'q17': q17,
                'q18': q18,
                'q19': q19,
                'q20': q20,
                'q21': q21,
                'q22': q22,
                'q23': q23,
                'q24': q24,
                'q25': q26,
                'q27': q27,
                'q28': q28,
                'q29': q29,
                'data':current_date
            })
            return dbc.Alert('Dados salvos com sucesso!', color="primary")
        except pymongo.errors.DuplicateKeyError:
            return dbc.Alert('Usuário já respondeu o questionário!', color="danger")
    return ''
if __name__ == '__main__':
    app.run_server(debug=True)
