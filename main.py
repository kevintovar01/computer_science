# #menu
# from options_menu.hash_menu import hash_menu

from function_hash.hash_trasformation import HashTrasformation
from function_hash.hash_colisions import HashColision

# #menu hashs
# from options_menu.menu_function_hash import menu_hash_function
# from options_menu.menu_colisions import menu_hash_colisions

# from options_menu.menu_memory import menu_memory
# from options_menu.menu_structures import menu_structures 


# if __name__ == '__main__':
    # try:
    #     length, structure = menu_memory()
    #     if structure == 'Estructura parcial' or structure == 'Estructura total':
    #         my_hash = HashTrasformation(0, True)
    #         my_structure = length
    #         pass
    #     else:
    #         my_hash = HashTrasformation(length)
    #         hash_colisions = HashColision(my_hash)

    #     while True:
            
    #         function_hash, name_function = menu_hash_function(my_hash)

    #         if function_hash == True:
    #             print(name_function)
    #             break

    #         if structure == 'Estructura parcial' or structure == 'Estructura total':
    #             my_structure.function_hash = function_hash
    #             my_structure.my_hash = my_hash
    #             menu_structures(function_hash, name_function, my_hash, my_structure)
    #         else:    
    #             funtion_colision, name_colision = menu_hash_colisions(hash_colisions)
                
    #             if funtion_colision != True:
    #                 hash_menu(function_hash, name_function, funtion_colision, my_hash, name_colision)  
    # except:
    #     print("Salida Exitosa")




from flask import Flask, render_template, request, redirect, url_for

import sqlite3
import ast
import json
from ast import literal_eval



app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

my_hash = HashTrasformation(10)
colisions = HashColision(my_hash)

function = None
fuction_colision = None




@app.route('/') #route
def home():
    return render_template('home.html')

@app.route('/External_memory')
def external_memory():
    return render_template('external_memory.html')


"""Functions for Internal Memory"""
@app.route('/Internal_memory')
def internal_memory():
    return render_template('internal_memory.html')



@app.route('/Hash_fuctions')
def hash_fuctions():
    return render_template('hash_fuctions.html')


@app.route('/Hash', methods=['POST'])
def Hash():
    global function

    hash_fuction = request.form.get('hash_fuction')

    functions_hash = {
        'hash mod': my_hash.hash_function,
        'hash cuadrado': my_hash.hash_function_square,
        'hash truncamiento': my_hash.hash_truncamiento,
        'hash plegamiento multiplicacion': my_hash.hash_function_fold_multiplicative,
        'hash plegamiento suma': my_hash.hash_function_fold_additive
    }

    aux = function
    function = functions_hash[hash_fuction]
    if function != aux:
        my_hash.reset_list()
    
    context = {
        'name': hash_fuction,
        'hash': my_hash
    }
    return render_template('colisions_methods.html', **context)

@app.route('/Colisions', methods=['POST'])
def Colisions():
    global fuction_colision
    hash_fuction = request.form.get('hash_name')
    colision_fuction = request.form.get('colision_function')

    colision_hash = {
            'colision lineal': colisions.lineal_colision,
            'colision cuadratica': colisions.square_colision,
            'doble direccion hash': colisions.doble_direccion_hash,
            'arreglo anidado': colisions.arreglo_anidado,
            'lista encadenada': colisions.lista_encadenada
        }

    
    aux = fuction_colision
    fuction_colision = colision_hash[colision_fuction]

    if fuction_colision != aux:
        my_hash.reset_list()
    
    context = {
        'hash_name':hash_fuction,
        'colision_name': fuction_colision,
        'hash': my_hash
    }

    return render_template('hash_fuction.html', **context)


@app.route('/Operation', methods=['POST'])
def operations():
    operation = request.form.get('operations')
    name_colision = request.form.get('name_colision')
    value = int(request.form.get('value'))

    if operation == 'insert':
        my_hash.insert(value, function, fuction_colision, name_colision)
    elif operation == 'delete':
        my_hash.delete(value, function, fuction_colision, name_colision)  #fuction is our Hash
    else:
        my_hash.search(value, function, fuction_colision)

    return render_template('hash_fuction.html', hash=my_hash)




if __name__ == '__main__':
    app.run(debug=True) 
    
