from os import path, mkdir
from operative_system.limpiar_consola import clean_screen
from espera_consola.retraso import espera_consola
from componentes import Menu,Valida
from console_gotoxy import gotoxy
from crudArhivos import Archivo
from entidadesRol import *
from datetime import date


#.........................................................................................................
# Envio de ENTIDADES por relacion de agregación.
def recibo_clase_agregacion(clase='', tit_met='', mensaje='', mensaje_error='', nombre_arch='',
                            ident_inc='', col=0, fil=0):
    """Devuelve una instancia de una clase."""
    while True:
        clean_screen()
        validar = Valida(tit_met)
        archi_agg = Archivo(nombre_arch)
        entidades = archi_agg.leer_v2()
        _id = validar.solo_id(nombre_arch, mensaje, ident_inc, mensaje_error, col, fil)
        clase_utilizar = ''
        for entidad in entidades:
            if _id in entidad:
                clase_utilizar = entidad
                break
        # En el caso de que se agg. archivos en la ejecucion del programa, refrescar la carga del programa.
        try:
            if clase == 'departamento':
                return Departamento(clase_utilizar[1], clase_utilizar[0])
            if clase == 'cargo':
                return Cargo(clase_utilizar[1], clase_utilizar[0])
            if clase == 'obrero':
                fecha_ingresoStr = clase_utilizar[7].split('-')
                fecha_ingresoDate = date(
                    int(fecha_ingresoStr[0]), int(fecha_ingresoStr[1]), int(fecha_ingresoStr[2])
                )
                return Obrero(clase_utilizar[1], clase_utilizar[2], clase_utilizar[3], clase_utilizar[4],
                              clase_utilizar[5], clase_utilizar[6], fecha_ingresoDate,
                              float(clase_utilizar[8]), clase_utilizar[0], bool(clase_utilizar[9]))
            if clase == 'administrativo':
                fecha_ingresoStr = clase_utilizar[7].split('-')
                fecha_ingresoDate = date(
                    int(fecha_ingresoStr[0]), int(fecha_ingresoStr[1]), int(fecha_ingresoStr[2])
                )
                return Administrativo(clase_utilizar[3], clase_utilizar[1], clase_utilizar[2],
                                      clase_utilizar[4], clase_utilizar[5], clase_utilizar[6],
                                      fecha_ingresoDate, clase_utilizar[8], clase_utilizar[0],
                                      clase_utilizar[9])
        except IndexError:
            clean_screen()
            gotoxy(col+5, fil-2); print('ACTUALIZANDO PROGRAMA!!!')
            espera_consola(3, False)


def recibo_clase_agregacion_auto(id='', clase='', nombre_arch=''):
    """Devuelve una instancia de una clase."""
    while True:
        clean_screen()
        archi_agg = Archivo(nombre_arch)
        entidades = archi_agg.leer_v2()
        for entidad in entidades:
            if id in entidad:
                clase_utilizar = entidad
                break
        # En el caso de que se agg. archivos en la ejecucion del programa, refrescar la carga del programa.
        # if clase == 'departamento':
        #     return Departamento(clase_utilizar[1], clase_utilizar[0])
        # if clase == 'cargo':
        #     return Cargo(clase_utilizar[1], clase_utilizar[0])
        if clase == 'obrero':
            fecha_ingresoStr = clase_utilizar[7].split('-')
            fecha_ingresoDate = date(
                int(fecha_ingresoStr[0]), int(fecha_ingresoStr[1]), int(fecha_ingresoStr[2])
            )
            return Obrero(clase_utilizar[1], clase_utilizar[2], clase_utilizar[3], clase_utilizar[4],
                          clase_utilizar[5], clase_utilizar[6], fecha_ingresoDate,
                          float(clase_utilizar[8]), clase_utilizar[0], bool(clase_utilizar[9]))
        if clase == 'administrativo':
            fecha_ingresoStr = clase_utilizar[7].split('-')
            fecha_ingresoDate = date(
                int(fecha_ingresoStr[0]), int(fecha_ingresoStr[1]), int(fecha_ingresoStr[2])
            )
            return Administrativo(clase_utilizar[3], clase_utilizar[1], clase_utilizar[2],
                                  clase_utilizar[4], clase_utilizar[5], clase_utilizar[6],
                                  fecha_ingresoDate, float(clase_utilizar[8]), clase_utilizar[0],
                                  bool(clase_utilizar[9]))


