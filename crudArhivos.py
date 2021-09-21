class Archivo:
    def __init__(self, nombreArchivo='', separador='|'):
        self.__archivo = './nomina_archivos/' + nombreArchivo
        self.__separador = separador
        
    def leer(self):
        try:
          with open(self.__archivo, 'r', encoding="utf-8") as myFile:
            lista=[] 
            for linea in myFile:
              line = linea[:-1].split(self.__separador)
              lista.append(line)
        except IOError:
           lista=[]    
        return lista

    def leer_v2(self) -> list:
        try:
            with open(self.__archivo, mode='r', encoding="utf-8") as myFile:
                lista = []
                for parrafo in myFile:
                    if '\n' in parrafo:
                        linea = parrafo[:-1].split(self.__separador)
                        lista.append(linea)
                    else:
                        linea = parrafo.split(self.__separador)
                        lista.append(linea)
        except IOError: lista = []
        return lista
    
    def buscar(self, buscado): 
        resultado = []              
        with open(self.__archivo, mode='r', encoding='utf-8') as myFile:
            for linea in myFile:
                if linea[:-1].split(self.__separador)[0].find(buscado) is not -1 :
                    resultado = linea[:-1].split(self.__separador)
        return resultado
    
    def buscar_id(self, lista, buscado, identificador_inicio) -> bool:
        resultado = False
        if lista:
            for lista in lista:
                if lista[0:len(identificador_inicio)][0] == buscado:
                    resultado = True
                    break
            return resultado
        else: return resultado
   
    def buscarLista(self,buscado):
        resultado = []
        with open(self.__archivo, mode='r', encoding='utf-8') as myFile:
            for linea in myFile:
                registro = linea[:-1].split(self.__separador)
                if registro[0] == buscado:
                    resultado.append(registro)
        return resultado

    def buscar2(self,buscado1,buscado2):
        resultado = []
        with open(self.__archivo, mode='r', encoding='utf-8') as myFile:
            for linea in myFile:
                registro = linea[:-1].split(self.__separador)
                if registro[1] == buscado1 and registro[2] == buscado2:
                    resultado = registro
        return resultado

    def escribir(self, datos, modo):
        with open(self.__archivo, modo, encoding="utf-8") as myFile:
            for dato in datos:
                myFile.write(dato+'\n')
             
    def escribirM(self,datos,modo):
        with open(self.__archivo, modo, encoding="utf-8") as myFile:
          for dato in datos:
            linea=''
            for valor in dato:
              if type(valor) == int or float: linea +=str(valor)+self.__separador
              else: linea += valor + self.__separador
            myFile.write(linea[:-1]+"\n")
