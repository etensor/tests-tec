
class ListaConceptos:
    conceptos : dict = {}
    libre : int

    def __init__(self, tam = 0):
        self.libre = tam


    def insertar(self,llave, valor):
        self.conceptos[llave] = valor
        self.libre+=1

    def buscarE(self, llave):
        if llave in self.conceptos:
            return True
        else: return False

    def buscarDes(self,valor):
        if str(valor) in self.conceptos.values():
            return True
        return False




        #for _,value in self.conceptos.items():
         #   if str(valor) == value:
         #       return True
        #return False


