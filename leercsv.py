import pandas as pd
archivo = input("nombre del archivo a leer\t")
dl = pd.read_csv(archivo)#linea para leer un archivo csv
print ("\n")
print(dl)