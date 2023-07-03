import pandas as pd

df= pd.read_excel("Libro.xlsx")
df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
df1.columns= ['tipo','producto', 'precio']
pizzas=df1[df1['tipo']==' Pizza']
Fritas=df1[df1['tipo']=='Fritas']
sandwiches=df1[(df1['tipo']=='Sandwich')|(df1['tipo']=='Hamburguesa')|(df1['tipo']=='Pancho')]


df1['producto']=df1['producto'].str.lower()
lookup= df1[df1["producto"].str.contains(r"Jam" ,regex=True)]

print(lookup)
#print(len(empanadas))
#print(Fritas)
#print(len(Fritas))


"""
tipo=[]
producto=[]
precio=[]

for i in range(len(df1)):
    tipo.append(df1.iloc[i][0])
    producto.append(df1.iloc[i][1])
    precio.append(df1.iloc[i][2])


carta={"tipo": tipo, 'producto':producto, 'precio': precio}

for a in carta.items():
   print(carta["precio"][1])


print(df1.columns)
print(df1["producto"][0])


for a in range(len(pizzas)):
    print(pizzas.iloc[a]["tipo"])
    print(pizzas.iloc[a]["producto"])
    print(pizzas.iloc[a]["precio"])"""