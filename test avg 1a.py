a=int(input("enter the marks in first ia"))
b=int(input("enter the marks in second ia"))
c=int(input("enter the marks in third ia"))
if a<=b and a<=c:
    print('ia 2 and ia 3 have max marks')
    avg=(b+c)/2
if b<=a and b<=c:
     print('ia 1 and ia 3 have max marks')
     avg=(a+c)/2
if c<=a and c<=b:
     print('ia 1 and ia 2 have max marks')
     avg=29
     print(a+b)
print('average of the best two ia is ',avg)        