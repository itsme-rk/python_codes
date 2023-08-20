s=input('enter the input')

l=u=d=w=0

for i in s:
    if i.isdigit():
        d+=1
    if i.isspace():
        w+=1
    if i.islower():
        l+=1
    if i.isupper():
        u+=1
print('word:',w+1,'digit:',d,'upper:',u,'lower:',l)                   