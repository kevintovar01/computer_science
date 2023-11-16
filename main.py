from function_hash.hash_trasformation import HashTrasformation
from function_hash.hash_colisions import HashColision
from memorys.EstructurasParciales import Est_Parcial
from search.search import Search

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

my_hash = None
colisions = None
digits = None
my_structure = None

function = None
hash_fuction = None

fuction_colision = None


register = {}




@app.route('/') #route
def home():
    global my_hash, colisions, digits, my_structure, function, fuction_colision, hash_fuction, register
    my_hash = None
    colisions = None
    digits = None
    my_structure = None

    function = None
    hash_fuction = None
    register = {}
    fuction_colision = None
    return render_template('home.html')

@app.route('/External_memory', methods=['GET', 'POST'])
def external_memory():
    type = request.args.get('type')
    print(type)

    if type == 'Hashing Dinamico':
        return render_template('external_memory.html', aux=True)
    else:
        pass
        
    return render_template('external_memory.html', aux=False)


@app.route('/Conditions', methods=['GET','POST'])
def conditions():
    global my_structure
    if request.method == 'POST':
        cube = int(request.form.get('cube'))
        tasa_expansion = int(request.form.get('tasa_expansion'))
        tasa_reduccion = int(request.form.get('tasa_reduccion'))
        row = int(request.form.get('row'))
        structure = request.form.get('structure')
        digits = request.form.get('digits')
    else:
        structure = request.args.get('structure')
        return render_template('conditions.html' , structure=structure)

    if structure == 'None':
        structure = my_structure.tipo_expansion

    my_structure = Est_Parcial(cube,row,tasa_expansion,tasa_reduccion, structure)
    my_structure.function_hash = function
    my_hash.length = cube
    my_structure.my_hash = my_hash

    

    context = {
        'my_structure': my_structure,
        'structure': structure,
        'digits': digits
    }
    return render_template('view_structures.html',**context)


@app.route('/dinamic_structures', methods=['POST'])
def view_structures():
    global function
    global my_hash
    global register
    operation = request.form.get('operations')
    value = int(request.form.get('value'))
    name = request.form.get('nombre')
    last_name = request.form.get('apellido')
    digits = request.form.get('digits')
    
    aux = value

    if operation == 'insert':
        messages, value, index = my_hash.insert(value, function)
        value, messages = my_structure.agregar_clave(index, value)
        register[aux] = name,last_name
    elif operation == 'delete':
        value, messages= my_structure.eliminar_clave(value)  #fuction is our Hash
    elif operation == 'search':
        messages=my_structure.buscar_clave(value)
        
        if messages == False:
            messages = f"La clave {value} no fue encontrada en la estructura"
        elif messages["tipo"] == "Memoria Principal":
            messages = f"El valor {value} se encontro en la columna {messages['indice']} fila {messages['fila']}"
            messages += f" la clave esta vinculada al siguiente registro {register[aux]}"
        else:
            messages = f"El valor se encontro en la estructura de colisiones posicion {messages['posicion']}"
            messages += f" la clave esta vinculada al siguiente registro {register[aux]}"
       
    else:
        digits = value
        messages = 'La longitud a sido cambiada'
        my_hash.reset_list()
        register = {}

    context = {
                'hash': my_hash,
                'message': messages,
                'my_structure': my_structure,
                'structure': my_structure.tipo_expansion,
                'digits':digits,
                'aux':True
            }

    return render_template('view_structures.html', **context)


"""Functions for Internal Memory"""
@app.route('/Internal_memory', methods=['GET', 'POST'])
def internal_memory():
    aux = False
    
    if request.method == 'POST':

        global my_hash
        global colisions
        length = int(request.form.get('size'))
        my_hash = HashTrasformation(length)
        colisions = HashColision(my_hash)
        aux = True

    return render_template('internal_memory.html', length=aux)


@app.route('/Hash_fuctions', methods=['GET'])
def hash_fuctions():
    is_structure = request.args.get('structure')
    return render_template('hash_fuctions.html', structure=is_structure)


@app.route('/Binary_search')
def binary_search():
    global my_hash
    my_hash = Search(my_hash.length)

    search_type = request.args.get('type_search')
    context = {
        'hash': my_hash,
        'search_type': search_type,
        'aux':False
    }
    return render_template('hash_fuction.html', **context)




