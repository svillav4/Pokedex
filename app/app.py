from flask import Flask, render_template
import random
from data import list
 
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
    random_pokeneas = random.sample(list, 3)
    return render_template('pokeneaFrase.html', pokeneas=random_pokeneas)
    
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=80, debug=True)