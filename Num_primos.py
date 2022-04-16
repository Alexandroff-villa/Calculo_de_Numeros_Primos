from operaciones import Operaciones, lista_apropiada

class Pesi(Operaciones):
    '''
    Heredamos de la clase padre Operaciones, las variables de clases
    a,b: varibles int
    '''
    def __init__(self,a,b):
        super().__init__(a,b)

    def pesi(self):
        '''
        El metodo pesi nos permite verificar si los numeros ingrasdos son
        Primos Entre Si (PESI)

        -----------------------------------------------------------------

        Returns

        devuelve el valor True si son PESI y False en caso contrario
        '''
        if self.mcd()==1:
            p = True
        else:
            p = False
        return p

class Euler:
    '''
    Para calcular la funcion Euler de un numero

    Parameters:

    -------------------------------------------------------------

    a: variable de tipo int
    '''
    def __init__(self,a):
        self.a = a
        
    def func_euler(self):
        '''
        El metodo func_euler evalua el numero ingresado con la función de Euler

        -----------------------------------------------------------------------

        Returns 
        
        Devuelve un variable de tipo int
        '''
        num = []
        for i in range(1,self.a+1):
            B = Operaciones(i,self.a)
            if B.mcd() == 1:
                num.append(i)
        
        return len(num)


class Numero_primo(Euler):
    '''
    Se hereda de clase Euler con el de utilizar su metodo para hallar 
    numeros primos
    '''
    def __init__(self,primo):
        super().__init__(primo)

    def es_primo(self):
        '''
        Verifica si el valor ingresado es un numero primo

        Returns 

        devuelve True si es primo y False en caso contrario
        '''
        if self.func_euler() == self.a - 1:
            return True
        else:
            return False


    def cuantos_primos(self):
        '''
        Con el metodo cuantos_primos determinaremo cuantos numeros primos menores o 
        iguales al que ingresamos hay. Hacemos uso de la función lista_apropiada para
        reducir el campo a analizar

        Returns

        Devuelve una lista con todos los numeros primos menores o iguales al valor ingresado

        '''
        t = [2,3]
        lista1 = list(range(4,self.a+1))
        for i in lista_apropiada(lista1,2,3):
            A = Numero_primo(i)
            if A.es_primo() == True:
                t.append(i)
        return t    

if __name__ == "__main__":
    A = Euler(11)
    print(A.func_euler())
    