#.........................................................................................................
# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos():
    """Lista de Empleados Administrativos."""
    TITULO_METODO = "MANTENIMIENTO DE EMPLEADO ADMINISTRATIVO"
    archi_dep = Archivo("departamento.txt")
    archi_car = Archivo("cargo.txt")
    leer_dep = archi_dep.leer_v2()
    leer_car = archi_car.leer_v2()
    if leer_dep and leer_car:
        validar = Valida(TITULO_METODO)
        _id = validar.solo_id_auto("administrativo.txt", 'ADM')
        nom = validar.solo_letras("Nombre: ", "Ingresa un nombre correcto...", 15, 4)
        dep = recibo_clase_agregacion("departamento", TITULO_METODO, "Departamento (ID): ",
                                      "Ingresa un ID correcto...", "departamento.txt", "DEP", 15, 4)
        car = recibo_clase_agregacion("cargo", TITULO_METODO, "Cargo (ID): ", "Ingresa un ID correcto...",
                                      "cargo.txt", "CAR", 15, 4)
        fec_ing = validar.solo_fecha("Fecha de Ingreso (año-mes-dia): ", "Ingresa una fecha correcta...",
                                     15, 4)
        ci = validar.solo_cedula("C.I. (Cédula de Identidad): ", "Ingresa una cédula correcta...", 15, 4)
        tel = validar.solo_telefono("Teléfono: ", "Ingresa un teléfono correcto...", 15, 4)
        dire = validar.solo_letras("Dirección: ", "Ingresa una direccion correcta...", 15, 4)
        sue = validar.solo_decimales("Sueldo: ", "Ingresa un sueldo válido...", 15, 4) 
        com = validar.solo_respuesta("Comisión (si/no): ", "Ingresa una respuesta válida...", 15, 4)
        empleado_admin = Administrativo(nom, dep, car, dire, ci, tel, fec_ing, sue, _id, com)
        # Escritura de datos en un archivo!
        archi_emp_adm = Archivo("administrativo.txt")
        datos = empleado_admin.getEmpleado()
        datos = '|'.join(datos)
        archi_emp_adm.escribir([datos], 'a')
    else:
        clean_screen()
        if not leer_dep and not leer_car:
            gotoxy(20, 2); print(TITULO_METODO)
            gotoxy(15, 4); print("Se necesita registros en los archivos")
            gotoxy(15, 5); print(" departamento y cargo para funcionar!!!")
        elif not leer_dep:
            gotoxy(20, 2); print(TITULO_METODO)
            gotoxy(15, 4); print("Se necesita registros en el archivo")
            gotoxy(15, 5); print(" departamento para funcionar!!!")
        elif not leer_car:
            gotoxy(20, 2); print(TITULO_METODO)
            gotoxy(15, 4); print("Se necesita registros en el archivo")
            gotoxy(15, 5); print(" cargo para funcionar!!!")
        gotoxy(15, 7); espera_consola(5, False)


def empObreros():
    """Lista de Empleados Obreros"""
    TITULO_METODO = "MANTENIMIENTO DE EMPLEADO OBRERO"
    archi_dep = Archivo("departamento.txt")
    archi_car = Archivo("cargo.txt")
    leer_dep = archi_dep.leer_v2()
    leer_car = archi_car.leer_v2()
    if leer_dep and leer_car:
        validar = Valida(TITULO_METODO)
        _id = validar.solo_id_auto("obrero.txt", 'OBR')
        nom = validar.solo_letras("Nombre: ", "Ingresa un nombre correcto...", 15, 4)
        dep = recibo_clase_agregacion("departamento", TITULO_METODO, "Departamento (ID): ",
                                      "Ingresa un ID correcto...", "departamento.txt", "DEP", 15, 4)
        car = recibo_clase_agregacion("cargo", TITULO_METODO, "Cargo (ID): ", "Ingresa un ID correcto...",
                                      "cargo.txt", "CAR", 15, 4)
        fec_ing = validar.solo_fecha("Fecha de Ingreso (año-mes-dia): ", "Ingresa una fecha correcta...",
                                     15, 4)
        ci = validar.solo_cedula("C.I. (Cédula de Identidad): ", "Ingresa una cédula correcta...", 15, 4)
        tel = validar.solo_telefono("Teléfono: ", "Ingresa un teléfono correcto...", 15, 4)
        dire = validar.solo_letras("Dirección: ", "Ingresa una direccion correcta...", 15, 4)
        sue = validar.solo_decimales("Sueldo: ", "Ingresa un sueldo válido...", 15, 4) 
        con_col = validar.solo_respuesta("Contrato Colectivo (si/no): ", "Ingresa una respuesta válida...",
                                         15, 4)
        empleado_obrero = Obrero(nom, dep, car, dire, ci, tel, fec_ing, sue, _id, con_col)
        # Escritura de datos en un archivo!
        archi_emp_obr = Archivo("obrero.txt")
        datos = empleado_obrero.getEmpleado()
        datos = '|'.join(datos)
        archi_emp_obr.escribir([datos], 'a')
    else:
        clean_screen()
        if not leer_dep and not leer_car:
            gotoxy(20, 2); print(TITULO_METODO)
            gotoxy(15, 4); print("Se necesita registros en los archivos")
            gotoxy(15, 5); print(" departamento y cargo para funcionar!!!")
        elif not leer_dep:
            gotoxy(20, 2); print(TITULO_METODO)
            gotoxy(15, 4); print("Se necesita registros en el archivo")
            gotoxy(15, 5); print(" departamento para funcionar!!!")
        elif not leer_car:
            gotoxy(20, 2); print(TITULO_METODO)
            gotoxy(15, 4); print("Se necesita registros en el archivo")
            gotoxy(15, 5); print(" cargo para funcionar!!!")
        gotoxy(15, 7); espera_consola(5, False)


