from abc import ABC,abstractmethod
from datetime import date
from crudArhivos import Archivo
from operative_system.limpiar_consola import clean_screen
from console_gotoxy import gotoxy


class Empresa:
    def __init__(self, razonSocial, direccion, telefono, ruc) -> None:
        self.razonSocial = razonSocial
        self.direccion = direccion
        self.telefono = telefono
        self.ruc = ruc

    def getEmpresa(self) -> list:
        return [self.razonSocial, self.direccion, self.telefono, self.ruc]


class Departamento:
    def __init__(self, descripcion, id) -> None:
        self.__id = id
        self.descripcion = descripcion
       
    @property
    def id(self) -> str:
        return self.__id

    def getDepartamento(self) -> list:
        return [self.id, self.descripcion]


class Cargo:
    def __init__(self, descripcion, id) -> None:
        self.__id = id
        self.descripcion = descripcion
       
    @property
    def id(self) -> str:
        return self.__id

    def getCargo(self) -> list:
        return  [self.id, self.descripcion]


class Empleado(ABC): 
    def __init__(self, nombre, departamento, cargo, direccion, cedula,
                 telefono, fechaIngreso, sueldo, id) -> None:
        self.__id = id
        self.nombre = nombre
        self.departamento = departamento
        self.cargo = cargo
        self.direccion = direccion
        self.cedula = cedula
        self.telefono = telefono
        self.fechaIngreso = fechaIngreso
        self.sueldo = sueldo

    @property
    def id(self) -> str:
        return self.__id

    @abstractmethod
    def valorHora(self) -> float:  
        return round(self.sueldo / 240, 2)


class Administrativo(Empleado):
    def __init__(self, nombre, departamento, cargo, direccion, cedula,
                 telefono, fechaIngreso, sueldo, id, comision=False) -> None:
        super().__init__(nombre, departamento, cargo, direccion, cedula,
                         telefono, fechaIngreso, sueldo, id)
        self.comision = comision

    def valorHora(self) -> float:
        return super().valorHora()
    
    def getEmpleado(self) -> list:
        return  [self.id, self.departamento.id, self.cargo.id, self.nombre, self.direccion, self.cedula,
                 self.telefono, str(self.fechaIngreso), str(self.sueldo), str(self.comision)]


class Obrero(Empleado):
    def __init__(self, nombre, departamento, cargo, direccion, cedula,
                 telefono, fechaIngreso, sueldo, id, cc=False) -> None:
        super().__init__(nombre, departamento, cargo, direccion, cedula,
                         telefono, fechaIngreso, sueldo, id)
        self.cc = cc

    def valorHora(self) -> float:
        return super().valorHora()

    def getEmpleado(self) -> list:
        return  [self.id, self.nombre, self.departamento.id, self.cargo.id, self.direccion, 
                 self.cedula, self.telefono, str(self.fechaIngreso), str(self.sueldo), str(self.cc)]


class Deduccion:
    def __init__(self, iess, comision, antiguedad) -> None:
        self.__iess = iess    
        self.__comision = comision    
        self.__antiguedad = antiguedad
      
    def getIess(self) -> float:
        return round(self.__iess / 100, 4)
    
    def getComision(self) -> float:
        return round(self.__comision / 100, 4)
    
    def getAntiguedad(self) -> float:
        return round(self.__antiguedad / 100, 4)
    
    def getDeduccion(self) -> list:
        return  [str(self.__iess), str(self.__comision), str(self.__antiguedad)]


class Prestamo:
    def __init__(self, empleado, fecha, valor, numPagos, id) -> None:
        self.__id = id
        self.empleado = empleado
        self.fecha = fecha
        self.valor = valor
        self.numPagos = numPagos
        self.cuota = self.calcular_cuota()
        self.saldo = self.calcular_saldo()
        self.estado = self.calcular_estado()

    @property
    def id(self) -> str:
        return self.__id
    
    def calcular_cuota(self) -> float:
        if self.numPagos > 0: return round(self.valor / self.numPagos, 2)
        else: return 0
    
    def calcular_saldo(self) -> float:
        return round(self.cuota * self.numPagos, 2)
    
    def calcular_estado(self) -> bool:
        if self.saldo > 0: return True
        else: return False

    def getPrestamo(self):
        return [self.id, self.empleado.id, str(self.fecha), str(self.valor), str(self.numPagos), 
                str(self.cuota), str(self.saldo), str(self.estado)]
  
