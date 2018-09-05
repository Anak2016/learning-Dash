import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like  
import pandas_datareader.data as web
import datetime

# note:
# Google and yahoo: no longer offer free data
# robinhood: begins_at gives error



app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Symbol to graph:
    '''),
    dcc.Input(id='input', value='', type='text'),
    dcc.Graph(id = 'output-graph')
    # html.Div(id='output-graph'),

])

@app.callback(
    Output('output-graph','figure'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    start = datetime.datetime(2018, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'quandl', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    # df = df.drop("symbol", axis=1)
    # print(df.head())

    return {
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
    }

if __name__ == '__main__':
    app.run_server(debug=True)

# start = datetime.datetime(2015, 1, 1)
# end = datetime.datetime.now()
# df = web.DataReader("TSLA", 'robinhood', start, end)
# df.reset_index(inplace=True)
# df.set_index("begins_at", inplace=True)
# df = df.drop("symbol", axis=1)

# print(df.head())