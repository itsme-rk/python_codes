import re
def isphonenumber(s):
    r=s.split('-')
    if len(r)!=3:
        return False
    if len(r[0])!=3 or not r[0].isdigit():
        return False
    if len(r[1])!=3 or not r[1].isdigit():
        return False 
    if len(r[2])!=4 or not r[2].isdigit():
        return False
    return True

def isphonenumber_re(s):
    regex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo=regex.search(s)
    return mo!=None

rv=isphonenumber('415-555-4242')
print('1.phone number found',rv)

rv=isphonenumber_re('my phone number 415-555-4242.')
print('2.phone number found',rv)