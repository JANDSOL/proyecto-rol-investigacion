from entidadesRol import Administrativo
from unicodedata import normalize as normalizar_cadena
from datetime import date
from operative_system.limpiar_consola import clean_screen
from espera_consola.retraso import espera_consola
from console_gotoxy import gotoxy
from crudArhivos import Archivo


class Menu:
    def __init__(self, titulo='', opciones=[], separador='', col=6, fil=1):
        self.titulo = titulo
        self.opciones = opciones
        self.separador = separador
        self.columna = col
        self.fila = fil
        
    def menu(self):
        gotoxy(self.columna,self.fila); print(self.titulo)
        self.columna -= 5
        for opcion in self.opciones:
            self.fila +=1
            gotoxy(self.columna, self.fila); print(opcion)
        gotoxy(self.columna, self.fila+1); print(self.separador)
        gotoxy(self.columna+3, self.fila+2)
        opc = input("Elija opcion[1...{}]: ".format(len(self.opciones)))
        return opc


class Valida:
    def __init__(self, titulo_metodo) -> None:
        self.__tit_met = titulo_metodo

    def solo_id_auto(self, nom_arch='', identificador_inicial='', inicio=1) -> str:
        archi_id = Archivo(nom_arch)
        while True:
            valor = identificador_inicial + str(inicio)
            lista = archi_id.leer_v2()
            valor_buscado = archi_id.buscar_id(lista, valor, identificador_inicial)
            if not valor_buscado:
                return valor
            inicio += 1
        # archi_id = Archivo(nom_arch)
        # clean_screen()
        # while True:
        #     gotoxy(col+5, fil-2); print(self.__tit_met)
        #     gotoxy(col, fil); print(mensaje)
        #     gotoxy(col+len(mensaje), fil)
        #     valor = input('').upper().replace(' ', '')
        #     if valor[0:1] == inicio:  # String de inicio del ID -> A1, A2...An
        #         try:
        #             int(valor[1::])  # Asegurarse el ingreso de enteros despues del str inicial->A1...An
        #             # Validar si ese ID ya existe.
        #             valor_buscado = archi_id.buscar_V2(valor)
        #             if not valor_buscado:  # Si valor_buscado es False, retornar valor no repetido.
        #                 return valor
        #             else:
        #                 gotoxy(col, fil+2); print("ID repetido, ingresa otro...")
        #                 gotoxy(col, fil+3); espera_consola()
        #         except ValueError:
        #             gotoxy(col, fil+2); print(mensaje_error)
        #             gotoxy(col, fil+3); espera_consola()
        #     else:
        #         gotoxy(col, fil+2); print(mensaje_error)
        #         gotoxy(col, fil+3); espera_consola()
    
    def solo_id(self, nom_arch, mensaje, inicio, mensaje_error, col, fil):
        archi_id = Archivo(nom_arch)
        clean_screen()
        while True:
            lista = archi_id.leer_v2()
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            # Imprimir Id de clase
            fila_clases = fil+9
            for clase in lista:
                gotoxy(col-15, fila_clases); print(clase)
                fila_clases += 1
            gotoxy(col+len(mensaje), fil)
            valor = input('').upper().replace(' ', '')
            if valor[0:len(inicio)] == inicio:  # String de inicio del ID -> A1, A2...An
                try:
                    # Asegurarse el ingreso de enteros despues del str inicial->A1...An
                    int(valor[len(inicio):])
                    valor_buscado = archi_id.buscar_id(lista, valor, inicio)
                    if not valor_buscado:  # Si valor_buscado es False, retornar valor no repetido.
                        gotoxy(col, fil+2); print("ID no encontrado, ingresa otro...")
                        gotoxy(col, fil+3); espera_consola()
                    else: return valor
                except ValueError:
                    gotoxy(col, fil+2); print(mensaje_error)
                    gotoxy(col, fil+3); espera_consola()
            else:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()
    
    def solo_fecha(self, mensaje, mensaje_error, col, fil) -> date:
        clean_screen()
        while True:
            entro_tratamiento1 = False
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            valor = input('').replace(' ', '').split('-')
            if len(valor) > 3:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()
            else:
                # VALIDO INGRESO DE SOLO NUMEROS
                try:
                    anio = int(valor[0])
                    mes = int(valor[1])
                    dia = int(valor[2])
                except (IndexError, ValueError):
                    gotoxy(col, fil+2); print(mensaje_error)
                    gotoxy(col, fil+3); espera_consola()
                    entro_tratamiento1 = True
                if entro_tratamiento1 is False:
                    # VALIDO LAS FECHAS
                    try: return date(anio, mes, dia)
                    except (SyntaxError, NameError, ValueError, TypeError):
                        gotoxy(col, fil+2); print(mensaje_error)
                        gotoxy(col, fil+3); espera_consola()

    def solo_periodo(self, lista, mensaje, mensaje_error, col, fil) -> date:
        clean_screen()
        while True:
            entro_tratamiento1 = False
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            # Imprimir periodos de clase
            fila_clases = fil+9
            for clase in lista:
                gotoxy(col-15, fila_clases); print(clase)
                fila_clases += 1
            gotoxy(col+len(mensaje), fil)
            valor = input('').replace(' ', '').split('-')
            if len(valor) > 2:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()
            else:
                # VALIDO INGRESO DE SOLO NUMEROS
                try:
                    anio = int(valor[0])
                    mes = int(valor[1])
                    dia = 1
                except (IndexError, ValueError):
                    gotoxy(col, fil+2); print(mensaje_error)
                    gotoxy(col, fil+3); espera_consola()
                    entro_tratamiento1 = True
                if entro_tratamiento1 is False:
                    # VALIDO LAS FECHAS
                    try:
                        periodo = date(anio, mes, dia)
                    except (SyntaxError, NameError, ValueError, TypeError):
                        gotoxy(col, fil+2); print(mensaje_error)
                        gotoxy(col, fil+3); espera_consola()
                        periodo = ''
                    # Validar si hay el periodo
                    for empleado in lista:
                        perio_emp = empleado[2].split('-')
                        periodo_empleado = date(int(perio_emp[0]), int(perio_emp[1]), 1)
                        if periodo == periodo_empleado: return periodo
                    gotoxy(col, fil+2); print("Periodo no encontrado, ingresa otro...")
                    gotoxy(col, fil+3); espera_consola()
    
    def solo_periodo_doble_lista(self, lista1, lista2, mensaje, mensaje_error, col, fil) -> date:
        clean_screen()
        while True:
            fila_clases = 0
            entro_tratamiento1 = False
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            # Imprimir periodos de clase
            fila_clases = fil+9
            for clase in lista1:
                gotoxy(col-15, fila_clases); print(clase)
                fila_clases += 1
            for clase in lista2:
                gotoxy(col-15, fila_clases); print(clase)
                fila_clases += 1
            gotoxy(col+len(mensaje), fil)
            valor = input('').replace(' ', '').split('-')
            if len(valor) > 2:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()
            else:
                # VALIDO INGRESO DE SOLO NUMEROS
                try:
                    anio = int(valor[0])
                    mes = int(valor[1])
                    dia = 1
                except (IndexError, ValueError):
                    gotoxy(col, fil+2); print(mensaje_error)
                    gotoxy(col, fil+3); espera_consola()
                    entro_tratamiento1 = True
                if entro_tratamiento1 is False:
                    # VALIDO LAS FECHAS
                    try:
                        periodo = date(anio, mes, dia)
                    except (SyntaxError, NameError, ValueError, TypeError):
                        gotoxy(col, fil+2); print(mensaje_error)
                        gotoxy(col, fil+3); espera_consola()
                        periodo = ''
                    # Validar si hay el periodo
                    for empleado in lista1:
                        perio_emp1 = empleado[2].split('-')
                        periodo_empleado1 = date(int(perio_emp1[0]), int(perio_emp1[1]), 1)
                        if periodo == periodo_empleado1: return periodo
                    for empleado in lista2:
                        perio_emp2 = empleado[2].split('-')
                        periodo_empleado2 = date(int(perio_emp2[0]), int(perio_emp2[1]), 1)
                        if periodo == periodo_empleado2: return periodo
                    if periodo != '':
                        gotoxy(col, fil+2); print("Periodo no encontrado, ingresa otro...")
                        gotoxy(col, fil+3); espera_consola()

    def solo_fecha_sobretiempo_prestamo(self, fechaIng_obrero, mensaje, mensaje_error, col, fil) -> date:
        clean_screen()
        while True:
            entro_tratamiento1 = False
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            valor = input('').replace(' ', '').split('-')
            if len(valor) > 3:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()
            else:
                # VALIDO INGRESO DE SOLO NUMEROS
                try:
                    anio = int(valor[0])
                    mes = int(valor[1])
                    dia = int(valor[2])
                except (IndexError, ValueError):
                    gotoxy(col, fil+2); print(mensaje_error)
                    gotoxy(col, fil+3); espera_consola()
                    entro_tratamiento1 = True
                if entro_tratamiento1 is False:
                    # VALIDO FECHA
                    try: 
                        fecha_sobretiempo = date(anio, mes, dia)
                    except (SyntaxError, NameError, ValueError, TypeError):
                        gotoxy(col, fil+2); print(mensaje_error)
                        gotoxy(col, fil+3); espera_consola()
                    # VALIDO FECHA MAYOR AL INGRESO DEL EMPLEADO
                    try:
                        if fecha_sobretiempo >= fechaIng_obrero: return fecha_sobretiempo
                        else:
                            gotoxy(col, fil+2)
                            print("Ingresa una fecha mayor a la que inicio a laboral el empleado...")
                            gotoxy(col, fil+3); print(str(fechaIng_obrero))
                            gotoxy(col, fil+4); espera_consola(5)
                    except UnboundLocalError:
                        pass

    def solo_numeros(self,mensaje_error,col,fil) -> str:
        while True: 
            gotoxy(col,fil)            
            valor = input('')
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensaje_error)
                # time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor
    
    def solo_entero(self, mensaje, mensaje_error, col, fil) -> int:
        clean_screen()
        while True:
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            try:
                valor = int(input(''))
                if valor >= 0: return valor
                else:
                    gotoxy(col, fil+2); print(mensaje_error)
                    gotoxy(col, fil+3); espera_consola()
            except ValueError:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()

    def solo_letras(self, mensaje, mensaje_error, col, fil) -> str:
        clean_screen()
        while True:
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            valor = input('').strip().title().split(' ')
            valor_unido = ''
            vuelta = 0
            for value in valor:  # Eliminar espacios en blanco y dejar uno por palabra.
                if value != '':
                    vuelta += 1
                    if vuelta > 1: valor_unido += ' ' + value
                    else: valor_unido += value
            if len(valor_unido) < 2:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()
            else: return valor_unido

    def solo_empleados(self, mensaje, mensaje_error, col, fil) -> str:
        clean_screen()
        while True:
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            valor = input('').replace(' ', '').upper()
            if valor == 'ADMINISTRATIVO':
                return valor
            elif valor == 'OBRERO':
                return valor
            else:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()

    def solo_cedula(self, mensaje, mensaje_error, col, fil) -> str:
        CODIGOS_PROVINCIAS = (
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
            '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '30'
        )
        clean_screen()
        while True:
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            valor = input('').replace(' ', '')
            if valor[0:2] in CODIGOS_PROVINCIAS and valor.isdigit():
                if len(valor) == 10: return valor
                else:
                    if len(valor) < 10:
                        gotoxy(col, fil+2); print("Te faltan {} dígitos...".format(10-len(valor)))
                        gotoxy(col, fil+3); espera_consola()
                    elif len(valor) > 10:
                        gotoxy(col, fil+2); print("Sobrepasaste con {} dígitos...".format(len(valor)-10))
                        gotoxy(col, fil+3); espera_consola()
            else:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()
    
    def solo_ruc(self, mensaje, mensaje_error, col, fil) -> str:
        CODIGOS_PROVINCIAS = (
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
            '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '30'
        )
        clean_screen()
        while True:
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            valor = input('').replace(' ', '')
            if valor[0:2] in CODIGOS_PROVINCIAS and valor.isdigit():
                if len(valor) == 13: return valor
                else:
                    if len(valor) < 13:
                        gotoxy(col, fil+2); print("Te faltan {} dígitos...".format(13-len(valor)))
                        gotoxy(col, fil+3); espera_consola()
                    elif len(valor) > 13:
                        gotoxy(col, fil+2); print("Sobrepasaste con {} dígitos...".format(len(valor)-13))
                        gotoxy(col, fil+3); espera_consola()
            else:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()

    def solo_telefono(self, mensaje, mensaje_error, col, fil) -> str:
        CODIGOS_TEL_PROVINCIAS = ('02', '03', '04', '05', '06', '07', '5932', '5933', '5934', '5935',
                                                                      '5936', '5937')
        CODIGO_CEL = ('09', '5939')
        clean_screen()
        while True:
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            valor = input('').replace(' ', '')
            # VALIDACION TELEFONIA FIJA
            if (valor[0:2] in CODIGOS_TEL_PROVINCIAS and valor.isdigit()) \
            or (valor[0:4] in CODIGOS_TEL_PROVINCIAS and valor.isdigit()):
                # VALIDAR NUMERO TELEFONO 9-11(numeros en total) -> 042721038 - 59342721038
                if valor[0:2] in CODIGOS_TEL_PROVINCIAS[0:6]:  # 02, 03...N este en codigos provincias
                    if len(valor) == 9: return valor
                    if len(valor) < 9:
                        gotoxy(col, fil+2); print("Te faltan {} dígitos...".format(9-len(valor)))
                        gotoxy(col, fil+3); espera_consola()
                    elif len(valor) > 9:
                        gotoxy(col, fil+2); print("Sobrepasaste con {} dígitos...".format(len(valor)-9))
                        gotoxy(col, fil+3); espera_consola()
                else:  # 5932, 5933...N este en codigos provincias
                    if len(valor) == 11: return valor
                    if len(valor) < 11:
                        gotoxy(col, fil+2); print("Te faltan {} dígitos...".format(11-len(valor)))
                        gotoxy(col, fil+3); espera_consola()
                    elif len(valor) > 11:
                        gotoxy(col, fil+2); print("Sobrepasaste con {} dígitos...".format(len(valor)-11))
                        gotoxy(col, fil+3); espera_consola()
            # VALIDACION CELULARES
            elif (valor[0:2] in CODIGO_CEL and valor.isdigit()) \
              or (valor[0:4] in CODIGO_CEL and valor.isdigit()):
                # VALIDAR NUMERO CELULAR 10-12(numeros en total) -> 0959089115 - 593959089115
                if valor[0:2] in CODIGO_CEL[0:1]:  # 09 ingreso con este codigo
                    if len(valor) == 10: return valor
                    if len(valor) < 10:
                        gotoxy(col, fil+2); print("Te faltan {} dígitos...".format(10-len(valor)))
                        gotoxy(col, fil+3); espera_consola()
                    elif len(valor) > 10:
                        gotoxy(col, fil+2); print("Sobrepasaste con {} dígitos...".format(len(valor)-10))
                        gotoxy(col, fil+3); espera_consola()
                else:  # 5939 ingreso con este codigo
                    if len(valor) == 12: return valor
                    if len(valor) < 12:
                        gotoxy(col, fil+2); print("Te faltan {} dígitos...".format(12-len(valor)))
                        gotoxy(col, fil+3); espera_consola()
                    elif len(valor) > 12:
                        gotoxy(col, fil+2); print("Sobrepasaste con {} dígitos...".format(len(valor)-12))
                        gotoxy(col, fil+3); espera_consola()
            else:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()

    def solo_decimales(self, mensaje, mensaje_error, col, fil) -> float:
        clean_screen()
        while True:
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            try:
                valor = float(input(''))
                if valor >= 0: return valor
                else:
                    gotoxy(col, fil+2); print(mensaje_error)
                    gotoxy(col, fil+3); espera_consola()
            except ValueError:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()
    
    def solo_respuesta(self, mensaje, mensaje_error, col, fil) -> bool:
        clean_screen()
        while True:
            gotoxy(col+5, fil-2); print(self.__tit_met)
            gotoxy(col, fil); print(mensaje)
            gotoxy(col+len(mensaje), fil)
            valor_no_norm = input('').upper().replace(' ', '').replace('Ñ', '#')
            valor = normalizar_cadena("NFKD", valor_no_norm).encode("ascii","ignore").\
                                                               decode("ascii").replace('#', 'Ñ')
            if valor == 'SI': return True
            elif valor == 'NO': return False
            else:
                gotoxy(col, fil+2); print(mensaje_error)
                gotoxy(col, fil+3); espera_consola()
