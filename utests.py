from conceptos import ListaConceptos
import unittest

class TestsConceptos(unittest.TestCase):

    def test_agregar(self):
        #existe = listaListaConceptos.buscarE("$1") 
        lista = ListaConceptos()
        lista.insertar("Llave de prueba","una descripcion")
        self.assertTrue(lista.buscarE("Llave de prueba"))
    
    def test_buscarNoExisteConc(self):
        lista = ListaConceptos(2)
        lista.conceptos = {
         'prueba1':'descrip1',
         'prueba2': 'descrip2'
        }
        self.assertFalse(lista.buscarE('prueba3'))

    def test_agregarExisteDesc(self):
        lista = ListaConceptos(1)
        #lista.insertar('prueba-llave','prueba-descrip')
        lista.conceptos = dict(prueballave = "prueba-descrip",
                               llave2="decrip-llave2")
        
        existe = lista.buscarDes('prueba-descrip')
        self.assertEqual(existe,True)
    
    def test_buscarNoExisteDesc(self):
        lista = ListaConceptos(1)
        lista.insertar('llaveExiste','descripExiste')
        self.assertFalse(lista.buscarDes("asdfasf"))

        #existe = lista.buscarDes('JxAUBTjqnt111')
        #self.assertEqual(existe,False)

if __name__ == '__main__':
    unittest.main()