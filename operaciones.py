class Operaciones:
    '''
    Parameters:
    num, dem: variable de tipo int
    '''
    def __init__(self,num,dem):
        self.num = num
        self.dem = dem
   
    def mcd(self):
        '''
        Verifica quien de los valores ingresados es mayor,
        y aplica el algoritmo de Euclides para encontrar el mcd.

        ----------------------------------------

        Return

        Devuelve un int

        '''
        c = min(self.num,self.dem)
        max = 1
        for i in range(1,c+1):
            if self.num % i ==0 and self.dem % i == 0:
                max = i
        return max


def lista_apropiada(lista,*arg):
    '''
    Busca eliminar todos los multiplos de un valor int que se encuentra 
    de la lista.

    Parameters

    ----------------------------------------------------------

    lista: una variable de tipo list

    -----------------------------------------------------------

    Return

    devuelve un list
    '''
    new = []
    for j in arg:
        new = []
        for i in lista:
            if i%j != 0:
                new.append(i)
        lista = new.copy()

    return new
    
if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9,12]
    print(lista_apropiada(lista,3,4))
    
