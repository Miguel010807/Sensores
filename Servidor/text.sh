#!/bin/sh
# crear y activdar el entorno virtual
python3 -m venv .venv
source .venv/bin/activate
# instalar el flask
pip install flask
# crear la base de datos
sqlite3 datos.sqlite < datos.sql

#todo esto se activa con ". .nombre."