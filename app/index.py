# Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

# Recall app
from app import app


from lib import  sidebar, stats


# Data to plot

data = pd.read_csv('~/Documents/analisis_datos/dash-example/app/data/Iris.csv')

data = data.drop('Id', axis = 1)
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

variables_dict = {'sepal_length': 'Sepal Length', 'sepal_width': 'Sepal Width', 'petal_length': 'Petal Length', 'petal_width': 'Petal Width'}

# Plot layout


app.layout = html.Div(
    [sidebar.sidebar, stats.stats],
    className="ds4a-app",  # You can also add your own css files by locating them into the assets folder
)



# Callbacks and interactions

@app.callback(
    [
        Output("Scatter", "figure"),
        Output("Boxplot_x", "figure"),
        Output("Boxplot_y", "figure")
    ],
    [
        Input("variables_dropdown_x", "value"),
        Input("variables_dropdown_y", "value"),
        Input("species_button", "value")
    ]
)
def update_plots(dropdown_x, dropdown_y, button):
    
    if (button == 'si')  :
        Scatter_fig = px.scatter(
            data_frame = data,
            x = dropdown_x,
            y = dropdown_y,
            color = 'species'
        )
        Scatter_fig.update_layout(
        title='Scatterplot' + variables_dict[dropdown_x] + 'vs.' + variables_dict[dropdown_y],
        xaxis_title = variables_dict[dropdown_x],
        yaxis_title = variables_dict[dropdown_y],
        paper_bgcolor="#F8F9F9"
        )
        
    else :
        Scatter_fig = px.scatter(
            data_frame = data,
            x = dropdown_x,
            y = dropdown_y,
        )
        Scatter_fig.update_layout(
        title='Scatterplot: ' + variables_dict[dropdown_x] + ' vs. ' + variables_dict[dropdown_y],
        xaxis_title = variables_dict[dropdown_x],
        yaxis_title = variables_dict[dropdown_y],
        paper_bgcolor="#F8F9F9"
        )
    
    Box_fig_x = px.box(
    data_frame = data,
    x = 'species',
    y = dropdown_x,
    color = 'species'
    )
    Box_fig_x.update_layout(showlegend=False, xaxis_title = 'Species',
                            title = 'Boxplot: ' + variables_dict[dropdown_x],
                            yaxis_title = 'cm', paper_bgcolor="#F8F9F9")
    
    
    Box_fig_y = px.box(
    data_frame = data,
    x = 'species',
    y = dropdown_y,
    color = 'species'
    )
    Box_fig_y.update_layout(showlegend=False,  xaxis_title = 'Species',
                            title = 'Boxplot: ' + variables_dict[dropdown_y],
                            yaxis_title = 'cm', paper_bgcolor="#F8F9F9")    
    
    return [Scatter_fig, Box_fig_x, Box_fig_y]


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=True)