class Sobretiempo:
    def __init__(self, empleado, fecha, h_suplementarias, h_extraordinarias, id) -> None: 
        self.__id = id
        self.empleado = empleado
        self.fecha = fecha
        self.h_suplementaria = h_suplementarias
        self.h_extraordinaria = h_extraordinarias
        self.estado = self.calcular_estado()
        self.total_sobretiempo = self.sobretiempo()

    @property
    def id(self) -> str:
        return self.__id
    
    def calcular_estado(self) -> bool:
        if self.h_suplementaria > 0 or self.h_extraordinaria > 0: return True
        else: return False

    def sobretiempo(self) -> float:
        return round(
            self.empleado.valorHora() + (self.h_suplementaria * 1.5 + self.h_extraordinaria * 2), 2
        )
     
    def getSobretiempo(self) -> list:
       return [self.id, self.empleado.id, str(self.fecha), str(self.h_suplementaria), 
               str(self.h_extraordinaria), str(self.estado)]


class CalculoRol(ABC):
    @abstractmethod
    def getSueldo(self):
        pass
    @abstractmethod
    def getSobretiempo(self, periodo):
        pass
    @abstractmethod
    def getComision(self):
        pass
    @abstractmethod
    def getAntiguedad(self):
        pass
    @abstractmethod
    def getIess(self):
        pass
    @abstractmethod
    def getPrestamo(self, periodo):
        pass


class Nomina:
    def __init__(self, empleado, periodo, sobretiempo, deducciones, prestamo) -> None:
        self.periodo = periodo
        self.fecha = date.today()
        self.totIngresos = 0
        self.totDescuentos = 0
        self.totPagoNeto = 0
        self.listaDetalleNomina = []
        self.detalle_nomina = DetalleNomima(self.fecha, empleado, sobretiempo, deducciones, prestamo)

    def calcularNominaDetalle(self) -> None:
        empleado = self.detalle_nomina.empleado
        detalle = self.detalle_nomina
        rubrosIngresos = detalle.calcularRubrosIngresos()
        rubrosEgresos = detalle.calcularRubrosEgresos()
        self.totIngresos += detalle.totIng
        self.totIngresos = round(self.totIngresos, 2)
        self.totDescuentos += detalle.totDes
        self.totDescuentos = round(self.totDescuentos, 2)
        self.totPagoNeto += detalle.totLiq
        self.totPagoNeto = round(self.totPagoNeto, 2)
        self.listaDetalleNomina.append([
            str(self.periodo), empleado.id, empleado.cargo, empleado.departamento, str(rubrosIngresos[0]),
            str(rubrosIngresos[1]), str(rubrosIngresos[2]),str(rubrosIngresos[3]),str(rubrosIngresos[4]),
            str(rubrosEgresos[0]),str(rubrosEgresos[1]),str(rubrosEgresos[2]),str(rubrosEgresos[3])
        ])
        
    def getNomina(self) -> list:
        return [
            str(self.periodo), str(self.fecha), str(self.totIngresos),
            str(self.totDescuentos), str(self.totPagoNeto)
        ]

    def getDetalleNomina(self) -> list:
        return self.listaDetalleNomina
    
    def mostrarCabeceraNomina(self, razonSocial, direccion, telefono, ruc, tipoEmpl) -> None:
        clean_screen()
        print('              {}      Ruc : {}      Teléfono : {}      Dirección: {}'.format(
            razonSocial, ruc, telefono, direccion
            )
        )
        print("--"*78)
        print('FECHA: {}                N O M I N A   D E   P A G O  D E   E M P L E A D O S:    {}'\
              .format(str(self.fecha), tipoEmpl)
        )
        if isinstance(self.periodo, str):
            print('Nomina general de los empleados: {}'.format(self.periodo))
        else:
            anio = str(self.periodo.year)
            if 1 <= self.periodo.month <= 9:  # Between para mes entre 1 al 9
                mes = '0' + str(self.periodo.month)
            else:
                mes = str(self.periodo.month)
            print('Nomina correspondiente al Periodo: {}'.format(anio + '-' + mes))
        print('--'*78) 
        print(" "*18, "E M P L E A D O S", " "*36, "I N G R E S O S", " "*34, "E G R E S O S")
        print("\
|----------------------------------------------------|-------------------------------------------\
-----------|----------------------------------------------|"\
        )
        print("\
   Nombre      Cargo      Departamento      Sueldo      Sobretiempo      Antiguedad   Comision   \
   TotIng      Iess      Prestamo      TotDes      Neto   "\
        )
  
    def mostrarDetalleNomina(self, empleado, nomina_periodo) -> None:
        if empleado == 'administrativo':
            archiRol = Archivo('rolDetAdm.txt')
            rolDetalle = archiRol.leer_v2()
        else:
            archiRol = Archivo('rolDetObr.txt')
            rolDetalle = archiRol.leer_v2()
        fila = 9
        for det in rolDetalle:
            if det[0] == str(nomina_periodo):
                gotoxy(5,fila); print(det[1])
                gotoxy(16,fila); print(det[2])
                gotoxy(30,fila); print(det[3])
                gotoxy(45,fila); print(det[4])
                gotoxy(62,fila); print(det[5])
                gotoxy(78,fila); print(det[6])
                gotoxy(89,fila); print(det[7])
                gotoxy(101,fila); print(det[8])
                gotoxy(113,fila); print(det[9])
                gotoxy(124,fila); print(det[10])
                gotoxy(137,fila); print(det[11])
                gotoxy(148,fila); print(det[12])
                fila+=1
        input('\nPulsa enter <-- para continuar...')


