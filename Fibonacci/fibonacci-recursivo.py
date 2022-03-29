'''
    La sucesión de Fibonacci es la siguiente sucesión infinita de
    números naturales:
    {0,1,1,2,3,5,8,13,21,34,55,} ...
    fn=fn-1+f_n-2, fibonacci    
    La sucesión inicia con f0 y f1, y a partir de estos cada termino es la 
    suma de los dos anteriores.
'''


def fib(n):
    if n < 2:
        # f0 or f1
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)


for x in range(10):
    print(fib(x), end=',')

print('')
