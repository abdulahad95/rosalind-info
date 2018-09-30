s = input('Enter the string: \n')

a = 0
c = 0
g = 0
t = 0

for x in s:
    if x == 'A':
        a +=1
    if x == 'C':
        c +=1
    if x == 'G':
        g +=1 
    if x == 'T':
        t +=1
print (a, c, g, t)
