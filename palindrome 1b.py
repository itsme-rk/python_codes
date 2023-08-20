s=input('enter n:')
n=int(s)
m=0
while n!=0:
    m=m*10+n%10
    n=n//10
print('n=',s,";m=",m)
if m==int(s):
    print('palindrome')
else:
    print('not palindrome')    