from flask import Flask, render_template
import random
import os
from .data import list

app = Flask(__name__) 
 
@app.route('/') 
def get_pokedex(): 
    return 'Hello, Pokedex!'
  
@app.route('/PokeneaInfo')
def get_pokenea_info():
    random_pokeneas = random.sample(list, 3)
    return render_template('pokeneasInfo.html', pokeneas=random_pokeneas)

@app.route('/PokeneaFrase')
def get_pokenea_frase():
    random_pokeneas = random.sample(list, 1)
    container_id = os.uname()[1]
    return render_template('pokeneaFrase.html', pokeneas=random_pokeneas, container=container_id)
