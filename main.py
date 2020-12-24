def fib(num):
    a=0
    b=1
    c=0
    lst=[]
    for i in range(num):
        lst.append(c)
        a=b
        b=c
        c=a+b
    print(sum(lst))

print(fib(6))
