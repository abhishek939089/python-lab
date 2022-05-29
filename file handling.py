n= open('e.txt','r')
m= open('f.txt','w')
for i in n.readlines():
    if '172' in i:
        m.write(i)
n.close()
m.close()