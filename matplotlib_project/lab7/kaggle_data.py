'''Questions:
Visualize monthly sales trends over the past year using a line chart.
Compare sales by product category using a bar chart.
Show the regional sales distribution using a pie chart or choropleth map.
Add a dropdown menu to filter data by region or product category.
Include a summary card displaying total sales, average order value, and top-selling product.'''
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


app= Dash(__name__)
df= pd.read_excel("sales.xls")
df['Order Date']= pd.to_datetime(df['Order Date'])
products= df['Product Name']
years= df['Order Date'].dt.year
sales= df['Sales']
app.layout= html.Div([
    html.H2("Sales Data"),
    html.Div([
        html.Label("Dropdown",id= "product"),
        dcc.Dropdown()
    ]),
    html.Div([
        html.Label("Line Plot",id="line-plot"),
        dcc.Graph(id="line-plot")
    ]),
    html.Div([
        html.Label("Bar Plot",id= "bar-plot"),
        dcc.Graph(id= "bar-plot")
    ]),
    html.Div([
        html.Label("Pie Chart",id= "pie-plot"),
        dcc.Graph(id= "pie-plot")
    ])
    
])