import dash
from flask import Flask, render_template
import pandas as pd
from charts_flask.Yearly_Artist_Song import create_layout1, register_callbacks1   
from charts_flask.geo import create_layout2, register_callbacks2
from multiprocessing import Process

#initialize flask app
server = Flask(__name__)

#first dash app running on /dash1
app1 = dash.Dash(__name__, server=server, url_base_pathname='/dash1/')
app1.layout = create_layout1()
register_callbacks1(app1)

# #second dash app running on /dash2
app2 = dash.Dash(__name__, server=server, url_base_pathname='/dash2/')
app2.layout = create_layout2()
register_callbacks2(app2)

# Home route for Flask
@server.route('/')
def home():
    return render_template('index.html')  # Ensure you have an index.html in templates/

# function to run apps on different ports
def run_app1():
    app1.run_server(debug=True, port=8060, use_reloader=False)
    
def run_app2():
    app2.run_server(debug=True, port=8052, use_reloader=False)
    

if __name__ == '__main__':

    p1 = Process(target=run_app1)
    p2 = Process(target=run_app2)
    
    p1.start()
    p2.start()
    
    server.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)  # Flask will run on port 5000
    
    p1.join()
    p2.join()
   