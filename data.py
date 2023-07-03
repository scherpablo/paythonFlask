import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory


app= Flask(__name__)
app.secret_key= 'mysecretkey'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/carta') # '/'quiere decir pagina  principal
def carta():
    
    df= pd.read_excel("Libro.xlsx")
    df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
    df1.columns= ['tipo','producto', 'precio']

    return render_template("carta.html",df1 = df1)

@app.route('/pizza') # '/'quiere decir pagina  principal
def pizza():
    
    df= pd.read_excel("Libro.xlsx")
    df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
    df1.columns= ['tipo','producto', 'precio']
    pizzas=df1[df1['tipo']==' Pizza']

    return render_template("carta.html",df1 = pizzas)

@app.route('/empanada') # '/'quiere decir pagina  principal
def empanada():
    
    df= pd.read_excel("Libro.xlsx")
    df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
    df1.columns= ['tipo','producto', 'precio']
    empanadas=df1[df1['tipo']=='Empanada']
    
    return render_template("carta.html",df1 = empanadas)

@app.route('/milanesa') # '/'quiere decir pagina  principal
def milanesa():
    
    df= pd.read_excel("Libro.xlsx")
    df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
    df1.columns= ['tipo','producto', 'precio']
    milanesas=df1[df1['tipo']=='Milanesa']
    
    return render_template("carta.html",df1 = milanesas)

@app.route('/sandwich') # '/'quiere decir pagina  principal
def sandwich():
    
    df= pd.read_excel("Libro.xlsx")
    df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
    df1.columns= ['tipo','producto', 'precio']
    sandwiches=df1[(df1['tipo']=='Sandwich')|(df1['tipo']=='Hamburguesa')|(df1['tipo']=='Pancho')]

    
    return render_template("carta.html",df1 = sandwiches)

@app.route('/fritas') # '/'quiere decir pagina  principal
def fritas():
    
    df= pd.read_excel("Libro.xlsx")
    df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
    df1.columns= ['tipo','producto', 'precio']
    Fritas=df1[df1['tipo']=='Fritas']

    return render_template("carta.html",df1 = Fritas)

@app.route('/lookup', methods=['POST'])
def lookup():
    cadena=request.form["lookup"]
    cadena=cadena.lower()
    df= pd.read_excel("Libro.xlsx")
    df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
    df1.columns= ['tipo','producto', 'precio']
    df1['producto']=df1['producto'].str.lower()
    lookups= df1[df1["producto"].str.contains(r""+cadena+"" ,regex=True)]
        
    if len(lookups)==0:
        flash("No se ha encontrado coincidencia")
        return render_template("lookup.html", df1 = lookups)
        
    else:
        return render_template("lookup.html", df1 = lookups)
    
if __name__ == '__main__':
    app.run(debug=True)
    #index()
    #pizza()