@app.route('/Hash', methods=['GET','POST'])
def hash():
    global function
    global my_hash
    global hash_fuction
    hash_truncamiento = None
    temp = hash_fuction
    hash_fuction = request.form.get('hash_fuction')
    
    if hash_fuction == None:
        hash_truncamiento = request.form.get('hash_truncamiento')
        if hash_truncamiento != None:
            hash_fuction = "hash truncamiento"
        else:
            hash_fuction = temp

        print(hash_truncamiento)
        


    is_structure = request.form.get('structure')

    if is_structure == 'None' and my_structure != None:
        is_structure = my_structure.tipo_expansion

    print(is_structure)
    if is_structure != 'None':
        my_hash = HashTrasformation(0, True)
        

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
        register = {}
    
    if hash_truncamiento == '0' or hash_truncamiento == '1':
        my_hash.order = int(hash_truncamiento)
    
    


    if is_structure != 'None':
        context = {'name': hash_fuction,'hash': my_hash, 'structure':is_structure}
        return render_template('conditions.html', **context)
    

    context = {
        'name': hash_fuction,
        'hash': my_hash
    }



    return render_template('colisions_methods.html', **context)

@app.route('/Colisions', methods=['GET','POST'])
def Colisions():
    print("La ruta /Colisions fue llamada")
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
        'colision_name': colision_fuction,
        'hash': my_hash,
        'aux': False
    }
    return render_template('hash_fuction.html', **context)


@app.route('/verification', methods=['POST'])
def veryfication():
    global digits
    aux = request.form.get('aux')
    digits = int(request.form.get('value'))
    search_type = request.form.get('aux')
    colision_name = request.form.get('colision_name')

    if aux == 'binary_searh':
        context = {'hash':my_hash, 'digits': digits, 'aux': 'binary_searh'}
        return render_template('hash_fuction.html', **context)

    print(digits)
    context = {
                'hash': my_hash,
                'digits':digits,
                'colision_name':colision_name,
                'search_type': search_type,
                'aux':True
            }
    return render_template('hash_fuction.html', **context)
    

@app.route('/Operation', methods=['POST'])
def operations():
    global digits
    global register

    operation = request.form.get('operations')
    colision_name = request.form.get('colision_name')
    name_colision = request.form.get('name_colision')
    value = int(request.form.get('value'))
    name = request.form.get('nombre')
    last_name = request.form.get('apellido')



    print(value)
    aux = value
    if operation == 'insert':
        messages, value, index = my_hash.insert(value, function, fuction_colision, name_colision)
        register[aux] = name, last_name
    elif operation == 'delete':
        messages= my_hash.delete(value, function, fuction_colision, colision_name)  #fuction is our Hash
    elif operation == 'search':
        value, index, messages=my_hash.search(value, function, fuction_colision)
        messages += f" la clave esta vinculada al siguiente registro {register[aux]}"
    else:
        digits = value
        messages = 'La longitud a sido cambiada'
        my_hash.reset_list()
        register = {}

    context = {
                'hash': my_hash,
                'message': messages,
                'colision_name':colision_name,
                'digits':digits,
                'aux':True
            }

    return render_template('hash_fuction.html', **context)


@app.route('/Binary_operation', methods=['POST'])
def binary_operation():
    global digits
    global register
    operation = request.form.get('operations')
    name = request.form.get('nombre')
    last_name = request.form.get('apellido')
    try:
        value = int(request.form.get('value'))
    except:
        print("value null")
        
    search_type = request.form.get('search_type')
    
    print(search_type)

    index = value

    if operation == 'insert':    
        messages = my_hash.append_list(value)
        register[index] = name, last_name 
        
        # messages = f"La clave {value} ha sido insertada"
    elif operation == 'delete':
        messages= my_hash.delete(value)  #fuction is our Hash
    elif operation == 'sort':
        messages = my_hash.bubble_sort()
    elif operation == 'search':
        if search_type == 'Secuencial':
            messages = my_hash.sequence_search(value)
            messages += f" la clave esta vinculada al siguiente registro {register[index]}"
        else:
            aux = my_hash.bubble_sort()
            messages = my_hash.binary_search(value)
            messages += aux+", antes de la busqueda,"
            messages += f" la clave esta vinculada al siguiente registro {register[index]}"
    else:
        digits = value
        messages = 'La longitud a sido cambiada'
        my_hash.memory = []
        register = {}


    context = {
                'hash': my_hash,
                'message': messages,
                'digits':digits,
                'search_type': search_type,
                'aux':True
            }

    return render_template('hash_fuction.html', **context)


@app.route('/index')
def index():
    return render_template(
        'index.html',
    )


if __name__ == '__main__':
    app.run(debug=True) 
    
