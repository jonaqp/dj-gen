# import os
import cx_Oracle
import csv
from .query_oracle import (
    SQL_articulos, SQL_proveedores, SQL_personas,
    SQL_Menu, SQL_asientos
)

# Network drive somewhere


output_articulo = csv.writer(open("articulos.csv", "w"), dialect='excel')
output_proveedores = csv.writer(open("proveedor.csv", "w"), dialect='excel')
output_personas = csv.writer(open("personas.csv", "w"), dialect='excel')
output_menu = csv.writer(open("menu.csv", "w"), dialect='excel')
output_asientos = csv.writer(open("asientos.csv", "w"), dialect='excel')

connection = cx_Oracle.connect('apps/TMappsEBS@10.253.219.202:1523/QAS')
cursor = connection.cursor()

""" ARTICULOS """
cursor.execute(SQL_articulos)
for row in cursor:
    output_articulo.writerow(row)
cursor.close()

""" PROVEEDOR """
cursor.execute(SQL_proveedores)
for row in cursor:
    output_proveedores.writerow(row)
cursor.close()

""" Personas """
cursor.execute(SQL_personas)
for row in cursor:
    output_personas.writerow(row)
cursor.close()

""" Menu"""
cursor.execute(SQL_Menu)
for row in cursor:
    output_menu.writerow(row)
cursor.close()

""" Asientos """
cursor.execute(SQL_asientos)
for row in cursor:
    output_asientos.writerow(row)
cursor.close()

connection.close()
