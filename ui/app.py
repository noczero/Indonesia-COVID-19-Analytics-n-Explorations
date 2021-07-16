import aiohttp
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import os

from src.covid19 import Covid19
from src.utils import load_data_postprocessing, province_name_to_abr

# MODE
RETRIEVE_MODE = True

# PATH
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # This is your Project Root
DATA_PATH = os.path.join(ROOT_DIR, 'data')
IMAGES_PATH = os.path.join(ROOT_DIR, 'images')

# Update plot
if RETRIEVE_MODE:
    format = 'csv'  # export format
    sheet_gid = '2052139453'  # get from browser url when sheet clicked
    data_url = 'https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/export?format={}&gid={}'.format(
        format, sheet_gid)
    indo_covid19 = Covid19(url=data_url)
    indo_covid19.generate_csv()

STORAGE_URL = "https://github.com/noczero/Indonesia-COVID-19-Analytics-n-Explorations/blob/master"

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}], title="Indonesia COVID-19",
                external_stylesheets=[dbc.themes.BOOTSTRAP])

# load post_processing data
print("Load data...")
df_categories, df_times = load_data_postprocessing()

print("Config Layout...")
# get layout from main_layout
from layout.main_layout import *

# -- END Layout
# get callback function from callback_function
from callback.callback_functions import *


async def get_covid_19_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://data.covid19.go.id/public/api/prov.json") as resp:
            return await resp.json()


if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port=8080)
