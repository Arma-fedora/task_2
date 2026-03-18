def fibonacci(n, first=0, second=1):
    n1, n2 = first, second
    if n == 0:
        return n1
    elif n == 1:
        return n2
    elif n>=2:
        for _ in range(2, n+1):
            n1, n2 = n2, n1+n2
        return n2

        

            
    

        
# Классическая последовательность
print(fibonacci(10))        # 55
print(fibonacci(5))         # 5
print(fibonacci(0))         # 0
print(fibonacci(1))         # 1

# Обобщённая последовательность: начинается с 2 и 3
# F(0)=2, F(1)=3, F(2)=5, F(3)=8, F(4)=13, F(5)=21, F(6)=34, F(7)=55
print(fibonacci(7, first=2, second=3))   # 55
    