def cargos():
    """Lista de cargos de la empresa."""
    archi_cargo = Archivo("cargo.txt")
    while True:
        valor_repetido = False
        TITULO_METODO = "MANTENIMIENTO DE CARGOS"
        validar = Valida(TITULO_METODO)
        _id = validar.solo_id_auto("cargo.txt", "CAR")
        des = validar.solo_letras("Descripción de cargo: ", "Ingresa una descripción correcta...", 15, 4)
        # Validar -> no repetir cargos.
        lectura_car = archi_cargo.leer_v2()
        for cargo in lectura_car:
            if des == cargo[1]:
                gotoxy(15, 6); print("Descripción repetida, ingresa otra...")
                gotoxy(15, 7); espera_consola()
                valor_repetido = True
        if not valor_repetido:
            cargo = Cargo(des, _id)
            # Escritura de datos en un archivo!
            datos = cargo.getCargo()
            datos = '|'.join(datos)
            archi_cargo.escribir([datos],'a')
            break


def departamentos():
    """Lista de departamentos de la empresa."""
    archi_depar = Archivo("departamento.txt")
    while True:
        valor_repetido = False
        TITULO_METODO = "MANTENIMIENTO DE DEPARTAMENTOS"
        validar = Valida(TITULO_METODO)
        _id = validar.solo_id_auto("departamento.txt", "DEP")
        des = validar.solo_letras("Descripción de departamento: ",
                                  "Ingresa una descripción correcta...", 15, 4)
        # Validar -> no repetir departamentos.
        lectura_dep = archi_depar.leer_v2()
        for departamento in lectura_dep:
            if des == departamento[1]:
                gotoxy(15, 6); print("Descripción repetida, ingresa otra...")
                gotoxy(15, 7); espera_consola()
                valor_repetido = True
        if not valor_repetido:
            departamento = Departamento(des, _id)
            # Escritura de datos en un archivo!
            datos = departamento.getDepartamento()
            datos = '|'.join(datos)
            archi_depar.escribir([datos],'a')
            break


def empresa():
    """Datos generales de la Empresa."""
    TITULO_METODO = "MANTENIMIENTO DE EMPRESA"
    validar = Valida(TITULO_METODO)
    raz_soc = validar.solo_letras("Razón Social: ", "Ingresa un nombre correcto...", 15, 4)
    dire = validar.solo_letras("Dirección: ", "Ingresa una dirección correcta...", 15, 4)
    tel = validar.solo_telefono("Teléfono: ", "Ingresa un teléfono correcto...", 15, 4)
    ruc = validar.solo_ruc("R.U.C. (Registro Único de Contribuyentes): ",
                           "Ingresa una R.U.C. correcto...", 15, 4)
    empresa = Empresa(raz_soc, dire, tel, ruc)
    # Escritura de datos en un archivo!
    archi_empre = Archivo("empresa.txt")
    datos = empresa.getEmpresa()
    datos = '|'.join(datos)
    archi_empre.escribir([datos],'w')


def parametros():
    """Porcentaje de valor para Iess, Comisión, Antiguedad."""
    TITULO_METODO = "MANTENIMIENTO DE PARAMETROS (IESS, Comisión, Antiguedad)"
    validar = Valida(TITULO_METODO)
    ies = validar.solo_decimales("Porcentaje del IESS: %", "Ingresa un porcentaje válido...", 15, 4)
    com = validar.solo_decimales("Porcentaje de comisión: %", "Ingresa un porcentaje válido...", 15, 4)
    ant = validar.solo_decimales("Porcentaje de antiguedad: %", "Ingresa un porcentaje válido...", 15, 4)
    deducciones = Deduccion(ies, com, ant)
    # Escritura de datos en un archivo!
    archi_param = Archivo("deducciones.txt")
    datos = deducciones.getDeduccion()
    datos = '|'.join(datos)
    archi_param.escribir([datos], 'w')


#.....................................................................................................
# Opciones del Menu Novedades
def sobretiempos():
    """Funcionalidad solo para empleados obreros."""
    TITULO_METODO = "NOVEDADES SOBRETIEMPO"
    archi_ob = Archivo("obrero.txt")
    leer_obrero = archi_ob.leer_v2()
    if leer_obrero:
        validar = Valida(TITULO_METODO)
        _id = validar.solo_id_auto("sobretiempo.txt", "SOB")
        emp = recibo_clase_agregacion("obrero", TITULO_METODO, "Empleado Obrero (ID): ",
                                      "Ingresa un ID correcto...", "obrero.txt", "OBR", 15, 4)
        fec = validar.solo_fecha_sobretiempo_prestamo(emp.fechaIngreso, "Fecha del sobretiempo: ",
                                                      "Ingresa una fecha correcta...", 15, 4)
        h_sup = validar.solo_entero("Horas de recargo: ", "Ingresa una hora correcta...", 15, 4)
        h_ext = validar.solo_entero("Horas extraordinarias: ", "Ingresa una hora correcta...", 15, 4)
        sobretiempo = Sobretiempo(emp, fec, h_sup, h_ext, _id)
        # Escritura de datos en un archivo!
        archi_sobret = Archivo("sobretiempo.txt")
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archi_sobret.escribir([datos], 'a')
    else:
        clean_screen()
        gotoxy(20, 2); print(TITULO_METODO)
        gotoxy(15, 4); print("Se necesita registros en el archivo")
        gotoxy(15, 5); print(" obrero para funcionar!!!")
        gotoxy(15, 7); espera_consola(5, False)
     
   
