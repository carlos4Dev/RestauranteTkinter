import sqlite3

def crear_bd():
	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()

	try:
		cursor.execute('''CREATE TABLE categoria(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL)''')
	except sqlite3.OperationalError:
		print("La tabla de Categorías ya existe.")
	else:
		print("La tabla de categorías se ha creado correctamente.")

	try:
		cursor.execute('''CREATE TABLE plato(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL,
				categoria_id INTEGER NOT NULL,
				FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
	except sqlite3.OperationalError:
		print("La tabla de Platos ya existe.")
	else:
		print("La tabla de Platos se ha creado correctamente.")
	conexion.close()

def agregar_categoria():
	categoria = input("¿Nombre de la nueva categoría?\n> ")

	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()

	try:
		cursor.execute("INSERT INTO categoria VALUES (null,'{}')".format(categoria))
	except sqlite3.IntegrityError:
		print("La categoria '{}' ya existe.".format(categoria))
	else:
		print("La categoría '{}' se ha creado corectamente.".format(categoria))
	conexion.commit()
	conexion.close()

def agregar_plato():
	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()

	categorias = cursor.execute("SELECT * FROM categoria").fetchall()
	print("Seleccione la categoría del plato que deseea añadir:")
	for categoria in categorias:
		print("[{}] {}".format(categoria[0], categoria[1]))

	categoria_usuario = int(input("> "))

	plato = input("¿Nombre del nuevo plato?\n> ")

	try:
		cursor.execute("INSERT INTO plato VALUES (null,'{}','{}')".format(plato, categoria_usuario))
	except sqlite3.IntegrityError:
		print("El plato '{}' ya existe.".format(plato))
	else:
		print("El plato '{}' se ha creado corectamente.".format(plato))

	conexion.commit()
	conexion.close()

def mostrar_menu():
	conexion = sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()

	categorias = cursor.execute("SELECT * FROM categoria").fetchall()
	for categoria in categorias:
		print("\n********",categoria[1],"********")
		print("**************************")
		platos = cursor.execute("SELECT * FROM plato WHERE categoria_id = {}"\
				.format(categoria[0])).fetchall()
		for plato in platos:
			print("\t{}".format(plato[1]))

	conexion.close()

# Creamos la base de datos
crear_bd()

# Menú de opciones del programa
while True:
	print("\nGestor restaurantes version 1.0")
	opcion = input("\nIntroduce una opción:\n[1] Agregar una categoria\
					\n[2] Agregar un plato\
					\n[3] Mostrar el menú\
					\n[4] Salir del programa\n\n> ")

	if opcion == "1":
		agregar_categoria()

	elif opcion=="2":
		agregar_plato()

	elif opcion=="3":
		mostrar_menu()

	elif opcion=="4":
		print("Ha elegido salir del programa. Que tenga un buen día.\n")
		break

	else:
		print("Opción incorrecta")