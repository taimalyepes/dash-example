import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd
import os

# Recall app
from app import app

data = pd.read_csv('~/Documents/analisis_datos/dash-example/app/data/Iris.csv')

data = data.drop('Id', axis = 1)
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

variables_dict = {'sepal_length': 'Sepal Length', 'sepal_width': 'Sepal Width', 'petal_length': 'Petal Length', 'petal_width': 'Petal Width'}

dropdown_x = 'sepal_length'
dropdown_y = 'sepal_width'

Scatter_fig = px.scatter(
    data_frame = data,
    x = dropdown_x,
    y = dropdown_y,
    color = 'species'
)
Scatter_fig.update_layout(
    title= 'Scatterplot ' + variables_dict[dropdown_x] + ' vs. ' + variables_dict[dropdown_y] , paper_bgcolor="#F8F9F9"
)


Box_fig_x = px.box(
    data_frame = data,
    x = 'species',
    y = dropdown_x,
    color = 'species'

)
Box_fig_x.update_layout(showlegend=False, xaxis_title = 'Species',
                        title = 'Boxplot: ' + variables_dict[dropdown_x],
                        yaxis_title = variables_dict[dropdown_x], paper_bgcolor="#F8F9F9")

Box_fig_y = px.box(
    data_frame = data,
    x = 'species',
    y = dropdown_y,
    color = 'species'

)
Box_fig_y.update_layout(showlegend=False, xaxis_title = 'Species',
                        title = 'Boxplot: ' + variables_dict[dropdown_y],
                        yaxis_title = variables_dict[dropdown_y],  paper_bgcolor="#F8F9F9")


stats = html.Div(
    [
        # Place the different graph components here.
        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=Scatter_fig, id="Scatter"))
            ]
        ),
        
        dbc.Row(
            [
             dbc.Col(dcc.Graph(figure=Box_fig_x, id="Boxplot_x")),
             dbc.Col(dcc.Graph(figure=Box_fig_y, id="Boxplot_y"))   
            ]
        
        )
        
    ],
    className="ds4a-body",
)