# -- Provinces Function
# New Cases Provinsi
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go
import pandas as pd
from src.utils import load_data_postprocessing, province_name_to_abr

from ui.app import df_categories, DATA_PATH, df_times, STORAGE_URL
from ui.app import app


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
    # other_covid19_data = get_covid_19_data()
    # print(other_covid19_data)
    df_province_geo_location = pd.read_json(f"{DATA_PATH}/geo_location_provinces.json")
    df_province_geo_location['province'] = df_province_geo_location['name'].apply(
        lambda name: province_name_to_abr(name))
    # print(df_province_geo_location.head(5))
    df_province_geo_location = df_province_geo_location.set_index('province')

    # print(df_province_geo_location.index("Aceh"))

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


# PLOT KASUS AKTIF
@app.callback(Output(component_id='plot-kasus-aktif', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_aktif(province):
    return f"{STORAGE_URL}/images/Kasus%20Aktif_{province}.png?raw=true"


# PLOT KASUS harian
@app.callback(Output(component_id='plot-kasus-harian', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_harian(province):
    return f"{STORAGE_URL}/images/Kasus%20Harian_{province}.png?raw=true"


# PLOT KASUS harian rata-rata
@app.callback(Output(component_id='plot-kasus-harian-rata-rata', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_harian_rata_rata(province):
    return f"{STORAGE_URL}/images/Kasus%20Harian%20Rata-Rata%20di%20{province}.png?raw=true"


# PLOT KASUS meninggal
@app.callback(Output(component_id='plot-kasus-meninggal', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_meninggal(province):
    return f"{STORAGE_URL}/images/Meninggal%20Dunia_{province}.png?raw=true"


# PLOT KASUS meninggal harian
@app.callback(Output(component_id='plot-kasus-meninggal-harian', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_meninggal_harian(province):
    return f"{STORAGE_URL}/images/Meninggal%20Dunia%20Harian_{province}.png?raw=true"


# PLOT TOTAL CASE
@app.callback(Output(component_id='plot-total-case', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_total_case(province):
    return f"{STORAGE_URL}/images/Total%20Case_{province}.png?raw=true"


# PLOT KASUS sembuh
@app.callback(Output(component_id='plot-sembuh', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_sembuh(province):
    return f"{STORAGE_URL}/images/Sembuh_{province}.png?raw=true"


# PLOT KASUS sembuh harian
@app.callback(Output(component_id='plot-sembuh-harian', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_sembuh_harian(province):
    return f"{STORAGE_URL}/images/Sembuh%20Harian_{province}.png?raw=true"


# PLOT KASUS sembuh rata-rata harian
@app.callback(Output(component_id='plot-sembuh-harian-rata-rata', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_sembuh_harian_rata_rata(province):
    return f"{STORAGE_URL}/images/Sembuh%20Harian%20Rata-Rata%20di%20{province}.png?raw=true"


# PLOT KASUS meninggal dunia rata-rata
@app.callback(Output(component_id='plot-meninggal-dunia-rata-rata', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_sembuh_harian_rata_rata(province):
    return f"{STORAGE_URL}/images/Meninggal%20Dunia%20Harian%20Rata-Rata%20di%20{province}.png?raw=true"


# PLOT KASUS meninggal dunia rata-rata dalam hari
@app.callback(Output(component_id='plot-meninggal-dunia-rata-rata-weekday', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_sembuh_harian_rata_rata(province):
    return f"{STORAGE_URL}/images/Meninggal%20Dunia%20Harian%20Rata-Rata%20dalam%20Hari%20di%20{province}.png?raw=true"


# PLOT KASUS sembuh harian rata-rata dalam hari
@app.callback(Output(component_id='plot-sembuh-harian-rata-rata-weekday', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_sembuh_harian_rata_rata(province):
    return f"{STORAGE_URL}/images/Sembuh%20Harian%20Rata-Rata%20dalam%20Hari%20di%20{province}.png?raw=true"


# PLOT KASUS sembuh harian rata-rata dalam hari
@app.callback(Output(component_id='plot-kasus-harian-rata-rata-weekday', component_property='src'),
              [Input('province', 'value')])
def update_plot_kasus_sembuh_harian_rata_rata(province):
    return f"{STORAGE_URL}/images/Kasus%20Harian%20Rata-Rata%20dalam%20Hari%20di%20{province}.png?raw=true"


# PLOT k-means-daily
@app.callback(Output(component_id='plot-k-means-daily', component_property='src'),
              [Input('province', 'value')])
def update_plot_kmeans_daily(province):
    return f"{STORAGE_URL}/images/K-Means-Daily_Semua_Provinsi.png?raw=true"


# PLOT k-means-weekly-no-norm
# @app.callback(Output(component_id='plot-k-means-weekly-no-norm', component_property='src'),
#              [Input('province', 'value')])
# def update_plot_kmeans_weekly_no_norm(province):
#    return f"{STORAGE_URL}/images/K-Means-Weekly_no_norm_Semua_Provinsi.png?raw=true"


# PLOT k-means-weekly-no-norm
@app.callback(Output(component_id='plot-k-means-weekly', component_property='src'),
              [Input('province', 'value')])
def update_plot_kmeans_weekly(province):
    return f"{STORAGE_URL}/images/K-Means_Weekly_Semua_Provinsi.png?raw=true"


@app.callback(
    Output("zona_cluster_modal", "is_open"),
    [Input("zona_cluster", "n_clicks"), Input("close", "n_clicks")],
    [State("zona_cluster_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modals-statistik-provinsi", "is_open"),
    [Input("plot-multi-line-provinsi", "n_clicks"), Input("close_modals", "n_clicks")],
    [State("modals-statistik-provinsi", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
