lista1 = [2,5,2,1,1,5,8,2,3]
lista2 = [4,2,7,5,9,1]

# A = lista1, B = lista2
# (1) : AnB  |  (2) :  B\A

def intersec_listas(A: list, B: list):
    C = [x for x in A if x in B]
    print('     A n B : ', C)

def B_dif_A(A: list, B: list):
    C = [x for x in B if x not in A]
    print('     B \ A : ', C)


def main():
    print('     A = ',lista1)
    print('     B = ',lista2)
    print('  ','-'*40)
    intersec_listas(lista1,lista2)
    B_dif_A(lista1,lista2)

if __name__ == '__main__':
    main()