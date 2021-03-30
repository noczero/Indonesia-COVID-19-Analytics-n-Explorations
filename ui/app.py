import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from src.utils import load_data_postprocessing

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}], title="Indonesia COVID-19")

# load post_processing data
print("Load data...")
df_categories, df_times = load_data_postprocessing()

print("Config Layout...")
# -- START LAYOUT
app.layout = html.Div([
    # HEADER
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('covid-19-logo.png'),
                     id='corona-image',
                     style={
                         "height": "60px",
                         "width": "auto",
                         "margin-bottom": "25px",
                     },
                     ),
            html.Img(src=app.get_asset_url('indonesia-flag.png'),
                     id='id-flag',
                     style={
                         "height": "60px",
                         "width": "auto",
                         "margin-bottom": "25px",
                     },
                     )
        ],
            className="one-third column",
            style={
                "padding-top": "30px"
            }
        ),
        html.Div([
            html.Div([
                html.H3("Indonesia COVID-19 ", style={"margin-bottom": "0px", 'color': 'white'}),
                html.H5("Analytics & Explorations", style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column", id="title"),

        html.Div([
            html.H6('Terakhir Diperbarui : ', style={'color': 'white'}),
            html.H6(str(df_times['Total Case'].iloc[-1]) + '  19:30 (GMT)',
                    style={'color': 'white'})

        ], className="one-third column", id='title1'),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    # Multiple Cards Total Kasus Indonesia
    html.Div([
        # Total Kasus di Indonesia
        html.Div([
            html.H6(children='Total Kasus ',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            # Jumlah Total
            html.P(f"{df_categories['Total Case'].iloc[-1].sum()}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

            html.P(
                'Baru :  ' + f"{df_categories['Total Case'].iloc[-1].sum() - df_categories['Total Case'].iloc[-2].sum()} "
                + ' (' + str(
                    round(((df_categories['Total Case'].iloc[-1].sum() - df_categories['Total Case'].iloc[-2].sum()) /
                           df_categories['Total Case'].iloc[-1].sum()) * 100, 2)) + '%)',
                style={
                    'textAlign': 'center',
                    'color': '#e55467',
                    'fontSize': 15,
                    'margin-top': '-18px'}
            )
        ], className="card_container three columns",
        ),

        # Kasus Aktif
        html.Div([
            html.H6(children='Total Kasus Aktif ',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            # Jumlah Kasus Aktif
            html.P(f"{df_categories['Kasus Aktif'].iloc[-1].sum()}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

            html.P(
                'Baru :  ' + f"{df_categories['Kasus Aktif'].iloc[-1].sum() - df_categories['Kasus Aktif'].iloc[-2].sum()} "
                + ' (' + str(
                    round(((df_categories['Kasus Aktif'].iloc[-1].sum() - df_categories['Kasus Aktif'].iloc[-2].sum()) /
                           df_categories['Kasus Aktif'].iloc[-1].sum()) * 100, 2)) + '%)',
                style={
                    'textAlign': 'center',
                    'color': '#e55467',
                    'fontSize': 15,
                    'margin-top': '-18px'}
            )
        ], className="card_container three columns",
        ),

        # Kasus Sembuh Harian
        html.Div([
            html.H6(children='Total Sembuh ',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            # Jumlah Sembuh
            html.P(f"{df_categories['Sembuh'].iloc[-1].sum()}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

            # Statistik
            html.P(
                'Baru :  ' + f"{df_categories['Sembuh'].iloc[-1].sum() - df_categories['Sembuh'].iloc[-2].sum()} "
                + ' (' + str(
                    round(((df_categories['Sembuh'].iloc[-1].sum() - df_categories['Sembuh'].iloc[-2].sum()) /
                           df_categories['Sembuh'].iloc[-1].sum()) * 100, 2)) + '%)',
                style={
                    'textAlign': 'center',
                    'color': '#e55467',
                    'fontSize': 15,
                    'margin-top': '-18px'}
            )
        ], className="card_container three columns",
        ),

        # Kasus Meninggal Dunia
        html.Div([
            html.H6(children='Total Meninggal Dunia ',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            # Jumlah Meninggal Dunia
            html.P(f"{df_categories['Meninggal Dunia'].iloc[-1].sum()}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

            # Statistik
            html.P(
                'Baru :  ' + f"{df_categories['Meninggal Dunia'].iloc[-1].sum() - df_categories['Meninggal Dunia'].iloc[-2].sum()} "
                + ' (' + str(
                    round(((df_categories['Meninggal Dunia'].iloc[-1].sum() -
                            df_categories['Meninggal Dunia'].iloc[
                                -2].sum()) /
                           df_categories['Meninggal Dunia'].iloc[-1].sum()) * 100, 2)) + '%)',
                style={
                    'textAlign': 'center',
                    'color': '#e55467',
                    'fontSize': 15,
                    'margin-top': '-18px'}
            )
        ], className="card_container three columns",
        ),
    ], className="row flex-display"),

    # Second ROW Card
    html.Div([
        # Kasus Meninggal Dunia Harian
        html.Div([
            html.H6(children='Total Meninggal Dunia Harian ',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            # Jumlah Meninggal Dunia Harian
            html.P(f"{df_categories['Meninggal Dunia Harian'].iloc[-1].sum()}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

            # Statistik
            html.P(
                'Baru :  ' + f"{df_categories['Meninggal Dunia Harian'].iloc[-1].sum() - df_categories['Meninggal Dunia Harian'].iloc[-2].sum()} "
                + ' (' + str(
                    round(((df_categories['Meninggal Dunia Harian'].iloc[-1].sum() -
                            df_categories['Meninggal Dunia Harian'].iloc[
                                -2].sum()) /
                           df_categories['Meninggal Dunia Harian'].iloc[-1].sum()) * 100, 2)) + '%)',
                style={
                    'textAlign': 'center',
                    'color': '#e55467',
                    'fontSize': 15,
                    'margin-top': '-18px'}
            )
        ], className="card_container three columns",
        ),

        # Kasus Sembuh Harian
        html.Div([
            html.H6(children='Total Sembuh Harian ',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            # Jumlah Sembuh Harian
            html.P(f"{df_categories['Sembuh Harian'].iloc[-1].sum()}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

            # Statistik
            html.P(
                'Baru :  ' + f"{df_categories['Sembuh Harian'].iloc[-1].sum() - df_categories['Sembuh Harian'].iloc[-2].sum()} "
                + ' (' + str(
                    round(((df_categories['Sembuh Harian'].iloc[-1].sum() - df_categories['Sembuh Harian'].iloc[
                        -2].sum()) /
                           df_categories['Sembuh Harian'].iloc[-1].sum()) * 100, 2)) + '%)',
                style={
                    'textAlign': 'center',
                    'color': '#e55467',
                    'fontSize': 15,
                    'margin-top': '-18px'}
            )
        ], className="card_container three columns",
        ),

        # Kasus Kasus Harian
        html.Div([
            html.H6(children='Total Kasus Harian ',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            # Jumlah Kasus Harian
            html.P(f"{df_categories['Kasus Harian'].iloc[-1].sum()}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

            # Statistik
            html.P(
                'Baru :  ' + f"{df_categories['Kasus Harian'].iloc[-1].sum() - df_categories['Kasus Harian'].iloc[-2].sum()} "
                + ' (' + str(
                    round(
                        ((df_categories['Kasus Harian'].iloc[-1].sum() - df_categories['Kasus Harian'].iloc[-2].sum()) /
                         df_categories['Kasus Harian'].iloc[-1].sum()) * 100, 2)) + '%)',
                style={
                    'textAlign': 'center',
                    'color': '#e55467',
                    'fontSize': 15,
                    'margin-top': '-18px'}
            )
        ], className="card_container three columns",
        )

    ], className="row flex-display"),

    # Third Rowss Component
    html.Div([

        # Statistik Per Provinsi
        html.Div([

            html.P('Pilih Provinsi:', className='fix_label', style={'color': 'white'}),

            dcc.Dropdown(id='province',
                         multi=False,
                         clearable=True,
                         value='Jakarta',
                         placeholder='Pilih Provinsi',
                         options=[{'label': c, 'value': c}
                                  for c in (df_categories['Total Case'].columns)], className='dcc_compon'),

            html.P('Kasus Terbaru : ' + '  ' + ' ' + str(df_times['Total Case'].iloc[-1]) + '  ',
                   className='fix_label', style={'color': 'white', 'text-align': 'center'}),
            dcc.Graph(id='new_cases', config={'displayModeBar': False}, className='dcc_compon',
                      style={'margin-top': '20px'},
                      ),

            dcc.Graph(id='active_cases', config={'displayModeBar': False}, className='dcc_compon',
                      style={'margin-top': '20px'},
                      ),

            dcc.Graph(id='cured_cases', config={'displayModeBar': False}, className='dcc_compon',
                      style={'margin-top': '20px'},
                      ),

            dcc.Graph(id='death', config={'displayModeBar': False}, className='dcc_compon',
                      style={'margin-top': '20px'},
                      ),

        ], className="create_container three columns", id="cross-filter-options"),

        # Plot Pie Chart
        html.Div([
            dcc.Graph(id='pie_chart',
                      config={'displayModeBar': 'hover'}),
        ], className="create_container four columns"),

        # Plot Line Char
        html.Div([
            dcc.Graph(id="line_chart")

        ], className="create_container five columns"),

    ], className="row flex-display"),

    # MAPS
    html.Div([
        html.Div([
            dcc.Graph(id="map")], className="create_container1 twelve columns"),
    ], className="row flex-display"),

], id="mainContainer",
    style={"display": "flex", "flex-direction": "column"})


# -- END Layout

# -- Provinces Function
# New Cases Provinsi
@app.callback(Output('new_cases', 'figure'), [Input('province', 'value')])
def update_new_cases(province):
    value_confirmed = df_categories['Total Case'][province].iloc[-1] - df_categories['Total Case'][province].iloc[-2]
    delta_confirmed = df_categories['Total Case'][province].iloc[-2] - df_categories['Total Case'][province].iloc[-3]

    result = {
        "data": [go.Indicator(
            mode='number+delta',
            value=value_confirmed,
            delta={
                'reference': delta_confirmed,
                'position': 'right',
                'valueformat': ',g',
                'relative': False,
                'font': {
                    'size': 15
                }
            },
            number={
                "valueformat": ',',
                'font': {'size': 20}
            },
            domain={
                'y': [0, 1],
                'x': [0, 1]
            }
        )],
        'layout': go.Layout(
            title={
                'text': 'Kasus Terkonfirmasi',
                'y': 1,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            font=dict(color='white'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50
        )
    }

    return result


# --

# ACtive Cases Provinsi
@app.callback(Output('active_cases', 'figure'), [Input('province', 'value')])
def update_active_cases(province):
    value_confirmed = df_categories['Kasus Aktif'][province].iloc[-1] - df_categories['Kasus Aktif'][province].iloc[-2]
    delta_confirmed = df_categories['Kasus Aktif'][province].iloc[-2] - df_categories['Kasus Aktif'][province].iloc[-3]

    result = {
        "data": [go.Indicator(
            mode='number+delta',
            value=value_confirmed,
            delta={
                'reference': delta_confirmed,
                'position': 'right',
                'valueformat': ',g',
                'relative': False,
                'font': {
                    'size': 15
                }
            },
            number={
                "valueformat": ',',
                'font': {'size': 20}
            },
            domain={
                'y': [0, 1],
                'x': [0, 1]
            }
        )],
        'layout': go.Layout(
            title={
                'text': 'Kasus Aktif',
                'y': 1,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            font=dict(color='white'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50
        )
    }

    return result


# --

# Cured Cases Provinsi
@app.callback(Output('cured_cases', 'figure'), [Input('province', 'value')])
def update_cured_cases(province):
    value_confirmed = df_categories['Sembuh'][province].iloc[-1] - df_categories['Sembuh'][province].iloc[-2]
    delta_confirmed = df_categories['Sembuh'][province].iloc[-2] - df_categories['Sembuh'][province].iloc[-3]

    result = {
        "data": [go.Indicator(
            mode='number+delta',
            value=value_confirmed,
            delta={
                'reference': delta_confirmed,
                'position': 'right',
                'valueformat': ',g',
                'relative': False,
                'font': {
                    'size': 15
                }
            },
            number={
                "valueformat": ',',
                'font': {'size': 20}
            },
            domain={
                'y': [0, 1],
                'x': [0, 1]
            }
        )],
        'layout': go.Layout(
            title={
                'text': 'Kasus Sembuh',
                'y': 1,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            font=dict(color='white'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50
        )
    }

    return result


# --

# Death Cases Provinsi
@app.callback(Output('death', 'figure'), [Input('province', 'value')])
def update_death_cases(province):
    value_confirmed = df_categories['Meninggal Dunia'][province].iloc[-1] - \
                      df_categories['Meninggal Dunia'][province].iloc[-2]
    delta_confirmed = df_categories['Meninggal Dunia'][province].iloc[-2] - \
                      df_categories['Meninggal Dunia'][province].iloc[-3]

    result = {
        "data": [go.Indicator(
            mode='number+delta',
            value=value_confirmed,
            delta={
                'reference': delta_confirmed,
                'position': 'right',
                'valueformat': ',g',
                'relative': False,
                'font': {
                    'size': 15
                }
            },
            number={
                "valueformat": ',',
                'font': {'size': 20}
            },
            domain={
                'y': [0, 1],
                'x': [0, 1]
            }
        )],
        'layout': go.Layout(
            title={
                'text': 'Kasus Meninggal Dunia',
                'y': 1,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            font=dict(color='white'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50
        )
    }

    return result


# --

# Create pie chart (total casualties)
@app.callback(Output('pie_chart', 'figure'),
              [Input('province', 'value')])
def update_graph(province):
    new_confirmed = df_categories['Kasus Aktif'][province].iloc[-1]
    new_death = df_categories['Meninggal Dunia Harian'][province].iloc[-1]
    new_recovered = df_categories['Sembuh Harian'][province].iloc[-1]
    new_active = df_categories['Kasus Harian'][province].iloc[-1]
    colors = ['orange', '#dd1e35', 'green', '#e55467']

    return {
        'data': [go.Pie(labels=['Kasus Aktif', 'Meninggal Harian', 'Sembuh Harian', 'Kasus Harian'],
                        values=[new_confirmed, new_death, new_recovered, new_active],
                        marker=dict(colors=colors),
                        hoverinfo='label+value+percent',
                        textinfo='label+value',
                        textfont=dict(size=13),
                        hole=.7,
                        rotation=45
                        )],

        'layout': go.Layout(
            # width=800,
            # height=520,
            plot_bgcolor='#1f2c56',
            paper_bgcolor='#1f2c56',
            hovermode='closest',
            title={
                'text': 'Kasus Harian : ' + (province),
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                       'color': 'white',
                       'size': 20},
            legend={
                'orientation': 'h',
                'bgcolor': '#1f2c56',
                'xanchor': 'center', 'x': 0.5, 'y': -0.2},
            font=dict(
                family="sans-serif",
                size=12,
                color='white')
            ),


        }



if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