def prestamos():
    """Funcionalidad para empleados."""
    TITULO_METODO = "NOVEDADES PRESTAMOS"
    archi_adm = Archivo("administrativo.txt")
    leer_administrativo = archi_adm.leer_v2()
    archi_obr = Archivo("obrero.txt")
    leer_obrero = archi_obr.leer_v2()
    if leer_obrero or leer_administrativo:
        validar = Valida(TITULO_METODO)
        _id = validar.solo_id_auto("prestamo.txt", "PRE")
        ingreso_empl = validar.solo_empleados("Tipo de empleado (Administrativo, Obrero): ",
                                              "Ingrese un empleado válido...", 15, 4)
        if ingreso_empl == "ADMINISTRATIVO" and leer_administrativo:
            emp = recibo_clase_agregacion(
                "administrativo", TITULO_METODO, "Empleado Administrativo (ID): ",
                "Ingresa un ID correcto...", "administrativo.txt", "ADM", 15, 4
            )
        elif ingreso_empl == "OBRERO" and leer_obrero:
            emp = recibo_clase_agregacion("obrero", TITULO_METODO, "Empleado Obrero (ID): ",
                                          "Ingresa un ID correcto...", "obrero.txt", "OBR", 15, 4)
        else:
            clean_screen()
            gotoxy(20, 2); print(TITULO_METODO)
            if not leer_administrativo:
                gotoxy(15, 4); print("Se necesita registros en el archivo")
                gotoxy(15, 5); print(" administrativo para funcionar!!!")
            elif not leer_obrero:
                gotoxy(15, 4); print("Se necesita registros en el archivo")
                gotoxy(15, 5); print(" obrero para funcionar!!!")
            gotoxy(15, 7); espera_consola(5, False)
            return None
        fec = validar.solo_fecha_sobretiempo_prestamo(emp.fechaIngreso, "Fecha del sobretiempo: ",
                                                      "Ingresa una fecha correcta...", 15, 4)
        valo = validar.solo_decimales("Cantidad: $", "Ingresa una cantidad correcta...", 15, 4)
        num_pago = validar.solo_entero("Número de pagos: ", "Ingrese números correctos...", 15, 4)
        prestamo = Prestamo(emp, fec, valo, num_pago, _id)
        # Escritura de datos en un archivo!
        archi_prest = Archivo("prestamo.txt")
        datos = prestamo.getPrestamo()
        datos = '|'.join(datos)
        archi_prest.escribir([datos], 'a')
    else:
        clean_screen()
        gotoxy(20, 2); print(TITULO_METODO)
        if not leer_administrativo and not leer_obrero:
            gotoxy(15, 4); print("Se necesita registros en los archivos")
            gotoxy(15, 5); print(" obrero o administrativo para funcionar!!!")
        gotoxy(15, 7); espera_consola(5, False)


