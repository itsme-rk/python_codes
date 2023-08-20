import difflib
s1=input('enter the string1  ')
s2=input('enter the string2  ')

rv=difflib.SequenceMatcher(None,s1,s2)

print('similarities between both strings',rv.ratio())