import sqlite3
from flask import Flask, g, jsonify, request, url_for
from math import ceil

def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}

def abrirConexion():
   if 'db' not in g:
      g.db = sqlite3.connect("datos.sqlite")
      g.db.row_factory = dict_factory
   return g.db

def cerrarConexion(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

app = Flask(__name__)
app.teardown_appcontext(cerrarConexion)

@app.route("/api/test")
def test():
    return "funcionando!"

@app.route("/api/sensor", methods=['POST'])
def sensor():
    datos = request.json
    Nombre = datos['Nombre']
    Valor = datos['Valor']
    db = abrirConexion()
    db.execute("INSERT INTO dates (Nombre, Valor) VALUES (?, ?);", (Nombre, Valor))
    db.commit()
    cerrarConexion()
    print(f"nombre del sensor {Nombre}, valor: {Valor}")
    return "OK"
