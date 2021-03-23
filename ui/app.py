import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from src.utils import load_data_postprocessing

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],title="Indonesia COVID-19")

# load post_processing data
print("Load data...")
df_categories, df_times = load_data_postprocessing()

print("Config Layout...")
# layout
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
                "padding-top" : "30px"
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
    ],className="row flex-display"),

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
                    round(((df_categories['Sembuh Harian'].iloc[-1].sum() - df_categories['Sembuh Harian'].iloc[-2].sum()) /
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
                    round(((df_categories['Kasus Harian'].iloc[-1].sum() - df_categories['Kasus Harian'].iloc[-2].sum()) /
                           df_categories['Kasus Harian'].iloc[-1].sum()) * 100, 2)) + '%)',
                style={
                    'textAlign': 'center',
                    'color': '#e55467',
                    'fontSize': 15,
                    'margin-top': '-18px'}
            )
        ], className="card_container three columns",
        )

    ], className="row flex-display")
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
