# import os
import cx_Oracle
import csv

SQL = """
        select  msib.organization_id                   Org_Id
       ,haou.name                              Organizacion
       ,msib.segment1||'.'||msib.segment2||'.'||msib.segment3||'.'||msib.segment4   Codigo
       ,msib.description                       Descripcion
       ,decode(msib.inventory_item_status_code,'Active','Activo'
                                              ,'Inactive','Inactivo'
                                              ,msib.inventory_item_status_code)     Estado
       ,msib.segment1                          codigo_Linea
       ,linea.description                      Linea_Articulo
       ,msib.segment1||'.'||msib.segment2      codigo_Clase
       ,clase.description                      Clase_Articulo
       ,msib.segment1||'.'||msib.segment2||'.'||msib.segment3  Codigo_SubClase
       ,subclase.description                   SubClase_Articulo
       ,msib.primary_unit_of_measure           Uni_Med
       ,msib.secondary_uom_code                Uni_Med_Sec

  from  inv.mtl_system_items_b          msib
       ,hr.hr_all_organization_units    haou
       ,(select  ffvv1.flex_value
                ,ffvv1.description
                ,ffvs1.flex_value_set_name
           from  apps.fnd_flex_values_vl        ffvv1
                ,applsys.fnd_flex_value_sets    ffvs1
          where  1 = 1
            and  ffvs1.flex_value_set_name  = 'TS_INV_TM_LINEA_ART'
            and  ffvs1.flex_value_set_id    = ffvv1.flex_value_set_id
        )  linea
       ,(select  ffvv2.flex_value
                ,ffvv2.description
                ,ffvs2.flex_value_set_name
                ,ffvv2.parent_flex_value_low
           from  apps.fnd_flex_values_vl        ffvv2
                ,applsys.fnd_flex_value_sets    ffvs2
          where  1 = 1
            and  ffvs2.flex_value_set_name  = 'TS_INV_TM_CLASE_ART'
            and  ffvs2.flex_value_set_id    = ffvv2.flex_value_set_id
        )  clase
       ,(select  ffvv3.flex_value
                ,ffvv3.description
                ,ffvs3.flex_value_set_name
                ,ffvv3.parent_flex_value_low
           from  apps.fnd_flex_values_vl        ffvv3
                ,applsys.fnd_flex_value_sets    ffvs3
          where  1 = 1
            and  ffvs3.flex_value_set_name  = 'TS_INV_TM_SUBCLASE_ART'
            and  ffvs3.flex_value_set_id    = ffvv3.flex_value_set_id
        )  subclase
 where  1 = 1
   and  substr(msib.inventory_item_status_code,1,1) in ('A','I')
   and  haou.organization_id            = 101
   and  linea.flex_value                = 30

   and  haou.organization_id            = msib.organization_id
   and  linea.flex_value                = msib.segment1
   and  clase.parent_flex_value_low     = msib.segment1
   and  clase.flex_value                = msib.segment2
   and  subclase.parent_flex_value_low  = msib.segment1
   and  subclase.flex_value             = msib.segment3
   and  msib.secondary_uom_code <> ' '
order by  msib.organization_id,msib.segment1||'.'||msib.segment2||'.'||msib.segment3||'.'||msib.segment4

        """

# Network drive somewhere
filename = "Output.csv"
FILE = open(filename, "w")
output = csv.writer(FILE, dialect='excel')


# os.putenv('ORACLE_HOME', '/oracle/product/10.2.0/db_1')
# os.putenv('LD_LIBRARY_PATH', '/oracle/product/10.2.0/db_1/lib')

connection = cx_Oracle.connect('apps/TMappsEBS@10.253.219.202:1523/QAS')

cursor = connection.cursor()
cursor.execute(SQL)
for row in cursor:
    output.writerow(row)
cursor.close()
connection.close()
FILE.close()
