import aiohttp
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from src.utils import load_data_postprocessing,province_name_to_abr

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
            dcc.Graph(id="new_cases_line_chart")
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
                'text': 'Kasus Harian',
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


# Timeline plot
@app.callback(Output('new_cases_line_chart', 'figure'),
              [Input('province', 'value')])
def update_graph(province):
    # daily confirmed
    df_new_active = df_categories['Kasus Harian'][province]
    df_date = pd.to_datetime(df_times['Kasus Harian'])
    df_rolling_average = df_new_active.rolling(window=7).mean()

    result = {
        'data': [go.Bar(x=df_date.tail(30),
                        y=df_new_active.tail(30),

                        name='Kasus Harian',
                        marker=dict(
                            color='orange'),
                        hoverinfo='text',
                        hovertext=
                        '<b>Waktu</b>: ' + df_date.tail(30).astype(str) + '<br>' +
                        '<b>Kasus Harian</b>: ' + [f'{x:,.0f}' for x in df_new_active.tail(30)] + '<br>' +
                        '<b>Provinsi</b>: ' + province + '<br>'

                        ),
                 go.Scatter(x=df_date.tail(30),
                            y=df_rolling_average.tail(30),
                            mode='lines',
                            name='Rata-rata mingguan kasus harian',
                            line=dict(width=3, color='#FF00FF'),
                            # marker=dict(
                            #     color='green'),
                            hoverinfo='text',
                            hovertext=
                            '<b>Waktu</b>: ' + df_date.tail(30).astype(str) + '<br>' +
                            '<b>Rata-rata Mingguan Kasus Harian</b>: ' + [f'{x:,.0f}' for x in
                                                                          df_rolling_average.tail(30)] + '<br>'
                            )],

        'layout': go.Layout(
            plot_bgcolor='#1f2c56',
            paper_bgcolor='#1f2c56',
            title={
                'text': '30 Hari Terakhir Kasus Harian di ' + (province),
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': 'white',
                'size': 20},

            hovermode='x',
            margin=dict(r=0),
            xaxis=dict(title='<b>Waktu</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='white'
                       )

                       ),

            yaxis=dict(title='<b>Kasus Harian</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='white'
                       )

                       ),

            legend={
                'orientation': 'h',
                'bgcolor': '#1f2c56',
                'xanchor': 'center', 'x': 0.5, 'y': -0.3},
            font=dict(
                family="sans-serif",
                size=12,
                color='white'),

        )

    }
    return result


@app.callback(Output('map', 'figure'),
              [Input('province', 'value')])
def update_graph(province):
    # covid_data_3 = covid_data.groupby(['Lat', 'Long', 'Country/Region'])[['confirmed', 'death', 'recovered', 'active']].max().reset_index()
    # covid_data_4 = covid_data_3[covid_data_3['Country/Region'] == w_countries]
    #other_covid19_data = get_covid_19_data()
    #print(other_covid19_data)
    df_province_geo_location = pd.read_json("../data/geo_location_provinces.json")
    df_province_geo_location['province'] = df_province_geo_location['name'].apply(lambda name: province_name_to_abr(name))
    #print(df_province_geo_location.head(5))
    df_province_geo_location = df_province_geo_location.set_index('province')

    #print(df_province_geo_location.index("Aceh"))



    latitude = df_province_geo_location['latitude'][df_province_geo_location.index == province]
    longitude = df_province_geo_location['longitude'][df_province_geo_location.index == province]
    jumlah_kasus = df_categories['Total Case'][province].iloc[-1]
    jumlah_sembuh = df_categories['Sembuh'][province].iloc[-1]
    jumlah_aktif = df_categories['Kasus Aktif'][province].iloc[-1]
    jumlah_meninggal = df_categories['Meninggal Dunia'][province].iloc[-1]

    if province:
        zoom = 8
        zoom_lat = latitude.values[0]
        zoom_lon = longitude.values[0]

    result = {
        'data': [go.Scattermapbox(
            lon=longitude.values,
            lat=latitude.values,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=jumlah_kasus / 400,
                color=jumlah_kasus,
                colorscale='hsv',
                showscale=False,
                sizemode='area',
                opacity=0.3),

            hoverinfo='text',
            hovertext=
            '<b>Provinsi </b>: ' + province + '<br>' +
            '<b>Lintang</b>: ' + str(latitude.values[0]) + '<br>' +
            '<b>Bujur</b>: ' + str(longitude.values[0]) + '<br>' +
            '<b>Jumlah Kasus</b>: ' + str(jumlah_kasus) + '<br>' +
            '<b>Jumlah Sembuh</b>: ' + str(jumlah_sembuh) + '<br>' +
            '<b>Jumlah Meninggal</b>: ' + str(jumlah_meninggal) + '<br>' +
            '<b>Jumlah Aktif</b>: ' + str(jumlah_aktif) + '<br>'

        )],

        'layout': go.Layout(
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            # width=1820,
            # height=650,
            hovermode='closest',
            mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',
                center=go.layout.mapbox.Center(lat=zoom_lat, lon=zoom_lon),
                # style='open-street-map',
                style='dark',
                zoom=zoom
            ),
            autosize=True,

        )

    }


    return result


async def get_covid_19_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://data.covid19.go.id/public/api/prov.json") as resp:
            return await resp.json()


if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
