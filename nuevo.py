from conceptos import ListaConceptos
import unittest

claseTest = ListaConceptos()

class ConceptosTests(unittest.TestCase):

    
    claseTest.conceptos = {
        "palabra1": "descripcion1", 
        "pal2": "desc2", 
        "palab3":"descrip3"
        }

    def test_agregar(self):
        claseTest.conceptos["hola"] = "saludo"
        self.assertIn("hola",claseTest.conceptos)

    def test_buscarC(self):
        self.assertTrue("pal2" in claseTest.conceptos)

    def test_buscarD(self):
        self.assertTrue("descrip3" in claseTest.conceptos.values())

    def test_noExisteC(self):
        ##self.assertFalse("asdf" in claseTest.conceptos)
        self.assertNotIn("asdf",claseTest.conceptos)

    def test_noExisteD(self):
        self.assertFalse("descrip falsa" in claseTest.conceptos.values())

    def test_noVacia(self):
        self.assertIsNotNone(claseTest.conceptos)
    
    def test_eliminar(self):
        claseTest.conceptos.pop("pal2")
        self.assertFalse("pal2" in claseTest.conceptos)




if __name__ == '__main__':
    unittest.main(verbosity=2)
