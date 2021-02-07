import sqlite3
from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("BitBrasas - Fin de semana")
root.resizable(0,0)
root.config(bd=30, relief="groove")

Label(root, text="     Restaurante BitBrasas    ", fg="darkblue", 
	font=("Trebuchet",28,"bold italic")).pack()
Label(root, text="Menú fin de semana", fg="blue", 
	font=("Bodoni",24,"bold italic")).pack()

# Espacio en blanco para separar los títulos y las categorías
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# Buscar las categorías y platos de la bd
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
	Label(root, text=categoria[1], fg="blue", font=("Verdana",20,"bold italic")).pack()
	platos = cursor.execute("SELECT * FROM plato WHERE categoria_id = {}"\
			.format(categoria[0])).fetchall()
	for plato in platos:
		Label(root, text=plato[1], fg="darkblue", font=("Georgia",15,"italic")).pack()

	# Separación entre categorías
	Label(root, text="").pack()

# Precio del menú
Label(root, text="30€ (IVA incluido)", fg="darkblue", font=("Bodoni", 20,"bold italic")).pack(side="right")

conexion.close()

# Finalmente ejecutamos el bucle
root.mainloop()