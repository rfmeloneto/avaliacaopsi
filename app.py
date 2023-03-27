import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pymongo
from dash import Input, Output, State

# client = pymongo.MongoClient()
# db = client['avaliacaoaplicada']
# collection = db['autoavaliacao']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

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
            )], className='mb-3 w-50 bg-secondary text-white'),

        # html.Br(),

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
            )], className='mb-3 w-50 bg-primary text-white'),

        # html.Br(),

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
            )], className='mb-3 w-50 bg-info text-white'),

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
            )], className='mb-3 w-50 bg-warning text-white'),

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
            )], className='mb-3 w-50 bg-success text-white'),

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
            ), ], className='mb-3 w-50 bg-danger text-white'),

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
            ), ], className='mb-3 w-50 bg-secondary text-white'),

        html.Br(),

        html.Label('8. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g8',
                options=[
                    {'label': 'Previsível', 'value': 'Estável'},
                    {'label': 'Crítico', 'value': 'Analítico'},
                    {'label': 'Tagarela', 'value': 'Influenciador'},
                    {'label': 'Sarcástico', 'value': 'Dominador'},

                ],
            ), ], className='mb-3 w-50 bg-primary text-white'),

        html.Br(),

        html.Label('9. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g9',
                options=[
                    {'label': 'Preciso', 'value': 'Analítico'},
                    {'label': 'Comunicativo', 'value': 'Influenciador'},
                    {'label': 'Acolhedor', 'value': 'Estável'},
                    {'label': 'Destemido', 'value': 'Dominador'},

                ],
            ), ], className='mb-3 w-50 bg-info text-white'),

        html.Br(),

        html.Label('10. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g10',
                options=[
                    {'label': 'Impaciente', 'value': 'Dominador'},
                    {'label': 'Bem-humorado', 'value': 'Influenciador'},
                    {'label': 'Generoso', 'value': 'Estável'},
                    {'label': 'Lógico', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-warning text-white'),

        html.Br(),

        html.Label('11. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g11',
                options=[
                    {'label': 'Franco', 'value': 'Dominador'},
                    {'label': 'Ordeiro', 'value': 'Analítico'},
                    {'label': 'Otimista', 'value': 'Influenciador'},
                    {'label': 'Calmo', 'value': 'Estável'},

                ],
            ), ], className='mb-3 w-50 bg-success text-white'),

        html.Br(),

        html.Label('12. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g12',
                options=[
                    {'label': 'Procrastinador', 'value': 'Estável'},
                    {'label': 'Importuno', 'value': 'Influenciador'},
                    {'label': 'Impaciente', 'value': 'Dominador'},
                    {'label': 'Inseguro', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('13. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g13',
                options=[
                    {'label': 'Incerto', 'value': 'Estável'},
                    {'label': 'Preocupado', 'value': 'Analítico'},
                    {'label': 'Discutidor', 'value': 'Dominador'},
                    {'label': 'Desorganizado', 'value': 'Influenciador'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('14. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g14',
                options=[
                    {'label': 'Perseverante', 'value': 'Estável'},
                    {'label': 'Mandão', 'value': 'Dominador'},
                    {'label': 'Pessimista', 'value': 'Analítico'},
                    {'label': 'Desorganizado', 'value': 'Influenciador'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('15. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g15',
                options=[
                    {'label': 'Indisciplinado', 'value': 'Influenciador'},
                    {'label': 'Questionador', 'value': 'Dominador'},
                    {'label': 'Insesível', 'value': 'Analítico'},
                    {'label': 'Reprimido', 'value': 'Estável'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('16. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g16',
                options=[
                    {'label': 'Lento', 'value': 'Estável'},
                    {'label': 'Direto', 'value': 'Dominador'},
                    {'label': 'Desobediente', 'value': 'Influenciador'},
                    {'label': 'Cético', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('17. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g17',
                options=[
                    {'label': 'Tranquilo', 'value': 'Estável'},
                    {'label': 'Decidido', 'value': 'Dominador'},
                    {'label': 'Entusiasmado', 'value': 'Influenciador'},
                    {'label': 'Exigente', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('18. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g18',
                options=[
                    {'label': 'Paciente', 'value': 'Dominador'},
                    {'label': 'Desligado', 'value': 'Influenciador'},
                    {'label': 'Intolerante', 'value': 'Dominador'},
                    {'label': 'Introvertido', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('19. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g19',
                options=[
                    {'label': 'Pessimista', 'value': 'Analítico'},
                    {'label': 'Carismático', 'value': 'Influenciador'},
                    {'label': 'Reservado', 'value': 'Estável'},
                    {'label': 'Competitivo', 'value': 'Dominador'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('20. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g20',
                options=[
                    {'label': 'Complacente', 'value': 'Estável'},
                    {'label': 'Manipulador', 'value': 'Dominador'},
                    {'label': 'Resmungão', 'value': 'Analítico'},
                    {'label': 'Desordenado', 'value': 'Influenciador'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('21. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g21',
                options=[
                    {'label': 'Brincalhão', 'value': 'Influenciador'},
                    {'label': 'Serene', 'value': 'Estável'},
                    {'label': 'Enérgico', 'value': 'Dominador'},
                    {'label': 'Autodisciplinado', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('22. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g22',
                options=[
                    {'label': 'Vingativo', 'value': 'Dominador'},
                    {'label': 'Engraçado', 'value': 'Influenciador'},
                    {'label': 'Amigável', 'value': 'Estável'},
                    {'label': 'Disciplinado', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('23. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g23',
                options=[
                    {'label': 'Exigente', 'value': 'Dominador'},
                    {'label': 'Acomodado', 'value': 'Estável'},
                    {'label': 'Superficial', 'value': 'Influenciador'},
                    {'label': 'Centralizador', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('24. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g24',
                options=[
                    {'label': 'Orgulhoso', 'value': 'Dominador'},
                    {'label': 'Aventureiro', 'value': 'Influenciador'},
                    {'label': 'Conformado', 'value': 'Estável'},
                    {'label': 'Cauteloso', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('25. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g25',
                options=[
                    {'label': 'Cauteloso', 'value': 'Analítico'},
                    {'label': 'Passivo', 'value': 'Estável'},
                    {'label': 'Precipitado', 'value': 'Influenciador'},
                    {'label': 'Acelerado', 'value': 'Dominador'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('26. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g26',
                options=[
                    {'label': 'Teimoso', 'value': 'Dominador'},
                    {'label': 'Inconveniente', 'value': 'Influenciador'},
                    {'label': 'Minucioso', 'value': 'Analítico'},
                    {'label': 'Acomodado', 'value': 'Estável'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('27. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g27',
                options=[
                    {'label': 'Ambicioso', 'value': 'Dominador'},
                    {'label': 'Leal', 'value': 'Estável'},
                    {'label': 'Comunicativo', 'value': 'Influenciador'},
                    {'label': 'Discreto', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('28. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g28',
                options=[
                    {'label': 'Complacente', 'value': 'Estável'},
                    {'label': 'Frio', 'value': 'Dominador'},
                    {'label': 'Impulsivo', 'value': 'Influenciador'},
                    {'label': 'Controlador', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

        html.Label('29. Grupo de Palavras'),
        dbc.Card([
            dcc.RadioItems(
                id='g29',
                options=[
                    {'label': 'Submisso', 'value': 'Dominador'},
                    {'label': 'Negativo', 'value': 'Influenciador'},
                    {'label': 'Ingênuo', 'value': 'Dominador'},
                    {'label': 'Ousado', 'value': 'Analítico'},

                ],
            ), ], className='mb-3 w-50 bg-danger text-white'),

        html.Br(),

    ], className='d-flex justify-content-center'),

], )
if __name__ == '__main__':
    app.run_server(debug=True)
