x = [ [5, 2, 3], [10, 8, 9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1. Actualizar valores
matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6
print(matriz)

# Cambiar nombre
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

# Cambiar Cancun por Monterrey
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print(ciudades)

# Cambiar latitud
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

print("-" * 20)

# 2. Iterar lista diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:
        salida = ""
        for llave, valor in diccionario.items():
            salida += f"{llave} - {valor}, "
        # Quitar ultima coma y espacio
        print(salida[:-2])

cantantes_lista = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes_lista)
print("-" * 20)

# 3. Obtener valores lista
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])
        else:
            print(f"La llave '{llave}' no existe.")

iterarDiccionario2("nombre", cantantes_lista)
print("-" * 10)
iterarDiccionario2("pais", cantantes_lista)

print("-" * 20)

# 4. Iterar diccionario con listas
def imprimirInformacion(diccionario):
    for llave, lista_valores in diccionario.items():
        print(f"{len(lista_valores)} {llave.upper()}")
        for valor in lista_valores:
            print(valor)
        print("") # Espacio vacio

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)