#.........................................................................................................
# opciones de Rol de Pago
def rolAdministrativo():
    """Calculo del rol para el empleado administrativo."""
    TITULO_METODO = "ROL ADMINISTRATIVO"
    # Validacion para evitar conflictos entre los archivos.
    archi_adm = Archivo("administrativo.txt")
    leer_administrativo = archi_adm.leer_v2()
    archi_dep = Archivo("departamento.txt")
    leer_departamento = archi_dep.leer_v2()
    archi_car = Archivo("cargo.txt")
    leer_cargo = archi_car.leer_v2()
    archi_dedu = Archivo("deducciones.txt")
    leer_deducciones = archi_dedu.leer_v2()
    archi_emp = Archivo("empresa.txt")
    leer_empresa = archi_emp.leer_v2()
    archi_pres = Archivo("prestamo.txt")
    leer_prestamos = archi_pres.leer_v2()
    if leer_administrativo and leer_departamento and leer_cargo and leer_deducciones and leer_empresa \
        and leer_prestamos:
        validar = Valida(TITULO_METODO)
        salir = ''
        while salir != ':!q':
            # Volver a leer los archivos para refrescar si se cambia algo en media ejecucion.
            leer_administrativo = archi_adm.leer_v2()
            leer_departamento = archi_dep.leer_v2()
            leer_cargo = archi_car.leer_v2()
            leer_deducciones = archi_dedu.leer_v2()
            leer_empresa = archi_emp.leer_v2()
            leer_prestamos = archi_pres.leer_v2()
            nom_per = validar.solo_periodo(leer_prestamos, "Periodo (año-mes): ",
                                           "Ingresa un periodo correcto...", 15, 4)
            # Calculo de la Nomina por cada periodo existente en prestamos.
            entro_nomina = False
            for prestamo in leer_prestamos:
                if prestamo[1][0:3] == 'ADM':  # Seleccionar empleados administrativos
                    perio_prest = prestamo[2].split('-')
                    periodo_prestamo = date(int(perio_prest[0]), int(perio_prest[1]), 1)
                    for empleado in leer_administrativo:
                        # Si id del empleado admin. es == al id del emp. admin.
                        # Ingresar solo si los periodos coinciden.
                        if prestamo[1] == empleado[0] and nom_per == periodo_prestamo:
                            entro_nomina = True
                            emp = recibo_clase_agregacion_auto(empleado[0], "administrativo",
                                                               "administrativo.txt")
                            ded = Deduccion(float(leer_deducciones[0][0]), float(leer_deducciones[0][1]),
                                            float(leer_deducciones[0][2]))
                            fec_pres = prestamo[2].split('-')
                            fecha_prestamo = date(int(fec_pres[0]), int(fec_pres[1]), int(fec_pres[2]))
                            pres = Prestamo(emp, fecha_prestamo, float(prestamo[3]),
                                            int(prestamo[4]), prestamo[0])
                            nomina = Nomina(emp, nom_per, 0, ded, pres)
                            nomina.calcularNominaDetalle()  # Inicializar calculos internos de la nomina.
                            # grabar cabecera del rol
                            cabecera_identica = False
                            archi_cab_rol = Archivo("rolCabAdm.txt")
                            leer_rol_cabecera = archi_cab_rol.leer_v2()
                            for cabecera in leer_rol_cabecera:
                                # Saber si hay ya registros identicos para evitar guardarlos de nuevo.
                                if '|'.join(cabecera) == '|'.join(nomina.getNomina()):
                                    cabecera_identica = True
                            if not cabecera_identica:  # Si no hay cabecera identica grabar.
                                archi_cab_rol.escribir(['|'.join(nomina.getNomina())], 'a')
                            # grabar detalle del rol
                            detalle_identico = False
                            archi_det_rol = Archivo("rolDetAdm.txt")
                            leer_rol_detalle = archi_det_rol.leer_v2()
                            for detalle in leer_rol_detalle:
                                if '|'.join(detalle) == '|'.join(nomina.getDetalleNomina()[0]):
                                    detalle_identico = True
                            if not detalle_identico:
                                print(nomina.getDetalleNomina()[0])
                                archi_det_rol.escribir(['|'.join(nomina.getDetalleNomina()[0])], 'a')
            if not entro_nomina:
                gotoxy(20, 2); print(TITULO_METODO)
                gotoxy(15, 4); print('No esta disponible ese periodo para calcular la nomina!!!')
                gotoxy(15, 5)
                salir = input('Ingresa (:!q) para salir, otro valor para continuar: ').replace(' ', '')
                gotoxy(15, 7); espera_consola(limpiar_pantalla=False)
            if entro_nomina: break
        if entro_nomina:
            empr = Empresa(leer_empresa[0][0], leer_empresa[0][1], leer_empresa[0][2], leer_empresa[0][3])
            nomina.mostrarCabeceraNomina(
                empr.razonSocial, empr.direccion, empr.telefono, empr.ruc, "A D M I N I S T R A T I V O S"
            )
            nomina.mostrarDetalleNomina("administrativo", nom_per)
    else:
        clean_screen()
        gotoxy(20, 2); print(TITULO_METODO)
        gotoxy(15, 4); print("Se necesita registros en los archivos")
        cadena_anterior = 1
        if not leer_administrativo:
            gotoxy(15+cadena_anterior, 5); print("administrativo, ")
            cadena_anterior += 16
        if not leer_departamento:
            gotoxy(15+cadena_anterior, 5); print("departamento, ")
            cadena_anterior += 14
        if not leer_cargo:
            gotoxy(15+cadena_anterior, 5); print("cargo, ")
            cadena_anterior += 7
        if not leer_deducciones:
            gotoxy(15+cadena_anterior, 5); print("deducciones, ")
            cadena_anterior += 13
        if not leer_empresa:
            gotoxy(15+cadena_anterior, 5); print("empresa, ")
            cadena_anterior += 9
        if not leer_prestamos:
            gotoxy(15+cadena_anterior, 5); print("prestamos, ")
            cadena_anterior += 11
        gotoxy(15+cadena_anterior, 5); print("para funcionar!!!")
        gotoxy(15, 7); espera_consola(5, False)


