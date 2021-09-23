from conceptos import ListaConceptos
import unittest

## Juan David Jimenez
## David Penilla


# Pruebas:

# * para ejecutar:
 # python Tests-Funcionalidades.py

# Las funcionalidades evaluadas en las pruebas
# nos dieron un marco sobre el cual construir
# el programa. Con las pruebas sentimos poder
# generar un esquema claro pero flexible
# sobre las funciones necesarias en el programa.

# Las pruebas de las funcionalidades más avanzadas
# Se encuentran en test_adivina_palabra.py

# * para ejecutar:
 # python test_adivina_palabra.py

claseTest = ListaConceptos()

class ConceptosTests(unittest.TestCase):

    
    claseTest.conceptos = {
        "palabra1": "descripcion1", 
        "pal2": "desc2", 
        "palab3":"descrip3"
        }

    def test_agregar(self):
        claseTest.insertar("hola","saludo")
        self.assertIn ("hola",claseTest.conceptos)

    def test_buscarC(self):
        self.assertTrue (claseTest.buscarC("pal2"))

    def test_buscarD(self):
        self.assertTrue (claseTest.buscarD("descrip3"))

    def test_noExisteC(self):
        self.assertFalse (claseTest.buscarC("asdf"))
        ##self.assertNotIn("asdf",claseTest.conceptos)

    def test_noExisteD(self):
        self.assertFalse (claseTest.buscarD("descrip falsa"))

    def test_noVacia(self):
        self.assertIsNotNone (claseTest.conceptos)
    
    def test_eliminar(self):
        claseTest.eliminar("pal2")
        self.assertFalse(claseTest.buscarC("pal2"))




if __name__ == '__main__':
    unittest.main(verbosity=2)
