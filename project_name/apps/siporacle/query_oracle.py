SQL_articulos = """
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

SQL_proveedores = """
    select TIPO_DOCUMENTO,NUMERO_DOCUMENTO, TIPO_CUENTA, TIPO_MONEDA, NUMERO_CUENTA   from TM_DATOS_PROVEEDORES
"""

SQL_personas = """
    select PERSON_ID, FIRST_NAME,LAST_NAME from TM_PERSON
"""

SQL_Menu = """
    select RESPONSIBILITY_ID, SECUENCIA,NIVEL,DESCRIPCION,SUB_MENU_ID,MENU_ID,FUNCTION_ID from TM_PRUEBA
"""

SQL_asientos = """
    select EMPRESA, PERIODO,CODPER,CONCEPTO,D_CONCEPTO,CONCEPTO_TAREO,CUENTA,TIPO,MONTO,DESCRIPCION,FLAG_CC,CC  from TMP_ASIENTO_TMSOFT
"""

SQL_tipo_almacen = """
    select ORGANIZATION_ID, NAME,INVENTORY_ITEM_ID,DESCRIPTION,ENCUMBRANCE_ACCOUNT_OLD,
     EXPENSE_ACCOUNT_OLD, EXPENSE_OLD, ENCUMBRANCE_ACCOUNT_NEW, EXPENSE_ACCOUNT_NEW,
     EXPENSE_NEW
     from TMP_CUENTAS_ARTICULO_SCARRILLO
"""

SQL_concepto_aranceles = """
    select MEMO_LINE_ID, ORG_ID,NAME,DESCRIPTION,LANGUAGE,
     SOURCE_LANG, LAST_UPDATE_DATE, CREATION_DATE, CREATED_BY,LAST_UPDATED_BY,
     LAST_UPDATE_LOGIN
     from AR_MEMO_LINES_ALL_TL_BK
"""

SQL_vendedor_inactivo = """
     SELECT APS.VENDOR_ID
   FROM ap.AP_SUPPLIERS APS, ap.AP_SUPPLIER_SITES_ALL APSA
  WHERE APS.VENDOR_ID = APSA.VENDOR_ID
    AND APSA.VENDOR_SITE_CODE = 'FACT NAC PEN'
    AND APS.segment1 is not null
    AND NVL(end_date_active,SYSDATE) < SYSDATE
"""

SQL_proyectos_activos = """
select ppa.project_id,
         ppa.segment1||' - '||ppa.name||' - '||to_char(ppa.completion_date,'dd/mm/yyyy') segment1
    from pa.pa_projects_all ppa
   where nvl(ppa.completion_date,to_date(sysdate))>=to_date(sysdate)
     and ppa.project_status_code IN ( select project_status_code
                                        from apps.pa_project_statuses
                                       where project_system_status_code = 'APPROVED')
     and org_id=81
order by segment1 asc
"""

SQL_organizacion = """
select ou.organization_id org_id
       ,ou.name razon_social
       ,e.legal_entity_identifier RUC
       ,x.segment_value segmento
from   hr_all_organization_units ou
       ,hr_organization_information oi
       ,xle_entity_profiles e
       ,apps.gl_ledgers gle
       ,xle_fp_ledger_v x
where  ou.organization_id = oi.organization_id
and    oi.org_information_context = 'Operating Unit Information'
and    oi.org_information2 = to_char(e.legal_entity_id)
and    to_char(gle.ledger_id) = oi.org_information3
and    x.ledger_id = gle.ledger_id
and    le_information_contexT = 'PE'
"""

SQL_unidad_medida = """
    select UOM_CODE CODIGO_UDM
       ,UNIT_OF_MEASURE NOMBRE_UNIDAD
       ,DESCRIPTION     DESC_UNIDAD
