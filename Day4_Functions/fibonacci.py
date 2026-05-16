# Problem :print fabonacci(n)- nth fibo9nacci number do.Series:0,1,1,2,3,5,8........
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 0 1 1 2 3 5 8...
print(fibonacci(12))  # 144
