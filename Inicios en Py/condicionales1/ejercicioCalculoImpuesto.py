salario = float(input("ingrese el salario anual: "))

if salario > 0:
 if salario > 50000:
     if salario > 100000:
         print ("El impuesto es del 30%")
     else: 
         print ("El impuesto es del 20%")
 else:
     print ("No pagan impuesto")
else:
   print("salario no valido")