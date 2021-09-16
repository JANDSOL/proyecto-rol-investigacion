from time import time
from crudArhivos import Archivo
from datetime import date
from abc import ABC,abstractmethod
from helpers import gotoxy,borrarPantalla
import os,time
    
class Empresa:
    def __init__(self, razonSocial, direccion, telefono, ruc):
        self.razonSocial = razonSocial
        self.direccion = direccion
        self.telefono = telefono
        self.ruc = ruc
       
    def mostrarEmpresa(self):   
        print(''' {} 
        - Ruc : {} 
        - Dirección : {} 
        - Teléfono: {}'''.format(self.razonSocial,self.ruc, 
                                     self.direccion, self.telefono))
       
class Departamento:
    def __init__(self, descripcion,id=1):
        self.__id = id
        self.descripcion = descripcion
       
    @property
    def id(self):
        return self.__id

    def mostrarDepartamento(self):
        print('{}. DEPARTAMENTO DE {}'.format(self.id,self.descripcion))
        print(' ')

class Cargo:
    def __init__(self, descripcion,id=1):
        self.__id = id
        self.descripcion = descripcion
       
    @property
    def id(self):
        return self.__id

    def mostrarCargo(self):
        print('{}. CARGO {}'.format(self.id,self.descripcion))
   
    def getCargo(self):
        return  [str(self.id),self.descripcion]
     
    
class Empleado(ABC): 
    def __init__(self,nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo,id=1):
        self.__id = id
        self.nombre = nombre
        self.departamento=departamento
        self.cargo = cargo
        self.direccion = direccion
        self.cedula = cedula
        self.telefono = telefono
        self.fechaIngreso = fechaIngreso
        self.sueldo = sueldo

    @property
    def id(self):
        return self.__id

    @abstractmethod
    def valorHora(self):  
        return self.sueldo/240
    

    def mostrarEmpleado(self):
        print(' {} Empleado : {} Cedula: {} dirección : {} Cargo: {} Dpto: {}'.format(self.id,self.nombre,self.cedula,self.direccion,self.cargo.descripcion,self.departamento.descripcion),end=" ")

    
class Administrativo(Empleado):
    def __init__(self,nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo,id,comision= True):
        super().__init__(nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo,id)
        self.comision = comision

   
    def mostrarEmpleado(self): 
        print(' {} Administrativo : {} Cedula: {} dirección : {} Cargo: {} Dpto: {}'.format(self.id,self.nombre,self.cedula,self.direccion,self.cargo.descripcion,self.departamento.descripcion),end=" ")
        print("Comision:{}".format(self.comision))

    def valorHora(self):
        return super().valorHora()
    
    def getEmpleado(self):
        return  [self.id,self.nombre,str(self.departamento.id),str(self.cargo.id),self.direccion,self.cedula,self.telefono,str(self.fechaIngreso),str(self.sueldo),str(self.comision)]
    
class Obrero(Empleado):
    def __init__(self,nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo,id, cc= True):
        super().__init__(nombre,departamento,cargo, direccion, cedula, telefono, fechaIngreso, sueldo,id)
        self.cc = cc

    def mostrarEmpleado(self): 
        print(' {} Obrero : {} Cedula: {} dirección : {} Cargo: {} Dpto: {}'.format(self.id,self.nombre,self.cedula,self.direccion,self.cargo.descripcion,self.departamento.descripcion),end=" ")
        print("CColectivo:{}".format(self.cc))

    def valorHora(self):
        return super().valorHora()
    
    def getEmpleado(self):
        return  [self.id,self.nombre,str(self.departamento.id),str(self.cargo.id),self.direccion,self.cedula,self.telefono,str(self.fechaIngreso),str(self.sueldo),str(self.cc)]
          
class Deduccion:
    def __init__(self, iess, comision, antiguedad):
        self.__iess = iess    
        self.__comision = comision    
        self.__antiguedad = antiguedad
      
    def getIess(self):
        return round(self.__iess/100,4)
    
    
    def getComision(self):
        return round(self.__comision/100,2)
    
    def getAntiguedad(self):
        return round(self.__antiguedad/100,2)
    
    def mostrarDeduccion(self):
        print('Valor Iess {} = \n Valor comision ({}) = \n Valor antiguedad ({}) ='.format(self.iess, self.comision, self.antiguedad))
    
    def getDeduccion(self):
        return  [str(self.__iess),str(self.__comision),str(self.__antiguedad)]
     
