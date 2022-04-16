class Cambio_base:
    '''
    Parameters

    number: numero en base diez
    base: un numero entero positivo mayor que la unidad
    '''

    def __init__(self,number,base):
        self.number = number
        self.base = base

    def cambio(self):
        '''
        El metodo cambio nos permitira convertir un numero en base 10
        a cual otra base que habremos especificado

        Returns 

        Devuelve una lista con los valores de cada cifra del nuevo numeral(numero)
        '''
        r = self.number
        l = []
        l.insert(0,self.number%self.base)
        while r >= self.base:
            r = r // self.base
            q = r % self.base
            l.append(q)

        l.reverse()
        return l


if __name__ == "__main__":
    A = Cambio_base(10,2)
    print(A.cambio())
