def is_prime(n):
    x = 2
    count = 0
    while count < n:
        for i in range(2,int(x ** 0.5)+1):
            if x % i == 0:
                break
        else:
            print(x,end=" ")
            count+=1
        x+=1

n = int(input())
is_prime(n)  