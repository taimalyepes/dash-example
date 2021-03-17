import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import json
from datetime import datetime as dt

# Recall app
from app import app

example_img = html.Div(
    children=[html.Img(src=app.get_asset_url("~/Documents/analisis_datos/dash-example/app/assets/logo.png"), id="example-image",)],
)

variables_dict = {'sepal_length': 'Sepal Lenght', 'sepal_width': 'Sepal Width', 'petal_length': 'Petal Length', 'petal_width': 'Petal Width'}

dropdown_x =dcc.Dropdown(
    id="variables_dropdown_x",
    options=[{"label": variables_dict[key], "value": key} for key in variables_dict.keys()],
    value="sepal_length",
    searchable=False,
    multi=False
)


dropdown_y =dcc.Dropdown(
    id="variables_dropdown_y",
    options=[{"label": variables_dict[key], "value": key} for key in variables_dict.keys()],
    value="sepal_width",
    searchable=False,
    multi=False
)

species_radio = dcc.RadioItems(
    id = 'species_button',
    options=[
        {'label': 'Sí', 'value': 'si'},
        {'label': 'No', 'value': 'no'}
    ],
    value='no',
    labelStyle={'display': 'inline-block'}
) 

sidebar = html.Div(
    [
        # Place the rest of Layout here
        
        example_img,
        html.Hr(),

        html.H5("Seleccione Variables a visualizar: Eje X"),
        dropdown_x,
        
        html.Hr(),
        
        html.H5("Seleccione Variables a visualizar: Eje Y"),
        dropdown_y,
        
        html.Hr(),
        
        html.H5("¿Desea discriminar por especie?"),
        species_radio
        
        ####################################################
    ],
   className="example-sidebar",
)