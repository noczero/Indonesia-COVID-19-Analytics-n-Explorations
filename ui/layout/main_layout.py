from ui.app import app, df_times, df_categories
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

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
            className="text-center col-md-4",
            style={
                "padding-top": "30px"
            }
        ),
        html.Div([
            html.Div([
                html.H3("Indonesia COVID-19 ", style={"margin-bottom": "0px", 'color': 'white'}),
                html.H5("Analytics & Explorations", style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="col-md-4", id="title"),

        html.Div([
            html.H6('Terakhir Diperbarui : ', style={'color': 'white'}),
            html.H6(str(df_times['Total Case'].iloc[-1]) + '  20:30 (GMT)',
                    style={'color': 'white'})

        ], className="col-md-4", id='title1'),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    # Multiple Cards Total Kasus Indonesia
    html.Div([
        # Total Kasus di Indonesia
        html.Div([
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
                        round(
                            ((df_categories['Total Case'].iloc[-1].sum() - df_categories['Total Case'].iloc[-2].sum()) /
                             df_categories['Total Case'].iloc[-1].sum()) * 100, 2)) + '%)',
                    style={
                        'textAlign': 'center',
                        'color': '#e55467',
                        'fontSize': 15,
                        'margin-top': '-18px'}
                )
            ], className="card_container",
            ),
        ], className="col-md-3"),

        # Kasus Aktif
        html.Div([
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
                        round(((df_categories['Kasus Aktif'].iloc[-1].sum() - df_categories['Kasus Aktif'].iloc[
                            -2].sum()) /
                               df_categories['Kasus Aktif'].iloc[-1].sum()) * 100, 2)) + '%)',
                    style={
                        'textAlign': 'center',
                        'color': '#e55467',
                        'fontSize': 15,
                        'margin-top': '-18px'}
                )
            ], className="card_container"),
        ], className="col-md-3"),

        # Kasus Sembuh Harian
        html.Div([
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
            ], className="card_container",
            ),
        ], className="col-md-3"),

        # Kasus Meninggal Dunia
        html.Div([
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
            ], className="card_container",
            )
        ], className="col-md-3"),
    ], className="row"),

    # Second ROW Card
    html.Div([
        # Kasus Meninggal Dunia Harian
        html.Div([
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
            ], className="card_container",
            ), ], className="col-md-3"),

        # Kasus Sembuh Harian
        html.Div([
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
            ], className="card_container",
            ), ], className="col-md-3"),

        # Kasus Kasus Harian
        html.Div([
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
                            ((df_categories['Kasus Harian'].iloc[-1].sum() - df_categories['Kasus Harian'].iloc[
                                -2].sum()) /
                             df_categories['Kasus Harian'].iloc[-1].sum()) * 100, 2)) + '%)',
                    style={
                        'textAlign': 'center',
                        'color': '#e55467',
                        'fontSize': 15,
                        'margin-top': '-18px'}
                )
            ], className="card_container",
            ), ], className="col-md-3"),

        html.Div([
            html.Div(
                [
                    html.Div([
                        dbc.Button("Lihat Zona Clustering", id="zona_cluster", className="btn btn-warning"),
                    ], className="container p-2"),
                    html.Div([
                        dbc.Button("Lihat Statistik Keseluruhan Provinsi", id="plot-multi-line-provinsi",
                                   className="btn btn-info"),
                    ], className="container p-2"),

                    dbc.Modal(
                        [
                            dbc.ModalHeader("Zona Clustering"),
                            dbc.ModalBody([
                                html.Div([
                                    html.H6(children='Zona Cluster Berdasarkan Rate Sembuh Harian & Meninggal Harian',
                                            style={
                                                'textAlign': 'center'},
                                            className="font-weight-bold"
                                            ),
                                    html.Img(
                                        src="#",
                                        id='plot-k-means-daily',
                                        style={
                                            "margin-bottom": "25px",
                                        },
                                        className="img-fluid",
                                    ),
                                ], className="container text-center",
                                ),
                                html.Hr(),
                                html.Div([
                                    html.H6(
                                        children='Zona Cluster Berdasarkan Rata-Rata Kasus Aktif Mingguan & Rata-Rata Penambahan Kasus per Kapita Mingguan',
                                        style={
                                            'textAlign': 'center'},
                                        className="font-weight-bold"
                                    ),
                                    html.Img(
                                        src="#",
                                        id='plot-k-means-weekly',
                                        style={
                                            "margin-bottom": "25px",
                                        },
                                        className="img-fluid ",
                                    ),
                                ], className="container text-center",
                                ),

                            ]),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="close", className="ml-auto")
                            ),
                        ],
                        id="zona_cluster_modal",
                        size="lg"
                    ),

                    dbc.Modal(
                        [
                            dbc.ModalHeader("Plot Statistik Keseluruhan Provinsi"),
                            dbc.ModalBody([
                                html.Div([
                                    html.H6(children='Kasus Aktif',
                                            style={
                                                'textAlign': 'center'},
                                            className='font-weight-bold'
                                            ),
                                    html.Img(
                                        src="https://raw.githubusercontent.com/noczero/Indonesia-COVID-19-Analytics-n-Explorations/master/images/Kasus%20Aktif_Semua_Provinsi.png",
                                        style={
                                            "margin-bottom": "25px",
                                        },
                                        className="img-fluid",
                                    ),
                                ], className="container text-center"),

                                html.Hr(),
                                html.Div([
                                    html.H6(
                                        children='Kasus Sembuh',
                                        style={
                                            'textAlign': 'center'},
                                        className='font-weight-bold'
                                        ),
                                    html.Img(
                                        src="https://raw.githubusercontent.com/noczero/Indonesia-COVID-19-Analytics-n-Explorations/master/images/Sembuh_Semua_Provinsi.png",
                                        style={
                                            "margin-bottom": "25px",
                                        },
                                        className="img-fluid",
                                    ),
                                ], className="container text-center"),

                                html.Hr(),
                                html.Div([
                                    html.H6(
                                        children='Kasus Meninggal Dunia',
                                        style={
                                            'textAlign': 'center'},
                                        className='font-weight-bold'
                                        ),
                                    html.Img(
                                        src="https://raw.githubusercontent.com/noczero/Indonesia-COVID-19-Analytics-n-Explorations/master/images/Meninggal%20Dunia_Semua_Provinsi.png",
                                        style={
                                            "margin-bottom": "25px",
                                        },
                                        className="img-fluid",
                                    ),
                                ], className="container text-center"),


html.Hr(),
                                html.Div([
                                    html.H6(
                                        children='Total Kasus Terkonfirmasi',
                                        style={
                                            'textAlign': 'center'},
                                        className='font-weight-bold'
                                        ),
                                    html.Img(
                                        src="https://raw.githubusercontent.com/noczero/Indonesia-COVID-19-Analytics-n-Explorations/master/images/Total%20Case_Semua_Provinsi.png",
                                        style={
                                            "margin-bottom": "25px",
                                        },
                                        className="img-fluid",
                                    ),
                                ], className="container text-center"),


                            ]),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="close_modals", className="ml-auto")
                            ),
                        ],
                        id="modals-statistik-provinsi",
                        size="lg"
                    ),
                ], className="card_container text-center"
            ), ], className="col-md-3"),
    ], className="row flex-display pt-4"),

    # Third Rowss Component
    html.Div([

        # Statistik Per Provinsi
        html.Div([
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

            ], className="create_container", id="cross-filter-options"),
        ], className="col-md-2"),

        # Plot Pie Chart
        html.Div([
            html.Div([
                dcc.Graph(id='pie_chart',
                          config={'displayModeBar': 'hover'}),
            ], className="create_container"),
        ], className="col-md-4"),

        # Plot Line Char
        html.Div([
            html.Div([
                dcc.Graph(id="new_cases_line_chart")
            ], className="create_container"),
        ], className="col-md-6"),

    ], className="row flex-display"),

    # MAPS

    html.Div([
        html.Div([
            dcc.Graph(id="map")], className="create_container1"),
    ], className="container flex-display"),

    # Static Plot First Row
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H6(children='Kasus Aktif',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-kasus-aktif',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4")
            ], className="col-md-4"),
            html.Div([
                html.Div([
                    html.H6(children='Kasus Harian',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-kasus-harian',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4")
            ], className="col-md-4"),
            html.Div([
                html.Div([
                    html.H6(children='Kasus Meninggal Dunia',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-kasus-meninggal',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4")
            ], className="col-md-4"),
        ], className="row flex-display"),

        # Static Plot Second Row
        html.Div([
            html.Div([
                html.Div([
                    html.H6(children='Kasus Meninggal Dunia Harian',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-kasus-meninggal-harian',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),

            html.Div([
                html.Div([
                    html.H6(children='Kasus Sembuh Harian',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-sembuh-harian',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),

            html.Div([
                html.Div([
                    html.H6(children='Kasus Sembuh',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-sembuh',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),
        ], className="row flex-display"),

        # Static Plot Third Row
        html.Div([
            html.Div([
                html.Div([
                    html.H6(children='Total Kasus',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-total-case',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),

            html.Div([
                html.Div([
                    html.H6(children='Kasus Sembuh Harian Rata-Rata Bulanan',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-sembuh-harian-rata-rata',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),

            html.Div([
                html.Div([
                    html.H6(children='Kasus Harian Rata-Rata Bulanan',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-kasus-harian-rata-rata',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),

        ], className="row flex-display"),

        # Static Plot Fourth Row
        html.Div([
            html.Div([
                html.Div([
                    html.H6(children='Kasus Meninggal Dunia Harian Rata-Rata Bulanan',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-meninggal-dunia-rata-rata',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),

            html.Div([
                html.Div([
                    html.H6(children='Kasus Meninggal Dunia Harian Rata-Rata Hari',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-meninggal-dunia-rata-rata-weekday',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),

            html.Div([
                html.Div([
                    html.H6(children='Kasus Sembuh Harian Rata-Rata Hari',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-sembuh-harian-rata-rata-weekday',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),

        ], className="row flex-display"),

        # Static Plot Fourth Row
        html.Div([
            html.Div([
                html.Div([
                    html.H6(children='Kasus Harian Rata-Rata Hari',
                            style={
                                'textAlign': 'center',
                                'color': 'white'}
                            ),
                    html.Img(
                        src="#",
                        id='plot-kasus-harian-rata-rata-weekday',
                        style={
                            "margin-bottom": "25px",
                        },
                        className="img-fluid rounded"
                    ),
                ], className="card_container_4",
                ),
            ], className="col-md-4"),
        ], className="row flex-display")
    ], className="m-5 text-center"),
], id="mainContainer", style={"display": "flex", "flex-direction": "column"})