class DetalleNomima(CalculoRol):
    def __init__(self, fecha_nomina, empleado, sobretiempo, deducciones, prestamo) -> None:
        self.fecha_nomina = fecha_nomina
        self.empleado = empleado
        self.sobretiempo = sobretiempo
        self.deducciones = deducciones
        self.prestamo = prestamo
        self.totIng = 0
        self.totDes = 0
        self.totLiq = 0

    def getSueldo(self) -> float:
        return round(self.empleado.sueldo, 2)
    
    def getSobretiempo(self) -> float:
        try:
            sobret = self.sobretiempo.total_sobretiempo
            return sobret
        except AttributeError:  # Para empleado administrativo que no tiene sobretiempo.
            return 0
    
    def getAntiguedad(self) -> float:
        """Calculo solo para empleado obrero."""
        if isinstance(self.empleado, Obrero):
            antig = self.deducciones.getAntiguedad()
            calculo_fechas = (self.fecha_nomina - self.empleado.fechaIngreso).days
            return round(antig * (calculo_fechas) / 365 * self.empleado.sueldo, 2)
        else: return 0
            
    def getComision(self) -> float:
        """Calculo solo para empleado administrativo."""
        if isinstance(self.empleado, Administrativo):
            if self.empleado.comision:  # Si comision es True
                comis = self.deducciones.getComision()
                return round(comis * self.empleado.sueldo, 2)
        else: return 0
    
    def getIess(self) -> float:
        ies = self.deducciones.getIess()
        try:
            return round(ies * (self.empleado.sueldo + self.sobretiempo.total_sobretiempo), 2)
        except AttributeError:
            return round(ies * (self.empleado.sueldo + 0), 2)

    def getPrestamo(self) -> float:
        try:
            return self.prestamo.cuota
        except AttributeError:
            return 0
        
    def calcularRubrosIngresos(self) -> list:
        ingresos = []
        ingresos.append(self.getSueldo())
        ingresos.append(self.getSobretiempo())
        ingresos.append(self.getAntiguedad())
        ingresos.append(self.getComision())
        for valor in ingresos:
            self.totIng += valor
        ingresos.append(round(self.totIng, 2))
        return ingresos
  
    def calcularRubrosEgresos(self) -> list:
        descuentos = []
        descuentos.append(self.getIess())
        descuentos.append(self.getPrestamo())
        for valor in descuentos:
            self.totDes += valor
        self.totLiq = round(self.totIng - self.totDes, 2)
        descuentos.append(round(self.totDes, 2))    
        descuentos.append(self.totLiq)    
        return descuentos