class Prestamo:
    def __init__(self,empleado, aamm, valor, numPagos,saldo, estado= True,id=1):
        self.__id = id
        self.empleado=empleado
        self.aamm = aamm
        self.valor = valor
        self.numPagos = numPagos
        self.cuota = valor/numPagos
        self.saldo = saldo
        self.estado = estado

    @property
    def id(self):
        return self.__id

    def mostrarPrestamo(self):
        print('''{}° Prestamo realizado: {}
          - Empleado= {}
          - Valor = ${}
          - Numeros Pagos = {}  
          - Cuota = ${:.2f} 
          - Saldo = ${:.2f}
          - estado = {} '''.format(self.id,self.aamm,self.empleado.nombre,self.valor,self.numPagos,self.cuota,self.saldo,self.estado))

    def getPrestamo(self):
       return [str(self.id),self.empleado.id,self.aamm,str(self.valor),str(self.numPagos),str(self.cuota),str(self.saldo),str(self.estado)]    
  
class Sobretiempo:
    def __init__(self,empleado, aamm,hSuplementarias,hExtraordinarias,estado= True,id=1): 
        self.__id = id
        self.empleado=empleado
        self.aamm = aamm
        self.h50 = hSuplementarias
        self.h100 = hExtraordinarias
        self.estado = estado

    @property
    def id(self):
        return self.__id

    def sobretiempo(self):
        return round(self.empleado.valorHora()+(self.h50*1.5+self.h100*2),2)
    
    def mostrarSobretiempo(self):
        print('''{}° Sobretiempo realizado: {}
          - Empleado= {}
          - H50 = {}
          - H100 = {}  
          - Valor = ${:.2f} 
          - estado = {} '''.format(self.id,self.aamm,self.empleado.nombre,self.h50,self.h100,self.sobretiempo(),self.estado))
     
    def getSobretiempo(self):
       return [str(self.id),str(self.empleado.id),self.aamm,str(self.h50),str(self.h100),str(self.estado)]    

class CalculoRol(ABC):
    @abstractmethod
    def getSueldo(self):
        pass
    @abstractmethod
    def getSobretiempo(self,aamm):
        pass
    @abstractmethod
    def getComision(self,deduccion):
        pass
    @abstractmethod
    def getAntiguedad(self,deduccion):
        pass
    @abstractmethod
    def getIess(self,deduccion):
        pass
    @abstractmethod
    def getPrestamo(self,aamm):
        pass 
     
    
