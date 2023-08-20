def f(n):
    if n==0 or n==1:
        return n
    else:
        return f(n-1)+f(n-2)
s=input("enter n: ")
n=int(s)
if n>0:
    r=f(n)
    print('the element at the', n,'th postion in fibonacci series is',r)
else:
    print('n=',n,'enter n<0')
for i in range(n):
    print(f(i),end=' ')                    
