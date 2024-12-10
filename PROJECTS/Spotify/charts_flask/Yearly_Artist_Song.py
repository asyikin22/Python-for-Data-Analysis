import dash 
from dash import dcc, html
import plotly.express as px
import pandas as pd

top_artist_per_year = pd.read_csv(r'./dataset/top_artist_2014_2024.csv', encoding='latin1')
top_songs_per_year = pd.read_csv(r'./dataset/top_song_2014_2024.csv', encoding='latin1')

#create plotly figure for top artist
def create_figure_artist(year):
    filtered_df = top_artist_per_year[top_artist_per_year['year'] == year]
    fig = px.bar(
        filtered_df,
        y='song_count', x='artist',
        orientation='v',
        title= f'Top Artist for {year}',
        color='artist',
        labels={'song_count': 'song count'},
        text='artist'
    )
    
    fig.update_layout(
        xaxis_title='Artist', yaxis_title='Song count', showlegend=False,
        title={
            'text': f'Top Artist for {year}', 
            'x': 0.5,
            'xanchor':'center', 
            'font': {
                'size': 30, 
                'weight': 'bold',
                'color': 'pink'
            }},
        plot_bgcolor='rgb(30, 30, 30)', 
        paper_bgcolor='rgb(30, 30, 30)',
        font={'color': 'white'},
        xaxis=dict(
            tickfont={'color': 'white'},
            showticklabels=False
        ),
        yaxis=dict(
            tickfont={'color': 'white'},
        ),
    )
    
    return fig

#create plotly figure for top song

def create_figure_song(year):
    filtered_df = top_songs_per_year[top_songs_per_year['year'] == year]
    fig = px.bar(
        filtered_df,
        y='play_count', x='song',
        orientation='v',
        color='song',
        title=f'Top Songs for {year}',
        labels={'play_count': 'Number of Times Played'},
        hover_data={'artist': True, 'play_count': True},
        text='artist'
    )
    fig.update_layout(
        xaxis_title='Song', yaxis_title='Song Count', showlegend=False,
        title={
            'text': f'Top Songs for {year}', 
            'x': 0.5, 'xanchor': 'center',
            'font': {'size': 30, 'weight': 'bold', 'color': 'pink'}
        },
         plot_bgcolor='rgb(30, 30, 30)', 
            paper_bgcolor='rgb(30, 30, 30)',
            font={'color': 'white'},
            xaxis=dict(
                tickfont={'color': 'white'},
                tickangle=40
            ),
            yaxis=dict(
                tickfont={'color': 'white'},
            ),
    )
    fig.update_traces(textfont_color='white')
    
    return fig

# Layout of the app
def create_layout1():
    return html.Div([
        # Create a flex container for both charts and dropdowns
        html.Div([
            # Section for Artist Dropdown and Chart
            html.Div([
                html.Label('Select Artist Year', style={'color': 'black', 'fontSize': 18, 'textAlign': 'center'}),
                dcc.Dropdown(
                    id='artist-year-dropdown',
                    options=[{'label': year, 'value': year} for year in top_artist_per_year['year'].unique()],
                    value=2014,
                    style={'backgroundColor': 'white', 'color': 'black', 'width': '150px', 'marginTop': '10px', 'marginBottom': '10px'},
                    clearable=False
                ),
                dcc.Graph(id='artist-bar-chart')
            ], style={'flex': 1, 'padding': '20px'}),  # This will take 50% width by default

            # Section for Song Dropdown and Chart
            html.Div([
                html.Label('Select Song Year', style={'color': 'black', 'fontSize': 18, 'textAlign': 'center'}),
                dcc.Dropdown(
                    id='song-year-dropdown',
                    options=[{'label': year, 'value': year} for year in top_songs_per_year['year'].unique()],
                    value=2014,
                    style={'backgroundColor': 'white', 'color': 'black', 'width': '150px', 'marginTop': '10px', 'marginBottom': '10px'},
                    clearable=False
                ),
                dcc.Graph(id='song-bar-chart')
            ], style={'flex': 1, 'padding': '20px'}),  # This will take 50% width by default
        ], style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-around', 'padding': '20px'}),
    ])

def register_callbacks1(app):
    # Callback for updating Artist Chart
    @app.callback(
        dash.Output('artist-bar-chart', 'figure'),
        [dash.Input('artist-year-dropdown', 'value')]
    )
    def update_chart_artist(selected_year):
        return create_figure_artist(selected_year)

    # callback for updating song chart
    @app.callback(
        dash.Output('song-bar-chart', 'figure'),
        [dash.Input('song-year-dropdown', 'value')]
    )

    def update_chart_song (selected_year):
        return create_figure_song(selected_year)

#run the app
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8060)
    
# default browser: http://127.0.0.1:8060
# http://localhost:8060/