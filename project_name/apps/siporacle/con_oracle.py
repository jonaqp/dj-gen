# import os
import cx_Oracle
import csv
from project_name.apps.siporacle.query_oracle import (
    SQL_articulos, SQL_proveedores, SQL_personas,
    SQL_Menu, SQL_asientos, SQL_tipo_almacen,
    SQL_concepto_aranceles, SQL_vendedor_inactivo,
    SQL_proyectos_activos, SQL_organizacion,
    SQL_unidad_medida, SQL_almacen_description,
    SQL_tareas_proyectos,
    SQL_posibles_almacen, SQL_articulos_acero,
    SQL_linea_articulo, SQL_clase_articulo, SQL_sub_clase_articulo,
    SQL_pedido_movimiento
)

# Network drive somewhere


# output_articulo = csv.writer(open("./csv/articulos.csv", "w"), dialect='excel')

# output_proveedores = csv.writer(open("./csv/proveedor.csv", "w"), dialect='excel')
# output_personas = csv.writer(open("./csv/personas.csv", "w"), dialect='excel')
# output_menu = csv.writer(open("./csv/menu.csv", "w"), dialect='excel') #mucha data
# output_asientos = csv.writer(open("./csv/asientos.csv", "w"), dialect='excel')
#
# output_tipo_almacen = csv.writer(open("./csv/tipo_almacen.csv", "w"), dialect='excel')
# output_concepto_aranceles = csv.writer(open("./csv/concepto_aranceles.csv", "w"), dialect='excel')
# output_vendedor_inactivo = csv.writer(open("./csv/vendedor_inactivo.csv", "w"), dialect='excel')
# output_proyectos_activos = csv.writer(open("./csv/proyectos_activos.csv", "w"), dialect='excel')
#
# output_organizacion = csv.writer(open("./csv/organizacion.csv", "w"), dialect='excel')
# output_unidad_medida = csv.writer(open("./csv/unidad_medida.csv", "w"), dialect='excel')
# output_almacen_description = csv.writer(open("./csv/almacen_description.csv", "w"), dialect='excel')
# output_tareas_proyectos = csv.writer(open("./csv/tareas_proyectos.csv", "w"), dialect='excel')
#
# output_posibles_almacen = csv.writer(open("./csv/posibles_almacen.csv", "w"), dialect='excel')
# output_articulos_acero = csv.writer(open("./csv/articulos_acero.csv", "w"), dialect='excel')
output_linea_articulo = csv.writer(open("./csv/linea_articulo.csv", "w"), dialect='excel')
output_clase_articulo = csv.writer(open("./csv/clase_articulo .csv", "w"), dialect='excel')
output_sub_clase_articulo = csv.writer(open("./csv/sub_clase_articulo.csv", "w"), dialect='excel')

output_sql_pedido_movimiento = csv.writer(open("./csv/pedido_movimiento.csv", "w"), dialect='excel')

connection = cx_Oracle.connect('apps/TMappsEBS@10.253.219.202:1523/QAS')
cursor = connection.cursor()

# """ ARTICULOS """
# cursor.execute(SQL_articulos)
# for row in cursor:
#     output_articulo.writerow(row)

# """ PROVEEDOR """
# cursor.execute(SQL_proveedores)
# for row in cursor:
#     output_proveedores.writerow(row)

# """ Personas """
# cursor.execute(SQL_personas)
# for row in cursor:
#     output_personas.writerow(row)
#
# """ Menu"""
# cursor.execute(SQL_Menu)
# for row in cursor:
#     output_menu.writerow(row)

#
# """ Asientos """
# cursor.execute(SQL_asientos)
# for row in cursor:
#     output_asientos.writerow(row)

#
# """ tipo_almacen """
# cursor.execute(SQL_tipo_almacen)
# for row in cursor:
#     output_tipo_almacen.writerow(row)

#
# """ concepto_aranceles """
# cursor.execute(SQL_concepto_aranceles)
# for row in cursor:
#     output_concepto_aranceles.writerow(row)

#
# """ vendedor_inactivo """
# cursor.execute(SQL_vendedor_inactivo)
# for row in cursor:
#     output_vendedor_inactivo.writerow(row)

#
# """ proyectos_activos """
# cursor.execute(SQL_proyectos_activos)
# for row in cursor:
#     output_proyectos_activos.writerow(row)

#
# """ organizacion """
# cursor.execute(SQL_organizacion)
# for row in cursor:
#     output_organizacion.writerow(row)

#
# """ unidad_medida """
# cursor.execute(SQL_unidad_medida)
# for row in cursor:
#     output_unidad_medida.writerow(row)

#
# """ almacen_description """
# cursor.execute(SQL_almacen_description)
# for row in cursor:
#     output_almacen_description.writerow(row)

#
# """ tareas_proyectos """
# cursor.execute(SQL_tareas_proyectos)
# for row in cursor:
#     output_tareas_proyectos.writerow(row)
#
#
# """ posibles_almacen """
# cursor.execute(SQL_posibles_almacen)
# for row in cursor:
#     output_posibles_almacen.writerow(row)

#
# """ articulos_acero """
# cursor.execute(SQL_articulos_acero)
# for row in cursor:
#     output_articulos_acero.writerow(row)

#
# """ linea_articulo """
# cursor.execute(SQL_linea_articulo)
# for row in cursor:
#     output_linea_articulo.writerow(row)
#
#
# """ clase_articulo """
# cursor.execute(SQL_clase_articulo)
# for row in cursor:
#     output_clase_articulo.writerow(row)
#
#
# """ sub_clase_articulo """
# cursor.execute(SQL_sub_clase_articulo)
# for row in cursor:
#     output_sub_clase_articulo.writerow(row)



""" SQL_pedido_movimiento """
cursor.execute(SQL_pedido_movimiento)
for row in cursor:
    output_sql_pedido_movimiento.writerow(row)



cursor.close()
connection.close()
