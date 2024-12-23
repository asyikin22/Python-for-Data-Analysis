import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

file_path = 'PROJECTS/Book/Goodreads.csv'

book_rating = pd.read_csv(file_path)

# print(book_rating.head())

#define minor genress
minor_genres = ['Economy', 'Dystopian', 'Biography', 'Photography', 'Feminism', 'Politics', 'Humor', 'Drama']

#Create grouped_genre column
book_rating['Grouped_Genre'] = book_rating['Genre'].apply(lambda x: 'Others' if x in minor_genres else x)

#initialize dash app 
app = Dash(__name__)

#define app layut 
app.layout = html.Div(style={'backgroundColor': '#1e1e1e'}, children=[
    html.Div(style={'position': 'relative', 'width': '100%', 'height':'500px'}, children=[
        
        #dropdown positioned absolutely within chart container
        html.Div(style={'position': 'absolute', 'top':'20px', 'left': '20px', 'z-index':'1', 'width':'200px', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            html.Label('Select Genre', style={'color': 'salmon', 'fontSize': 14, 'display': 'block', 'textAlign': 'center', 'marginRight': '50px'}),
            dcc.Dropdown(
                id='genre-dropdown',
                options=[{'label': genre, 'value': genre} for genre in book_rating['Grouped_Genre'].unique()],
                value = 'Faith',
                style={'width': '100px', 'height':'30px', 'display': 'inline-block', 'fontSize': 12, 'marginRight': '50px'},
                clearable=False
            )
        ]),
         dcc.Graph(id='genre-bar-chart', style={'height': '100%'})
    ])     
])

#define callback to update the bar chart
@app.callback(
    Output('genre-bar-chart', 'figure'),
    Input('genre-dropdown', 'value')
)

def update_chart(selected_genre):
    genre_books = book_rating[book_rating['Grouped_Genre'] == selected_genre].sort_values(by='Num_rating')

    fig = go.Figure()
    
    fig.add_trace(
        go.Bar(
            x=genre_books['Num_rating'],
            y=genre_books['Title'],
            orientation='h',
            text=genre_books['Title'],
            textposition='inside',
            hovertext=genre_books['Author'],
            hovertemplate=(
                "<b>%{text}</b><br>"  # Title is bold and at the top
                "Author: %{hovertext}<br>"  # Author comes after the title
                "<extra></extra>"  # Removes extra hover information (like the legend)
            ),
            marker=dict(
                color=genre_books['Num_rating'],
                colorscale='Viridis', 
                showscale=True,
                colorbar=dict(
                    title='',
                    thickness=15
                )
            )
        )
    )
    
    title_text = f'Goodreads Ratings: <span style="color: fuchsia";>{selected_genre}</span>'
    
    fig.update_layout(
        template='plotly_dark',
        title=title_text,
        title_x=0.5,
        title_font_size=15,
        title_font_color= 'yellow',
        xaxis_title='Number of Ratings (Log Scale)',
        yaxis_title='Book Title',
        xaxis_title_font=dict(size=10),
        width=800,
        height=520,
        yaxis=dict(showticklabels=False),  # Hide y-axis labels
        margin=dict(l=10, r=10, t=70, b=10), 
    )
    
    fig.update_xaxes(type="log")

    return fig

# default browser: http://127.0.0.1:8055

if __name__ == '__main__':
    app.run_server(debug=False, port=8055)