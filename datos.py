import pandas as pd
df=pd.DataFrame()

for d in range(1000):
	opcion = input("a. Registrar alumno\nb. Guardar y salir\t")
	if(opcion == "a"):
		nombre= input("Nombre: ")	
		apellidos= input("Apellidos: ")
		edad = input("Edad: ")
		grado = input("Grado: ")	
		grupo = input("Grupo: ")		
		correo = input("Correo electronico: ")
		data = {'Nombre':[nombre], 'Apellidos':[apellidos], 'Edad':[edad], 'Grado':[grado], 'Grupo':[grupo], 'Correo':[correo]}
		df=df.append(data, ignore_index =True)
	elif(opcion == "b"):
		print("Programa fializado")
		break
	else:
		print("opcion incorrecta")
df.to_csv("datos.csv")