def rolObrero():
    """Calculo del rol para el empleado administrativo."""
    TITULO_METODO = "ROL OBRERO"
    # Validacion para evitar conflictos entre los archivos.
    archi_adm = Archivo("obrero.txt")
    leer_obrero = archi_adm.leer_v2()
    archi_dep = Archivo("departamento.txt")
    leer_departamento = archi_dep.leer_v2()
    archi_car = Archivo("cargo.txt")
    leer_cargo = archi_car.leer_v2()
    archi_dedu = Archivo("deducciones.txt")
    leer_deducciones = archi_dedu.leer_v2()
    archi_emp = Archivo("empresa.txt")
    leer_empresa = archi_emp.leer_v2()
    archi_pres = Archivo("prestamo.txt")
    leer_prestamos = archi_pres.leer_v2()
    archi_sobret = Archivo("sobretiempo.txt")
    leer_sobretiempo = archi_sobret.leer_v2()
    if leer_obrero and leer_departamento and leer_cargo and leer_deducciones and leer_empresa \
        and (leer_prestamos or leer_sobretiempo):
        validar = Valida(TITULO_METODO)
        salir = ''
        while salir != ':!q':
            entro_nomina = False
            # Volver a leer en caso de ingresar datos en el archivo en media ejecucion
            leer_obrero = archi_adm.leer_v2()
            leer_departamento = archi_dep.leer_v2()
            leer_cargo = archi_car.leer_v2()
            leer_deducciones = archi_dedu.leer_v2()
            leer_empresa = archi_emp.leer_v2()
            leer_prestamos = archi_pres.leer_v2()
            leer_sobretiempo = archi_sobret.leer_v2()
            nom_per = validar.solo_periodo_doble_lista(leer_prestamos, leer_sobretiempo,
                                                       "Periodo (año-mes): ",
                                                       "Ingresa un periodo correcto...", 15, 4)
            if not leer_sobretiempo: leer_sobretiempo = ['']
            # Dirigir bucle entorno a todos los empleados.
            # Memoization se encargara de no volver a registrar datos repetidos.
            memoization_sobretiempo = []
            memoization_prestamo = []
            for empleado in leer_obrero:
                for sobretiempo in leer_sobretiempo:
                    peroi_sob = sobretiempo[2].split('-')
                    periodo_sobretiempo = date(int(peroi_sob[0]), int(peroi_sob[1]), 1)
                    for prestamo in leer_prestamos:
                        perio_prest = prestamo[2].split('-')
                        periodo_prestamo = date(int(perio_prest[0]), int(perio_prest[1]), 1)
                        if ((empleado[0] == sobretiempo[1] ) and (nom_per == periodo_sobretiempo))\
                            or ((empleado[0] == prestamo[1]) and (nom_per == periodo_prestamo)):
                            # Captura solo para sobretiempo.
                            if empleado[0] == sobretiempo[1] and nom_per == periodo_sobretiempo:
                                if not memoization_sobretiempo\
                                    or (sobretiempo not in memoization_sobretiempo):
                                    # print('\nsobretiempo:', sobretiempo, end='')
                                    # input('')
                                    # print('prestamo:', prestamo)
                                    # input('')
                                    memoization_sobretiempo.append(sobretiempo)
                            # Captura solo para prestamo
                            elif (empleado[0] == prestamo[1]) or (nom_per == periodo_prestamo):
                                if not memoization_prestamo\
                                    or (prestamo not in memoization_prestamo):
                                    # print('\nprestamo:', prestamo, end='')
                                    # input('')
                                    # print('sobretiempo:', sobretiempo)
                                    # input('')
                                    memoization_prestamo.append(prestamo)

            sobretiempo = memoization_sobretiempo
            prestamo = memoization_prestamo
            solo_sobr = []
            solo_pres = []
            relacion_doble = []
            entro_rela_dobl = False

            # Obtener la relacion del empleado que tiene en los periodos
            # Si periodo_sobretiempo == periodo_prestamo, ¡Capturarlo!
            if sobretiempo and prestamo:
                entro_rela_dobl = True
                for sobr in sobretiempo:
                    for pres in prestamo:
                        if sobr[1] == pres[1]:
                            entro_nomina = True
                            emp = recibo_clase_agregacion_auto(sobr[1], "obrero", "obrero.txt")
                            ded = Deduccion(float(leer_deducciones[0][0]), float(leer_deducciones[0][1]),
                                            float(leer_deducciones[0][2]))
                            fec_pres = pres[2].split('-')
                            fecha_prestamo = date(int(fec_pres[0]), int(fec_pres[1]), int(fec_pres[2]))
                            presta = Prestamo(emp, fecha_prestamo, float(pres[3]), int(pres[4]), pres[0])
                            fec_sob = sobr[2].split('-')
                            fecha_sobr = date(int(fec_sob[0]), int(fec_sob[1]), int(fec_sob[2]))
                            sobret = Sobretiempo(emp, fecha_sobr, int(sobr[3]), int(sobr[4]), sobr[0])
                            nomina = Nomina(emp, nom_per, sobret, ded, presta)
                            nomina.calcularNominaDetalle()  # Inicializar calculos internos de la nomina.
                            # grabar cabecera del rol
                            cabecera_identica = False
                            archi_cab_rol1 = Archivo("rolCabObr.txt")
                            leer_rol_cabecera1 = archi_cab_rol1.leer_v2()
                            for cabecera in leer_rol_cabecera1:
                                # Saber si hay ya registros identicos para evitar guardarlos de nuevo.
                                if '|'.join(cabecera) == '|'.join(nomina.getNomina()):
                                    cabecera_identica = True
                            if not cabecera_identica:  # Si no hay cabecera identica grabar.
                                archi_cab_rol1.escribir(['|'.join(nomina.getNomina())], 'a')
                            # grabar detalle del rol
                            detalle_identico = False
                            archi_det_rol1 = Archivo("rolDetObr.txt")
                            leer_rol_detalle1 = archi_det_rol1.leer_v2()
                            for detalle in leer_rol_detalle1:
                                if '|'.join(detalle) == '|'.join(nomina.getDetalleNomina()[0]):
                                    detalle_identico = True
                            if not detalle_identico:
                                archi_det_rol1.escribir(['|'.join(nomina.getDetalleNomina()[0])], 'a')
                            relacion_doble.append(sobr)
                            relacion_doble.append(pres)

            if prestamo and entro_rela_dobl:
                # Obtener solo el periodo del prestamo sin sobretiempo
                for pres in prestamo:
                    for pres_sobr in relacion_doble:
                        # Si PRE == PRE de la relacion_doble ingresar
                        # Para capturar prestamos diferentes
                        if pres[0][0:3] == pres_sobr[0][0:3]:
                            if pres not in relacion_doble and pres not in solo_pres:
                                regis_prestamo = calculo_registro_prestamos(pres, leer_deducciones, nom_per)
                                solo_pres.append(regis_prestamo[0])
                entro_nomina = regis_prestamo[1]
                nomina = regis_prestamo[2]
            elif prestamo and not entro_rela_dobl:
                for pres in prestamo:
                    regis_prestamo = calculo_registro_prestamos(pres, leer_deducciones, nom_per)
                    solo_pres.append(regis_prestamo[0])
                entro_nomina = regis_prestamo[1]
                nomina = regis_prestamo[2]

            if sobretiempo and entro_rela_dobl:
                # Obtener solo el periodo del sobretiempo sin prestamo
                for sobr in sobretiempo:
                    for sobr_pres in relacion_doble:
                        # Si SOB == SOB de la relacion_doble ingresar
                        # Para capturar sobretiempos diferentes
                        if sobr[0][0:3] == sobr_pres[0][0:3]:
                            if sobr not in relacion_doble and sobr not in solo_sobr:
                                regis_sobretiempo = calculo_registro_sobretiempo(sobr, leer_deducciones, nom_per)
                                solo_sobr.append(regis_sobretiempo[0])
                entro_nomina = regis_sobretiempo[1]
                nomina = regis_sobretiempo[2]
            elif sobretiempo and not entro_rela_dobl:
                for sobr in sobretiempo:
                    regis_sobretiempo = calculo_registro_sobretiempo(sobr, leer_deducciones, nom_per)
                    solo_sobr.append(regis_sobretiempo[0])
                entro_nomina = regis_sobretiempo[1]
                nomina = regis_sobretiempo[2]

            if not entro_nomina:
                gotoxy(20, 2); print(TITULO_METODO)
                gotoxy(15, 4); print('No esta disponible ese periodo para calcular la nomina!!!')
                gotoxy(15, 5)
                salir = input('Ingresa (:!q) para salir, otro valor para continuar: ').replace(' ', '')
                gotoxy(15, 7); espera_consola(limpiar_pantalla=False)
            if entro_nomina: break
        if entro_nomina:
            empr = Empresa(leer_empresa[0][0], leer_empresa[0][1], leer_empresa[0][2], leer_empresa[0][3])
            nomina.mostrarCabeceraNomina(
                empr.razonSocial, empr.direccion, empr.telefono, empr.ruc, "O B R E R O S"
            )
            nomina.mostrarDetalleNomina("obrero", nom_per)
    else:
        clean_screen()
        gotoxy(20, 2); print(TITULO_METODO)
        gotoxy(15, 4); print("Se necesita registros en los archivos")
        cadena_anterior = 1
        if not leer_obrero:
            gotoxy(15+cadena_anterior, 5); print("obrero, ")
            cadena_anterior += 8
        if not leer_departamento:
            gotoxy(15+cadena_anterior, 5); print("departamento, ")
            cadena_anterior += 14
        if not leer_cargo:
            gotoxy(15+cadena_anterior, 5); print("cargo, ")
            cadena_anterior += 7
        if not leer_deducciones:
            gotoxy(15+cadena_anterior, 5); print("deducciones, ")
            cadena_anterior += 13
        if not leer_empresa:
            gotoxy(15+cadena_anterior, 5); print("empresa, ")
            cadena_anterior += 9
        if not leer_prestamos and not leer_sobretiempo:
            gotoxy(15+cadena_anterior, 5); print("prestamos o sobretiempo, ")
            cadena_anterior += 25
        else:
            if not leer_prestamos:
                gotoxy(15+cadena_anterior, 5); print("prestamos, ")
                cadena_anterior += 11
            if not leer_sobretiempo:
                gotoxy(15+cadena_anterior, 5); print("sobretiempo, ")
                cadena_anterior += 13
        gotoxy(15+cadena_anterior, 5); print("para funcionar!!!")
        gotoxy(15, 7); espera_consola(5, False)


