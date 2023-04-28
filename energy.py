"""

"""

import dash
from dash import dcc, dash_table
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

### pandas dataframe to html table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server

df = pd.read_csv('mo_final_project.csv')

app.layout = html.Div([
               html.H1('Electricity Price Dashboard',style={'color':'#2a3f5f','font-weight': 'bold','text-align': 'center'}),
               html.H6('Filter By: ', style={'color':'#2a3f5f','font-weight': 'bold','margin-left':'30px'}),
               html.Div(
                 children= [
                     html.Div(children = [

                         html.Label('Sector'),
                         dcc.Dropdown(df.Sector.unique().tolist(), 'Residential', id = 'sector_name')],
                         style={'width':'15%','margin':'0.5%','color':'#2a3f5f'}
                     ),
                    html.Div(children = [
                        html.Label('State 1'),
                        dcc.Dropdown(df.State.unique().tolist(), 'US', id = 'state_1')],
                        style={'width':'12%','margin':'0.5%','color':'#2a3f5f'}
                    ),
                     html.Div(children = [
                         html.Label('State 2'),
                         dcc.Dropdown(df.State.unique().tolist(), 'NY', id = 'state_2')],
                         style={'width':'12%','margin':'0.5%','color':'#2a3f5f'}
                     ),
                     html.Div(children = [
                         html.Label('State 3'),
                         dcc.Dropdown(df.State.unique().tolist(), 'ND', id = 'state_3')],
                         style={'width':'12%','margin':'0.5%','color':'#2a3f5f'}
                     ),
                     html.Div(children = [
                         html.Label('State 4'),
                         dcc.Dropdown(df.State.unique().tolist(), 'HI', id = 'state_4')],
                         style={'width':'12%','margin':'0.5%','color':'#2a3f5f'}
                     ),
                     html.Div(children = [
                         html.Label('State 5'),
                         dcc.Dropdown(df.State.unique().tolist(), 'WA', id = 'state_5')],
                         style={'width':'12%','margin':'0.5%','color':'#2a3f5f'}
                     ),
                     html.Div(children = [
                         html.Label('State 6'),
                         dcc.Dropdown(df.State.unique().tolist(), 'CA', id = 'state_6')],
                         style={'width':'12%','margin':'0.5%','color':'#2a3f5f'}
                     )
                ], style={'display': 'flex', 'flex-direction': 'row',
                          'flex-wrap': 'wrap','margin-left':'auto','margin-right':'auto',
                          'width':'97%', 'background-color':' #f1f1f1', 'justify-content': 'center'}
            ),
               html.Div(
                    children=[
                        dcc.Graph(id="graph")
                    ], style={'margin-top': '25px'}
                ),
               html.Div(id='table_title', style={'margin-left':'auto','margin-right':'auto','text-align':'center',
                                                 'font-size': '20px','color':'#2a3f5f','width':'90%'}),
               html.Div(children = [
                    dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns])
                ],  id='tbl', style={'width':'90%', 'margin-left':'auto','margin-right':'auto','text-align':'center'}),

               html.Div(children=[
                                html.H4('Summary', style = {'color':'#2a3f5f'}),
                                html.P(children=[
                                    html.A('The electricity ',
                                           href='https://www.eia.gov/electricity/data.php',
                                           target='_blank'),
                                    html.Span('data used in this dashboard is from '
                                              'the U.S Energy Information Administration and it consists of'
                                              ' total sales(consumption), revenues generated, prices and customers '
                                              'of electricity in each sector across different states from 2010 - 2021.'
                                              'This dashboard visualizes price overtime across the several states')]),
                                html.P(children=[
                                    html.Strong('Residential Sector '),
                                    html.Span('means an energy-consuming sector that consists of living quarters for private households. Common uses of energy associated with this sector include space heating, water heating, air conditioning, lighting, refrigeration, cooking, and running a variety of other appliances. The residential sector excludes institutional living quarters.')
                                ]),
                                html.P(children=[
                                    html.Strong('Commercial Sector '),
                                    html.Span('means an energy-consuming sector that consists of service-providing facilities and equipment of businesses; Federal, State, and local governments; and other private and public organizations, such as religious, social, or fraternal groups. The commercial sector includes institutional living quarters. It also includes sewage treatment facilities. Common uses of energy associated with this sector include space heating, water heating, air conditioning, lighting, refrigeration, cooking, and running a wide variety of other equipment.')
                                ]),
                                html.P(children=[
                                    html.Strong('Industrial Sector '),
                                    html.Span('means an energy-consuming sector that consists of all facilities and equipment used for producing, processing, or assembling goods. The industrial sector encompasses the following types of activity: manufacturing; agriculture, forestry, fishing and hunting; mining, including oil and gas extraction; and construction. Overall energy use in this sector is largely for process heat and cooling and powering machinery, with lesser amounts used for facility heating, air conditioning, and lighting.')
                                ]),
                                html.P(children=[
                                    html.Strong('Transportation Sector '),
                                    html.Span('means an energy-consuming sector that consists of all vehicles whose primary purpose is transporting people and/or goods from one physical location to another. Included are automobiles; trucks; buses; motorcycles; trains, subways, and other rail vehicles; aircraft; and ships, barges, and other waterborne vehicles. Vehicles whose primary purpose is not transportation (e.g., construction cranes and bulldozers, farming vehicles, and warehouse tractors and forklifts) are classified in the sector of their primary use')
                                ]),
                                html.H6('References', style={'color':'#2a3f5f'}),
                                html.P(children=[
                                      html.A('https://www.eia.gov/tools/glossary/ ',
                                         href='https://www.eia.gov/tools/glossary/',
                                         target='_blank')]),
                                html.P(children=[
                                      html.A('https://www.eia.gov/electricity/data.php',
                                          href='https://www.eia.gov/electricity/data.php',
                                          target='_blank')])
             ], style={'width':'90%', 'margin-left':'auto','margin-right':'auto'} )
    ]
)
@app.callback(
    Output("graph", "figure"),
    Input("sector_name", "value"),
    Input("state_1", "value"),
    Input("state_2", "value"),
    Input("state_3", "value"),
    Input("state_4", "value"),
    Input("state_5", "value"),
    Input("state_6", "value")
)
def plot_costs(input_sector, input_state1, input_state2, input_state3, input_state4, input_state5, input_state6):
    states = list((input_state1, input_state2, input_state3, input_state4, input_state5, input_state6))
    sub_df = df[df.Sector == input_sector]
    sub_df = sub_df[sub_df.State.isin(states)].sort_values(by='Year')
    fig = px.line(sub_df, x='Year', y='Price', color='State',
                  title=f"Average Price of Electricity in the {input_sector} Sector per kWh for US and selected States")
    fig.update_layout(title_x=0.5, yaxis_title="Price (Cents/kWh)", xaxis_range=[2009,2022])
    return fig

