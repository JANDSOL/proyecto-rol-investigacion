from operative_system.limpiar_consola import clean_screen
from espera_consola.retraso import espera_consola
from componentes import Menu,Valida
from console_gotoxy import gotoxy
from crudArhivos import Archivo
from entidadesRol import *
from datetime import date


# Envio de ENTIDADES por relacion de agregación.
def recibo_clase_agregacion(clase='', tit_met='', mensaje='', mensaje_error='', nombre_arch='',
                            ident_inc='', col=0, fil=0):
    """Devuelve una instancia de la clase."""
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
        except IndexError:
            clean_screen()
            gotoxy(col+5, fil-2); print('ACTUALIZANDO PROGRAMA!!!')
            espera_consola(3, False)


# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos():
    TITULO_METODO = "MANTENIMIENTO DE EMPLEADO ADMINISTRATIVO"
    validar = Valida(TITULO_METODO)
    _id = validar.solo_id_auto("administrativo.txt", 'ADM')
    fec_ing = validar.solo_fecha("Fecha de Ingreso (año-mes-dia): ", "Ingresa una fecha correcta...",
                                 15, 4)
    nom = validar.solo_letras("Nombre: ", "Ingresa un nombre correcto...", 15, 4) 
    ci = validar.solo_cedula("C.I. (Cédula de Identidad): ", "Ingresa una cédula correcta...", 15, 4)
    tel = validar.solo_telefono("Teléfono: ", "Ingresa un teléfono correcto...", 15, 4)
    dire = validar.solo_letras("Dirección: ", "Ingresa una direccion correcta...", 15, 4)
    sue = validar.solo_decimales("Sueldo: ", "Ingresa un sueldo válido...", 15, 4) 
    com = validar.solo_respuesta("Comisión (si/no): ", "Ingresa una respuesta válida...", 15, 4)
    dep = recibo_clase_agregacion("departamento", TITULO_METODO, "Departamento (ID): ",
                                  "Ingrese un ID correcto...", "departamento.txt", "DEP", 15, 4)
    car = recibo_clase_agregacion("cargo", TITULO_METODO, "Cargo (ID): ", "Ingrese un ID correcto...",
                                  "cargo.txt", "CAR", 15, 4)
    empleado_admin = Administrativo(nom, dep, car, dire, ci, tel, fec_ing, sue, _id, com)
    # Escritura de datos en un archivo!
    archi_emp_adm = Archivo("administrativo.txt")
    datos = empleado_admin.getEmpleado()
    datos = '|'.join(datos)
    archi_emp_adm.escribir([datos], 'a')

def empObreros():
    TITULO_METODO = "MANTENIMIENTO DE EMPLEADO OBRERO"
    validar = Valida(TITULO_METODO)
    _id = validar.solo_id_auto("administrativo.txt", 'ADM')
    fec_ing = validar.solo_fecha("Fecha de Ingreso (año-mes-dia): ", "Ingresa una fecha correcta...",
                                 15, 4)
    nom = validar.solo_letras("Nombre: ", "Ingresa un nombre correcto...", 15, 4) 
    ci = validar.solo_cedula("C.I. (Cédula de Identidad): ", "Ingresa una cédula correcta...", 15, 4)
    tel = validar.solo_telefono("Teléfono: ", "Ingresa un teléfono correcto...", 15, 4)
    dire = validar.solo_letras("Dirección: ", "Ingresa una direccion correcta...", 15, 4)
    sue = validar.solo_decimales("Sueldo: ", "Ingresa un sueldo válido...", 15, 4) 
    con_col = validar.solo_respuesta("Contrato Colectivo (si/no): ", "Ingresa una respuesta válida...",
                                     15, 4)
    dep = recibo_clase_agregacion("departamento", TITULO_METODO, "Departamento (ID): ",
                                  "Ingrese un ID correcto...", "departamento.txt", "DEP", 15, 4)
    car = recibo_clase_agregacion("cargo", TITULO_METODO, "Cargo (ID): ", "Ingrese un ID correcto...",
                                  "cargo.txt", "CAR", 15, 4)
    empleado_obrero = Obrero(nom, dep, car, dire, ci, tel, fec_ing, sue, _id, con_col)
    # Escritura de datos en un archivo!
    archi_emp_obr = Archivo("obrero.txt")
    datos = empleado_obrero.getEmpleado()
    datos = '|'.join(datos)
    archi_emp_obr.escribir([datos], 'a')

def cargos():
    TITULO_METODO = "MANTENIMIENTO DE CARGOS"
    validar = Valida(TITULO_METODO)
    # _id =
    clean_screen()     
    gotoxy(20,2);print("MANTENIMIENTO DE CARGOS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Cargo: ")
    gotoxy(33,5)
    desCargo = input()
    archiCargo = Archivo("cargo.txt")
    cargos = archiCargo.leer()
    cargo = Cargo(desCargo, 'CAR19')
    datos = cargo.getCargo()
    datos = '|'.join(datos)
    archiCargo.escribir([datos],"a")

# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
   clean_screen()     
   gotoxy(20,2);print("INGRESO DE HORAS EXTRAS")
   empleado,entEmpleado = [],None
   aamm,h50,h100=0,0,0
   while not empleado:
      gotoxy(15,5);print("Empleado ID[    ]: ")
      gotoxy(27,5);id = input().upper()
      archiEmpleado = Archivo("./archivos/obrero.txt","|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
          gotoxy(35,5);print(entEmpleado.nombre)
      else: 
         gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
         espera_consola();gotoxy(27,5);print(" "*40)
    
    
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(15,7);print("Horas50:")
   gotoxy(15,8);print("Horas100:")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   #gotoxy(23,6);aamm = input()
   gotoxy(23,7);h50 = input()
   gotoxy(24,8);h100 = input()
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,9);grabar = input().lower()
   if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")                 
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
   
def prestamos():
    pass

# opciones de Rol de Pago
def rolAdministrativo():
   clean_screen()
   # Se ingresa los datos del rol a procesar     
   gotoxy(20,2);print("ROL ADMINISTRATIVO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   # Se procesa el rol con la confirmacion del usuario
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/administrativo.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              #print(empleado)
              entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetAdm.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"O B R E R O S")
            nomina.mostrarDetalleNomina()
    
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

   input("               Presione una tecla continuar...")  

def consultaRol():
   clean_screen()
   validar = Valida()
   # Se ingresa los datos del rol a Consultar     
   gotoxy(20,2);print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
   rol=0
   aamm=""
   gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(44,4)
   rol=input().upper()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de consultar el Rol(s/n):")
   gotoxy(54,7);procesar = input().lower()
   if procesar == "s":
        if rol == "A": 
            tit = "A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt","|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt","|")
        else: 
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObr.txt","|")
            archiRolDet = Archivo("./archivos/rolDetObr.txt","|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1],cabrol[0])
            entCabRol.totIngresos=float(cabrol[2])
            entCabRol.totDescuentos=float(cabrol[3])
            entCabRol.totPagoNeto=float(cabrol[4])
            detalle= archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])    
            # print(entCabRol.getNomina())
            # print(entCabRol.getDetalle())
            # input()
            # imprimir rol    
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input("No existe rol con ese periodo\n presione una tecla para continuar...")     
            
   else:
       gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")     
   input("               Presione una tecla continuar...")  

def rolObrero():
    pass


if __name__ == '__main__':
    # Menu Proceso Principal
    opc = ''
    while opc !='4':  
        clean_screen()
        menu = Menu("Menu Principal", ["1) Mantenimiento", "2) Novedades", "3) Rol de Pago", "4) Salir"],
                    "-"*25, 20, 10)
        opc = menu.menu().replace(' ', '')
        if opc == '1':  # MANTENIMIENTO
            opc1 = ''
            while opc1 !='7':
                clean_screen()    
                menu1 = Menu("Menu Mantenimiento", 
                             ["1) Empleados Administrativos", "2) Empleados Obreros", "3) Cargos",
                              "4) Departamentos", "5) Empresa", "6) Parametros", "7) Salir"
                             ], '-'*28, 20, 10)
                opc1 = menu1.menu().replace(' ', '')
                if opc1 == '1':
                    empAdministrativos()
                elif opc1 == '2':
                    empObreros()
                elif opc1 == '3':
                    cargos()
                elif opc1 == '4':
                    #TODO: DEPARTMANETO METODO EN NOMINA.
                    pass
                elif opc1 == '5':
                    #TODO: EMPRESA METODO EN NOMINA.
                    pass
                elif opc1 == '6':
                    #TODO: PARAMETROS METODO EN NOMINA.
                    pass
                elif opc1 == '7':
                    pass
        elif opc == "2":  # NOVEDADES
                clean_screen()
                menu2 = Menu("Menu Novedades",["1) Sobretiempo","2) Prestamos","3) Salir"],20,10)
                opc2 = menu2.menu()
                if opc2 == "1":
                    sobretiempos()
                elif opc2 == "2":
                    prestamos()
        elif opc == "3":  # ROL DE PAGO
                clean_screen()
                menu3 = Menu("Menu Rol",["1) Rol Administrativos","2) Rol Obreros","3) Consulta Rol","4) Sobre Empleado","5) Salir"],20,10)
                opc3 = menu3.menu()
                if opc3 == "1":
                    rolAdministrativo()
                elif opc3 == "2":
                    rolObrero()
                elif opc3 == "3":
                    consultaRol()
        elif opc == '4':  # SALIR
               clean_screen()
               print("Gracias por su visita....")
        else:  # OPCION INVALIDA
              print("Opcion no valida") 

    input("Presione una tecla <-- para salir...")
    clean_screen()