from   mtl_units_of_measure_vl
where  language = 'ESA';
"""

SQL_almacen_description = """
        SELECT o.organization_id warehouse_id
       ,p.organization_code warehouse_code
       ,o.name warehouse_name
       ,ou.organization_id enterprise_id
       ,ou.name enterprise_name
       ,loc.location_id
       ,loc.address_line_1 location_detail
    from   mtl_parameters p
           ,hr_all_organization_units o
           ,hr_organization_information oi
           ,hr_all_organization_units ou
           ,hr_locations_all loc
    where  p.organization_id = o.organization_id
    and    nvl(o.date_to,sysdate+1) > sysdate
    and    oi.organization_id = o.organization_id
    and    to_char(ou.organization_id) = oi.org_information3
    and    substr(p.organization_code,1,2) = 'AP'
    and    oi.org_information_context = 'Accounting Information'
    and    loc.inventory_organization_id = o.organization_id
"""

SQL_projectos_activos = """
select p.project_id
       ,p.segment1 numero_proyecto
       ,p.name nombre_proyecto
       ,p.description desc_proyecto
       ,p.org_id
       ,p.start_date fecha_inicio
       ,p.completion_date   fecha_vigencia
       ,p.closed_date fecha_cierre
       ,(select a.customer_id from PA_PROJECT_CUSTOMERS_V a where a.project_id = p.project_id --and a.project_relationship_code = 'CF'
        and creation_date in (select min(b.creation_date) from PA_PROJECT_CUSTOMERS_V b where b.project_id = a.project_id)
        and rownum = 1) cliente_id
from pa_projects_all p
     ,pa_project_statuses S
where  s.project_status_code = p.project_status_code
AND    project_system_status_code = 'APPROVED' and status_type = 'PROJECT'
"""

SQL_tareas_proyectos = """
    select t.task_id
       ,t.task_number numero_tarea
       ,t.task_name nombre_tarea
       ,t.description desc_tarea
       ,t.start_date fecha_inicio
       ,t.completion_date   fecha_vigencia
       ,p.project_id
       ,p.segment1 numero_proyecto
       ,p.name nombre_proyecto
       ,p.description desc_proyecto
from   pa_tasks t
       ,pa_projects_all p
       ,pa_project_statuses S
where  t.project_id = p.project_id
and    s.project_status_code = p.project_status_code
AND    project_system_status_code = 'APPROVED' and status_type = 'PROJECT'
"""

SQL_posibles_almacen = """
    select organization_id id, upper(name) name  from HR_organization_units
where organization_id in (select hoi.organization_id from hr_organization_information hoi
where hoi.org_information1 = 'INV')
order by 1
"""

SQL_articulos_acero = """
    select
       it.concatenated_Segments articulo,
       mt.organization_id,
       org.name,
       mt.transaction_id,
       mt.last_update_date,
       mt.creation_date,
       mt.subinventory_code,
       mt.locator_id,
       loc.concatenated_Segments Ubicacion,
       mt.transaction_type_id,
       mtp.transaction_type_name,
       mt.transaction_action_id,
       mt.transaction_source_type_id,
       mt.transaction_source_id,
       mt.transaction_source_name,
       mt.transaction_quantity,
       mt.actual_cost,
       mt.transaction_cost,
       mt.new_cost,
       mt.currency_code,
       mt.Transaction_Uom,
       mt.transaction_Date,
       mt.transfer_transaction_id,
       mt.project_id,
       mt.source_project_id,
       mt.expenditure_type
  from mtl_material_transactions mt,
       (select distinct inventory_item_id, concatenated_segments
          from mtl_system_items_b_kfv
         where segment1 = '30') it,
       hr_all_organization_units org,
       mtl_item_locations_kfv loc,
       mtl_transaction_types mtp
 where mt.inventory_item_id = it.inventory_item_id
   and mt.organization_id = org.organization_id
   and mt.locator_id = loc.inventory_location_id
   and mt.transaction_type_id = mtp.transaction_type_id
   and mt.inventory_item_id not in
   (select inventory_item_id from tm_vw_art_actualizado union
   select inventory_item_id from tm_vw_no_acero)
 order by it.inventory_item_id
"""