class Nomina:
    def __init__(self,fecha,aamm):
        self.aamm = aamm   
        self.fecha = fecha
        self.totIngresos=0
        self.totDescuentos=0
        self.totPagoNeto=0
        self.detalleNomina = []

    @property
    def id(self):
        return self.__id

    def calcularNominaDetalle(self,empleado,deduccion):
        detalle = DetalleNomima(empleado)
        rubrosIngresos = detalle.calcularRubrosIngresos(self.aamm,deduccion)
        rubrosEgresos = detalle.calcularRubrosEgresos(self.aamm,deduccion)
        self.totIngresos += detalle.totIng
        self.totDescuentos += detalle.totDes
        self.totPagoNeto += detalle.totLiq
        self.detalleNomina.append([
             empleado.id,empleado.cargo,empleado.departamento,
             str(rubrosIngresos[0]),str(rubrosIngresos[1]),str(rubrosIngresos[2]),str(rubrosIngresos[3]),str(rubrosIngresos[4]),
             str(rubrosEgresos[0]),str(rubrosEgresos[1]),str(rubrosEgresos[2]),str(rubrosEgresos[3])
        ])        
        
    def getNomina(self):
       return [self.aamm,str(self.fecha),str(self.totIngresos),str(self.totDescuentos),str(self.totPagoNeto)]
    
    def getDetalle(self):
        return self.detalleNomina
    
    def mostrarCabeceraNomina(self,razonSocial, direccion, telefono, ruc,tipoRol):
        borrarPantalla()
        print('              {} Ruc : {} Teléfono : {} Dirección: {}'.format(razonSocial,ruc,telefono,direccion))
        print('--------------------------------------------------------------------------------------------------------------------')
        print('FECHA: {}  N O M I N A   D E   P A G O  D E   E M P LE A D O S: {}  '.format(self.fecha,tipoRol))
        print('Nomina correspondiente al Periodo:{}'.format(self.aamm))
        print('--'*59) 
        print(" "*5,"E M P L E A D O S"," "*30,"I N G R E S O S"," "*22,"E G R E S O S")
        print("Nombre     Cargo          Departamento    Sueldo   Sobretiempo  Antiguedad  Comision TotIng   Iess    Prestamo   TotDes   Neto")
  
    def mostrarDetalleNomina(self):
        fila = 8
        #print(self.detalleNomina)
        for det in self.detalleNomina:
            #print(emp.nombre,emp.cargo.descripcion,emp.departamento.descripcion,ing[0],ing[1],ing[2],ing[3],des[0],des[1])    
            archiCargo = Archivo("./archivos/cargo.txt","|")
            cargo = archiCargo.buscar(det[1])
            if cargo: desCargo = cargo[1]
            else : desCargo = "Sin Cargo"
            archiDpto = Archivo("./archivos/departamento.txt","|")
            dpto = archiDpto.buscar(det[2])
            if dpto: desDpto = dpto[1]
            else : desDpto = "Sin Departamento"
            gotoxy(1,fila);print(det[0],end="")    
            gotoxy(10,fila);print(desCargo,end="")    
            gotoxy(25,fila);print(desDpto,end="")    
            gotoxy(43,fila);print(det[3],end="")    
            gotoxy(53,fila);print(det[4],end="")    
            gotoxy(67,fila);print(det[5],end="")    
            gotoxy(78,fila);print(det[6],end="")    
            gotoxy(86,fila);print(det[7],end="")    
            gotoxy(95,fila);print(det[8],end="")    
            gotoxy(104,fila);print(det[9],end="")    
            gotoxy(114,fila);print(det[10],end="")    
            gotoxy(122,fila);print(det[11],end="")   
            fila+=1
         
        
class DetalleNomima(CalculoRol):
    secuencia = 0
    def __init__(self,empleado):
        DetalleNomima.secuencia += 1
        self.__id = DetalleNomima.secuencia
        self.empleado = empleado
        self.totIng=0
        self.totDes=0
        self.totLiq=0
       
    def getSueldo(self):
        return self.empleado.sueldo
    
    def getSobretiempo(self,aamm):
      calSob = 0
      if self.empleado.id[0]=="O":
        calSob = 20 # ir a sobretiempo traer h50 y h100 y realizar el calculo  
      return 0
    
    def getAntiguedad(self,deduccion):
        calAnt = 0
        if self.empleado.id[0]=="O":
            calAnt = 20 # traer antiguedad de deducciones y realizar calculo  
        return calAnt
            
    def getComision(self,deduccion):
        calCom = 0
        if self.empleado.id[0]=="A":
            calCom =round(self.empleado.sueldo*deduccion.getComision(),2)
        return calCom
    
    def getIess(self,deduccion):
        return round(self.empleado.sueldo*deduccion.getIess(),2)
        
    def getPrestamo(self,aamm):
        archiPrestamo = Archivo("./archivos/prestamo.txt","|")
        prestamo = archiPrestamo.buscar2(self.empleado.id,aamm)
        if prestamo:
            entPrestamo = Prestamo(prestamo[1],prestamo[2],float(prestamo[3]),int(prestamo[4]),float(prestamo[5]),prestamo[0])
            return round(entPrestamo.valor/entPrestamo.numPagos,2)
        else: return 0
        
    def calcularRubrosIngresos(self,aamm,deduccion):
        ingresos = []
        ingresos.append(self.getSueldo())
        ingresos.append(self.getSobretiempo(aamm))
        ingresos.append(self.getAntiguedad(deduccion))
        ingresos.append(self.getComision(deduccion))
        for valor in ingresos:
            self.totIng += valor
        ingresos.append(self.totIng)    
        return ingresos
  
    def calcularRubrosEgresos(self,aamm,deduccion):
        descuentos = []
        descuentos.append(self.getIess(deduccion))
        descuentos.append(self.getPrestamo(aamm))
        for valor in descuentos:
            self.totDes += valor
        self.totLiq = round(self.totIng - self.totDes,2)
        descuentos.append(self.totDes)    
        descuentos.append(self.totLiq)    
        return descuentos
  


