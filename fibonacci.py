
#1TDCG (Scythe Control) - Caio Vinícius, Henrique Koji, João Cristovão, Luana Bannwart, Guilherme Cavalheiro #




cache = {}

def fibonacci(n):
    global cache
    if n in cache:
        return cache[n]
        
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

for i in range(0, 205):
    result = fibonacci(i)
    print(i, result)



