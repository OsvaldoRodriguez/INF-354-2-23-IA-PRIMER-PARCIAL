from kanren import facts, Relation, var, run
import numpy as np
#son declaraciones de variables especiales, que sierven para trabajar con las relaciones
a = var() 
b = var()

#Relacion padres
padres = Relation()
facts (padres, 
      ("Martha", "Nora"), ("Martha", "Felix"), ("Martha", "Heriberto"), ("Martha", "Samuel"), ("Martha", "Raul"), ("Martha", "Lidia"), ("Martha", "Sofia"),
      ("Marcelino", "Nora"), ("Marcelino", "Felix"), ("Marcelino", "Heriberto"), ("Marcelino", "Samuel"), ("Marcelino", "Raul"), ("Marcelino", "Lidia"), ("Marcelino", "Sofia"),
      
      ("Pedro", "Nelson"), ("Pedro", "Osvaldo"), ("Pedro", "Oliver"), ("Pedro", "Elsa"),
      ("Nora", "Nelson"),  ("Nora", "Osvaldo"), ("Nora", "Oliver"), ("Nora", "Elsa"),
       
      ("Samuel", "Alexandro"),
      ("Norah", "Alexandro"),
       
      ("Lidia", "Alizon"), ("Lidia", "Abigail"),
      ("David", "Alizon"), ("David", "Abigail"),
       
      ("Sofia", "Damaris"), ("Sofia", "Claudia"), ("Sofia", "Joel"),
      ("Jaime", "Damaris"), ("Jaime", "Claudia"), ("Jaime", "Joel"),
      
      ("Nelson", "Kadosh"), ("Nelson", "Emmanuel"), ("Nelson", "Linda"),
      ("Ximena", "Kadosh"), ("Ximena", "Emmanuel"), ("Ximena", "Linda"),
       
      ("Elsa", "Eitan"),
)

#Relacion abuelos
abuelos = Relation()
facts (abuelos, 
       ("Marcelino", "Nelson"), ("Marcelino", "Osvaldo"), ("Marcelino", "Oliver"), ("Marcelino", "Elsa"),
       ("Martha", "Nelson"), ("Martha", "Osvaldo"), ("Martha", "Oliver"), ("Martha", "Elsa"),

       ("Martha", "Alexandro"),
       ("Marcelino", "Alexandro"),
      
      ("Martha", "Alizon"), ("Martha", "Abigail"),
      ("Marcelino", "Alizon"), ("Marcelino", "Abigail"),
      
      ("Martha", "Damaris"), ("Martha", "Claudia"), ("Martha", "Joel"),
      ("Marcelino", "Damaris"), ("Marcelino", "Claudia"), ("Marcelino", "Joel"),
      
      ("Nora", "Kadosh"), ("Nora", "Emmanuel"), ("Nora", "Linda"),
      ("Pedro", "Kadosh"), ("Pedro", "Emmanuel"), ("Pedro", "Linda"),
       
)

def eliminando_repetidos(datos):
  return list(set(datos))

def padres_go(persona):
  res = run(0, a, padres(a, persona))
  return eliminando_repetidos(res)

def hijos_go(persona):
  res = run(0, a, padres(persona, a))
  return eliminando_repetidos(res)


def abuelos_go(persona):
  res = run(0, a, abuelos(a, persona))
  return eliminando_repetidos(res)

def tios_go(persona):
  # para encontrar los tios, hallamos los abuelos y luego buscamos a sus hijos que no sea el papa
  papas = padres_go(persona)
  abuelos = abuelos_go(persona)

  res = []
  for abu in abuelos:
    hijo_abu = run(0, b, padres(abu, b))
    for datos in hijo_abu:
      if not datos in papas:
        res.append(datos)
  return eliminando_repetidos(res)



def primos_go(persona):
  tios = tios_go(persona)
  res = []
  for tio in tios:
    hijo_de_tio = run(0, b, padres(tio, b))
    for datos in hijo_de_tio:
      res.append(datos)
  return eliminando_repetidos(res)

def hermanos_go(persona):
  papas = padres_go(persona)

  res = []
  for papa in papas:
    hijo_papa = run(0, b, padres(papa, b))
    for datos in hijo_papa:
      if not datos == persona:
        res.append(datos)
  return eliminando_repetidos(res)

def sobrinos_go(persona):
  hermanos = hermanos_go(persona)
  res = []
  for hermano in hermanos:
    hijo_hermano = run(0, b, padres(hermano, b))
    for datos in hijo_hermano:
      res.append(datos)
  return eliminando_repetidos(res)


def nietos_go(persona):
  hijos = hijos_go(persona)
  res = []
  for hijo in hijos:
    hijo_del_hijo = run(0, b, padres(hijo, b))
    for datos in hijo_del_hijo:
      if not datos in hijos:
        res.append(datos)
  return eliminando_repetidos(res)




def calcularTodo(persona):
  print("Datos de ", persona)
  print('Padres', padres_go(persona))
  print('Abuelos', abuelos_go(persona))
  print('Hijos', hijos_go(persona))
  print('Tios', tios_go(persona))
  print('Primos', primos_go(persona))
  print('Hermanos', hermanos_go(persona))
  print('Sobrinos', sobrinos_go(persona))
  print('Nietos', nietos_go(persona))
  print()
personas = ["Osvaldo", "Nelson", "Oliver", "Kadosh", "Damaris", "Alexandro", "Nora", "Elsa"]

for _ in personas:
  calcularTodo(_)

