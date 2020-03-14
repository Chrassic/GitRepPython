# Fibonacci-Zahlen-Modul

def fib(n):    # schreibe Fibonacci bis n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b

def fib2(n): # gib Fibonacci zurueck bis n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
