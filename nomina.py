from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesRol import *
from datetime import date
import time
# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos():
    pass
def empObreros():
    pass
def cargos():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARGOS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Cargo: ")
   gotoxy(33,5)
   desCargo = input()
   archiCargo = Archivo("./archivos/cargo.txt","|")
   cargos = archiCargo.leer()
   if cargos : idSig = int(cargos[-1][0])+1
   else: idSig=1
   cargo = Cargo(desCargo,idSig)
   datos = cargo.getCargo()
   datos = '|'.join(datos)
   archiCargo.escribir([datos],"a")
# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
   borrarPantalla()     
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
         time.sleep(2);gotoxy(27,5);print(" "*40)
    
    
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
   borrarPantalla()
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
   borrarPantalla()
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

# Menu Proceso Principal
opc=''
while opc !='5':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Novedades","3) Rol de Pago","4) Consultas","5) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='7':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Empleados Administratvos","2) Empleados Obreros","3) Cargos","4) Departamentos","5) Empresa","6) Parametros","7) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                empAdministrativos()
            elif opc1 == "3":
                cargos()
                        
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Novedades",["1) Sobretiempo","2) Prestamos","3) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()
            elif opc2 == "2":
                prestamos()
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Rol",["1) Rol Administrativos","2) Rol Obreros","3) Consulta Rol","4) Sobre Empleado","5) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo()
            elif opc3 == "2":
                rolObrero()
            elif opc3 == "3":
                consultaRol()
    elif opc == "4":
            borrarPantalla()
            menu4 = Menu("Menu Consultas",["1) Empleados","2) Cargos","3) Departamentos","4) Empresa","5) Parametros","6) Salir"],20,10)
            opc4 = menu.menu()
    elif opc == "5":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

