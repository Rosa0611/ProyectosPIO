'''
'''

def operaciones (a,b):
 def suma ():
    return a + b

 def resta ():
    return a - b
 
 resultadoSuma = suma ()
 resultadoResta = resta ()

 return resultadoSuma, resultadoResta

resulsuma , resulresta = operaciones (12, 6)

print (f"Resultado de la suma es: {resulsuma} y resta {resulresta}")