#.....................................................................................
# Calculos para los registros de sobretiempo y prestamo
def calculo_registro_sobretiempo(sobr, leer_deducciones, nom_per):
    entro_nomina = True
    emp = recibo_clase_agregacion_auto(sobr[1], "obrero", "obrero.txt")
    ded = Deduccion(float(leer_deducciones[0][0]), float(leer_deducciones[0][1]),
                    float(leer_deducciones[0][2]))
    fec_sob = sobr[2].split('-')
    fecha_sobr = date(int(fec_sob[0]), int(fec_sob[1]), int(fec_sob[2]))
    sobret = Sobretiempo(emp, fecha_sobr, int(sobr[3]), int(sobr[4]), sobr[0])
    nomina = Nomina(emp, nom_per, sobret, ded, 0)
    nomina.calcularNominaDetalle()  # Inicializar calculos internos de la nomina.
    # grabar cabecera del rol
    cabecera_identica = False
    archi_cab_rol1 = Archivo("rolCabObr.txt")
    leer_rol_cabecera1 = archi_cab_rol1.leer_v2()
    for cabecera in leer_rol_cabecera1:
        # Saber si hay ya registros identicos para evitar guardarlos de nuevo.
        if '|'.join(cabecera) == '|'.join(nomina.getNomina()):
            cabecera_identica = True
    if not cabecera_identica:  # Si no hay cabecera identica grabar.
        archi_cab_rol1.escribir(['|'.join(nomina.getNomina())], 'a')
    # grabar detalle del rol
    detalle_identico = False
    archi_det_rol1 = Archivo("rolDetObr.txt")
    leer_rol_detalle1 = archi_det_rol1.leer_v2()
    for detalle in leer_rol_detalle1:
        if '|'.join(detalle) == '|'.join(nomina.getDetalleNomina()[0]):
            detalle_identico = True
    if not detalle_identico:
        archi_det_rol1.escribir(['|'.join(nomina.getDetalleNomina()[0])], 'a')
    return(sobr, entro_nomina, nomina)

