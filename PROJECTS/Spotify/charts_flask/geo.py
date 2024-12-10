import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Initialize the dash app
app = dash.Dash(__name__)

# df_year = pd.read_csv(r'./Dataset/country_year_name.csv')
country_summary = pd.read_csv(r'./Dataset/country_summary.csv')
df_year = pd.read_csv('./Dataset/country_year_name.csv')

# Define the app layout
def create_layout2():
    return html.Div([
        html.H1("Top 15 Songs I Listened to by Location", style={'textAlign': 'center', 'color': 'white'}),

        # Layout for side-by-side charts using Flexbox
        html.Div([
            # Left side - Static Plotly scatter plot (Spotify usage chart)
            html.Div([
                dcc.Graph(
                    id='spotify-usage-chart',
                    figure=px.scatter(
                        country_summary, x='country_name', y='total_minutes',
                        size='total_songs', color='total_songs', size_max=100,
                        hover_name='country_name', title='Total Spotify Usage based on Location (Country)',
                        labels={
                            'total_minutes': 'Total Minutes',
                            'country_name': 'Country',
                            'total_songs': 'Total Songs'
                        }
                    ).update_layout(
                        title={
                            'text': 'Total Spotify Usage based on Location',
                            'x': 0.5,
                            'xanchor': 'center',
                            'font': {'size': 25, 'weight': 'bold'}
                        },
                        plot_bgcolor='rgb(30, 30, 30)',  # Dark background
                        paper_bgcolor='rgb(30, 30, 30)',  # Dark paper background
                        font=dict(color='white'),  # White font color
                        height=550,  # Adjust height
                        # width=550,
                        xaxis=dict(
                            showgrid=True,
                            gridcolor='rgb(169, 169, 169)',
                            tickangle=45
                        ),
                        yaxis=dict(
                            showgrid=True,
                            gridcolor='rgb(169, 169, 169)'
                        )
                    )
                )
            ], style={'flex': '1', 'padding': '0 10px'}),  # Flex to make both divs occupy equal space

            # Right side - Dropdown and Dash chart
            html.Div([
                dcc.Dropdown(
                    id='country-dropdown',
                    options=[{'label': country, 'value': country} for country in df_year['country_name'].unique()],
                    value=df_year['country_name'].unique()[0],  # Set the default value
                    style={'backgroundColor': 'pink', 'color': 'black', 'width': '200px', 'marginTop': '10px', 'marginBottom': '10px'},
                    clearable=False,
                ),
                dcc.Graph(id='top-songs-graph')
            ], style={'flex': '1', 'padding': '0 10px'})  # Flex to make both divs occupy equal space
        ], style={'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flextstart'})  # Flexbox for side-by-side layout
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
            y='song',
            x='count',
            color='song',
            labels={'song': 'Song', 'count': 'Frequency'},
            title=f'Top 15 Songs in {selected_country2}',
            text='artist',
            hover_data={'song': True, 'count': True, 'artist': True},
            orientation='h'
        )

        fig.update_layout(
            showlegend=False,
            title={
                'text': f'Top 15 Songs in {selected_country2}', 
                'x': 0.5,
                'xanchor': 'center', 
                'font': {'size': 30, 'weight': 'bold'}
            }, 
            plot_bgcolor='rgb(30, 30, 30)',  # Dark background
            paper_bgcolor='rgb(30, 30, 30)',  # Dark paper background
            font=dict(color='white'),  # White font color
            height=500,  # Adjust height
            # width=550,  # Set the width
            xaxis=dict(
                showgrid=True,
                gridcolor='rgb(169, 169, 169)'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgb(169, 169, 169)', 
                showticklabels=False
            )
        )
        fig.update_traces(textfont_color='white')

        return fig

# Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8052)
    
# default browser: http://127.0.0.1:8052
# http://localhost:8052/