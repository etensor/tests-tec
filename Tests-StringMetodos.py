# Parcial 1 - Práctico: Técnicas Avanzadas de Programación
#   David Penilla - 69675

from StringMetodos import *
import unittest

claseTest = StringMetodos()

class TestsMetodos(unittest.TestCase):

    def test_sonAnagramasT1(self):
        self.assertTrue(claseTest.sonAnagramas('óCAcL áCo','Coc acóL a'))
        
    def test_sonAnagramasT2(self):
        self.assertEqual(claseTest.sonAnagramas('CosA',' SaCo'), True)
    
    def test_sonAnagramasF1(self):
        self.assertFalse(claseTest.sonAnagramas('casoprueba','pruebaacaso'))
    
    
    def test_esPalindromoT1(self):
        self.assertTrue(claseTest.esPalindromo('Dábale arroz a la zorra el Abad'))

    def test_esPalindromoT2(self):
        self.assertTrue(claseTest.esPalindromo('La ruta nos aportó otro paso natural'))

    def test_esPalindromoF(self):
        self.assertFalse(claseTest.esPalindromo('Esto no es un palindromo'))


    def test_frecuenciasCharsT1(self):
        palabra = 'Hola cómo estás hoy?'
        palabra = claseTest.noTildesMayus(palabra)
        freq_list = [(ch,palabra.count(ch)) for ch in palabra]
        self.assertCountEqual(
            claseTest.frecuenciasChars(palabra),
            set(freq_list)
        )
    
    def test_frecuenciasCharsT2(self):
        palabra = 'Muy bien gracias, y tu?'
        palabra = claseTest.noTildesMayus(palabra)
        freq_list = [(ch,palabra.count(ch)) for ch in palabra]
        self.assertSetEqual(
            set(claseTest.frecuenciasChars(palabra)),
            set(freq_list)
        )

    def test_frecuenciasCharsF(self):
        palabra = 'Bien, bueno chao.'
        palabra = claseTest.noTildesMayus(palabra)
        freq_list = [(ch,palabra.count(ch)) for ch in palabra]
        self.assertNotEqual(
            claseTest.frecuenciasChars(palabra),
            freq_list
        )
    
    def test_tipoFrecuencias(self):
        self.assertIsInstance(claseTest.frecuenciasChars('palabra'),list)


print('\n\n\t Resultados Tests - StringMetodos:\n','-'*70,sep='')
unittest.main(verbosity=2)
