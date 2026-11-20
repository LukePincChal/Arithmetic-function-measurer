class function:
    def __init__(self, function):
        self.function = function
        self.n = int(5e5)
        self.h = 1e-7

    def derivate(self, x=0):
        value = (self.function(x + self.h) - self.function(x)) / self.h
        return round(value, 6)
    
    def integral(self, up, down=0):
        delta = (up-down)/self.n
        
        area = 0
        for i in range(self.n):
            area+= self.function(down+i*delta)*delta
        
        return area
    
    
    
    def line(self, a=0):
        #f'(a)x -f'(a)(a)+f(a)
        coeff = self.derivate(a)
        
        value = [coeff, -coeff*a+self.function(a)]
        return value # function class with the attributes
    
    
    
    def root_finder(self, factor, precision):
        self.precision = precision
        self.factor = factor
    
    def __add__(self, oher):
        if isinstance(other, function):
            pass

    def __mul__(self, oher):
        if isinstance(other, function):
            pass
        
    def __div__(self, oher):
        if isinstance(other, function):
            pass
        
    def __truediv__(self, oher):
        if isinstance(other, function):
            pass
        

def f(x):
    return x**2

funcao = function(f)
print(funcao.derivate(5))
print(funcao.integral(10, 1))
print(funcao.line(10))
