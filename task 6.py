def analyt(a,c=0):
    a=list(a)
    b={}
    for i in a:
        if i!=str(0):
            if str(i) not in b.keys():
                b[str(i)]=''
                b[str(i)]+=str(1)
                c+=1
            else:
                b[str(i)]+=str(1)
                c+=1
    memory=[]
    for i in a:
        if i!=str(0):
            if i not in memory:
                memory.append(i)
                b[str(i)]=str(len(b[i]))+str('|')+(f'{(len(b[i])/c*100):.1f}%')
    return b
print(analyt(input('input analytics----->')))