def calculo_registro_prestamos(pres, leer_deducciones, nom_per):
    entro_nomina = True
    emp = recibo_clase_agregacion_auto(pres[1], "obrero", "obrero.txt")
    ded = Deduccion(float(leer_deducciones[0][0]), float(leer_deducciones[0][1]),
                    float(leer_deducciones[0][2]))
    fec_pres = pres[2].split('-')
    fecha_prestamo = date(int(fec_pres[0]), int(fec_pres[1]), int(fec_pres[2]))
    presta = Prestamo(emp, fecha_prestamo, float(pres[3]), int(pres[4]), pres[0])
    nomina = Nomina(emp, nom_per, 0, ded, presta)
    nomina.calcularNominaDetalle()  # Inicializar calculos internos de la nomina.
    # grabar cabecera del rol
    cabecera_identica = False
    archi_cab_rol1 = Archivo("rolCabObr.txt")
    leer_rol_cabecera1 = archi_cab_rol1.leer_v2()
    for cabecera in leer_rol_cabecera1:
        # Saber si hay ya registros identicos para evitar guardarlos de nuevo.
        if '|'.join(cabecera) == '|'.join(nomina.getNomina()):
            cabecera_identica = True
    if not cabecera_identica:  # Si no hay cabecera identica grabar.
        archi_cab_rol1.escribir(['|'.join(nomina.getNomina())], 'a')
    # grabar detalle del rol
    detalle_identico = False
    archi_det_rol1 = Archivo("rolDetObr.txt")
    leer_rol_detalle1 = archi_det_rol1.leer_v2()
    for detalle in leer_rol_detalle1:
        if '|'.join(detalle) == '|'.join(nomina.getDetalleNomina()[0]):
            detalle_identico = True
    if not detalle_identico:
        archi_det_rol1.escribir(['|'.join(nomina.getDetalleNomina()[0])], 'a')
    return(pres, entro_nomina, nomina)


if __name__ == '__main__':
    # Menu Proceso Principal
    opc = ''
    while opc !='4':
        # Crear carpeta donde se alojan nuestros archivos si no existe.
        if not path.isdir('./nomina_archivos'):
            mkdir('./nomina_archivos')
        clean_screen()
        menu = Menu("MENÚ PRINCIPAL", ["1) Mantenimientos", "2) Novedades", "3) Roles de Pagos", "4) Salir"],
                    "-"*25, 20, 10)
        opc = menu.menu().replace(' ', '')
        if opc == '1':  # MANTENIMIENTO
            opc1 = ''
            while opc1 != '7':
                clean_screen()    
                menu1 = Menu("MENÚ MANTENIMIENTO", 
                             ["1) Empleados Administrativos", "2) Empleados Obreros", "3) Cargos",
                              "4) Departamentos", "5) Empresa", "6) Parametros (IESS, Comisión, Antiguedad)",
                              "7) Salir"
                             ], '-'*28, 20, 10)
                opc1 = menu1.menu().replace(' ', '')
                if opc1 == '1':   empAdministrativos()
                elif opc1 == '2': empObreros()
                elif opc1 == '3': cargos()
                elif opc1 == '4': departamentos()
                elif opc1 == '5': empresa()
                elif opc1 == '6': parametros()
                elif opc1 == '7': pass
                else:
                    print()
                    print(' '*13, "Opción no disponible 😥...")
                    espera_consola(3, False)
        elif opc == '2':  # NOVEDADES
            opc2 = ''
            while opc2 != '3':
                clean_screen()
                menu2 = Menu("MENÚ NOVEDADES",
                             ["1) Sobretiempo", "2) Prestamos", "3) Salir"
                             ], '-'*25, 20, 10)
                opc2 = menu2.menu().replace(' ', '')
                if opc2 == '1':   sobretiempos()
                elif opc2 == '2': prestamos()
                elif opc2 == '3': pass
                else:
                    print()
                    print(' '*13, "Opción no disponible 😥...")
                    espera_consola(3, False)
        elif opc == '3':  # ROL DE PAGO
            opc3 = ''
            while opc3 != '3':
                clean_screen()
                menu3 = Menu("MENÚ ROLES DE PAGOS",
                             ["1) Rol Empleados Administrativos", "2) Rol Empleados Obreros", "3) Salir"
                             ], '-'*32, 20, 10)
                opc3 = menu3.menu().replace(' ', '')
                if opc3 == '1':   rolAdministrativo()
                elif opc3 == '2': rolObrero()
                elif opc3 == '3': pass
                else:
                    print()
                    print(' '*13, "Opción no disponible 😥...")
                    espera_consola(3, False)
        elif opc == '4':  # SALIR
            clean_screen()
            print("Gracias por su visita 😃....")
        else:  # OPCION INVALIDA
            print()
            print(' '*13, "Opción no disponible 😥...")
            espera_consola(3, False)
    input("Presione una tecla <-- para salir 🥴...")
    clean_screen()
