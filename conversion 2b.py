def decimal(n,base):
    if n==0 :
        return n
    return base*decimal(n//10,base)+n%10

def hexadecimal(n,base):
    if n==0 :
        return n
    return hexadecimal(n//base,base) + digits[n%base] 

digits='123456789ABCDEF'

s=input('enter n:')
n=int(s)

s=input('enter base:')
b=int(s)

d=decimal(n,b)

if b==8:
    print('h=',hexadecimal(n,16))

print('n={},b={}'.format(n,b))
print('d=',d)
