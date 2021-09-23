# Parcial 1 - Práctico: Técnicas Avanzadas de Programación
#   David Penilla - 69675

class StringMetodos:

    def noTildesMayus(self,palabra):
        dicc = {'á':'a',
                'é':'e',
                'í':'i',
                'ó':'o',
                'ú':'u'}

        palabra = palabra.lower().replace(' ','')
        modif_pal = [dicc[ch] if ch in dicc else ch for ch in palabra]
        
        return ''.join(modif_pal)


    def sonAnagramas(self,str1,str2):
        a = self.noTildesMayus(str1)
        b = self.noTildesMayus(str2)

        if (len(a) != len(b)):
            return False
        else:
            for s in set(a):
                if a.count(s) != b.count(s):
                    return False
        return True
    

    def esPalindromo(self,str1):
        str1 = self.noTildesMayus(str1)

        return True if str1 == str1[::-1] else False


    def frecuenciasChars(self,str1):
        str1 = self.noTildesMayus(str1)

        freq_list = []
        for x in str1:
            tup = (x,str1.count(x))
            if tup not in freq_list:
                freq_list.append( tup )

        return freq_list
       

