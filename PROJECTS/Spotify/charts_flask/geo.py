import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Initialize the dash app
app = dash.Dash(__name__)

# df_year = pd.read_csv(r'./Dataset/country_year_name.csv')
country_summary = pd.read_csv(r'./dataset/country_summary.csv')
df_year = pd.read_csv(r'./dataset/country_year_name.csv')

# Define the app layout
def create_layout2():
    return html.Div([
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in df_year['country_name'].unique()],
            value=df_year['country_name'].unique()[0],  # Set the default value
            style={'backgroundColor': 'white', 'color': 'black', 'width': '50%', 'marginBottom': '5px'},
            clearable=False,
        ),
        dcc.Graph(id='top-songs-graph', style={'width': '100%', 'height':'280px'})       
    ])
    

# Define callback to update Dash chart (Top 15 Songs chart)
def register_callbacks2(app):
    @app.callback(
        Output('top-songs-graph', 'figure'),
        Input('country-dropdown', 'value')
    )
    def update_dash_chart(selected_country2):
        filtered_ctry = df_year[df_year['country_name'] == selected_country2]
        top_songs = filtered_ctry.groupby(['song', 'artist']).size().reset_index(name='count')
        top_songs = top_songs.sort_values(by='count', ascending=False).head(15)

        # Create horizontal bar chart for Dash
        fig = px.bar(
            top_songs,
            x='song',
            y='count',
            color='song',
            labels={'song': 'Song', 'count': 'Frequency'},
            title=f'Top 15 Songs in {selected_country2}',
            text='artist',
            hover_data={'song': True, 'count': True, 'artist': True},
        )

        fig.update_layout(
            showlegend=False,
            title={
                'text': f'Country: {selected_country2}', 
                'x': 0.5,
                'xanchor': 'center', 
                'font': {'size': 18}
            }, 
            plot_bgcolor='rgb(30, 30, 30)',  # Dark background
            paper_bgcolor='rgb(30, 30, 30)',  # Dark paper background
            font=dict(color='white'),  # White font color
            xaxis=dict(
                showgrid=True,
                gridcolor='rgb(169, 169, 169)'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgb(169, 169, 169)', 
                showticklabels=False
            ),
            margin=dict(l=20, r=20, t=50, b=20),
        )
        fig.update_traces(
            textfont=dict(
                family='Arial',    # Change font family if needed
                size=8,          # Change font size
                color='black'     # Font color
            )
        )
        # Remove song name from x-axis labels
        fig.update_layout(
        xaxis={'tickvals': []}  # Hide x-axis labels (song names)
        )
        

        return fig

# Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8052)
    
# default browser: http://127.0.0.1:8052
# http://localhost:8052/