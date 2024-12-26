import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Initialize Dash app
app = dash.Dash(__name__)

state_eth_gen = pd.read_excel(r"./Dataset_pop/comb_state_ethno_gen.xlsx")

# App layout
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Label("Select State:"),
            dcc.Dropdown(
                id='state-dropdown',
                options=[{'label': state, 'value': state} for state in state_eth_gen['State'].unique()],
                value=state_eth_gen['State'].iloc[0]  # Default value
            )
    ], style={'display': 'inline-block', 'width': '45%', 'margin-right': '10%'}),
    
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': year, 'value': year} for year in state_eth_gen['Year'].unique()],
            value=state_eth_gen['Year'].iloc[0]  # Default value
            ),
        ], style={'display': 'inline-block', 'width': '45%'}), 
    ]),  
    dcc.Graph(id='population-bar-chart'),
], style={'maxWidth': '1000px', 'margin': '0 auto', 'padding': '20px'})

# Callback for updating the chart
@app.callback(
    Output('population-bar-chart', 'figure'),
    [Input('state-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_chart(selected_state, selected_year):
    # Filter data based on selection
    filtered_df = state_eth_gen[(state_eth_gen['State'] == selected_state) & (state_eth_gen['Year'] == selected_year)]
    
    # Prepare data for bar chart
    categories = ['Bumi_M', 'Chi_M', 'Ind_M', 'Other_M', 'Bumi_F', 'Chi_F', 'Ind_F', 'Other_F']
    values = filtered_df[categories].values.flatten()
    labels = ['Bumi Male', 'Chinese Male', 'Indian Male', 'Other Male',
              'Bumi Female', 'Chinese Female', 'Indian Female', 'Other Female']

    # Create bar chart
    fig = px.bar(
        x=labels,
        y=values,
        labels={'x': 'Population Category', 'y': 'Population Count'},
        template='plotly_dark'
    )
    fig.update_traces(
        textposition='outside',
            hovertemplate=(
            "<b>Category:</b> %{x}<br>" +
            "<b>Population:</b> %{y}k <br>" +
            f"<b>State:</b> {selected_state}<br>" +
            f"<b>Year:</b> {selected_year}<extra></extra>"
        )
    )
    
    fig.update_layout(
        xaxis_title="Category", yaxis_title="Population (in thousands)", title_x=0.5,
        title={
            'text': (
                f"<span style='color:fuchsia; font-weight:bold;'>{selected_state}</span>"
                f"<span> in </span>"
                f"<span style='color:yellow; font-weight:bold;'>{selected_year}</span>"
            ), 
            'x': 0.5,
            'xanchor': 'center',
            'font': {
                'size': 32
            }  
        },
        margin={'t': 100},
    )
    
    
    # Define custom colors for bars
    custom_colors = ['#33FF57', '#FF5733', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#FF8C00', '#FF3333']

    # Update bar colors
    fig.update_traces(marker=dict(color=custom_colors))
    
    return fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True, port=8043)
    
# default browser: http://127.0.0.1:8043