@app.callback(
    Output("tbl", "children"),
    Input("sector_name", "value"),
    Input("state_1", "value"),
    Input("state_2", "value"),
    Input("state_3", "value"),
    Input("state_4", "value"),
    Input("state_5", "value"),
    Input("state_6", "value")
)
def plot_costs(input_sector, input_state1, input_state2, input_state3, input_state4, input_state5, input_state6):
    states = list((input_state1, input_state2, input_state3, input_state4, input_state5, input_state6))
    sub_df = df[df.Sector == input_sector]
    sub_df = sub_df[sub_df.State.isin(states)].sort_values(by='Year')
    sub_df_table = sub_df.groupby(['Year','Sector']).mean().reset_index()
    sub_df_table = sub_df_table.round(2)
    sub_df_table.columns = ['Year','Sector','Average Revenue','Averege Sales', 'Average Number of Customers', 'Average Price per kWh']
    return dash_table.DataTable(sub_df_table.to_dict('records'),[{"name": i, "id": i} for i in sub_df_table.columns])

@app.callback(
    Output("table_title", "children"),
    Input("sector_name", "value"),
)
def table_title(input_sector):
    return f"Average Yearly Price per kWh, Revenue, Sales(Consumption), and Customers of Electricity in the {input_sector} Sector"


if __name__ == '__main__':
    app.run_server(debug=True)
    #app.run_server(host='localhost',port=8006)





