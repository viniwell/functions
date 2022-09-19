def analyt(a):
    a=list(a)
    b={}
    c=0
    for i in a:
        if i not in b.keys():
            b[int(i)]=''
            b[int(i)]+=str(1)
            c+=1
        else:
            b[int(i)]+=str(1)
            c+=1
        memory=[]
        if i not in memory:
            memory.append(i)
            b[int(i)]=str(len(b[i]))+str('|')+str(f'{len(b[1])/c*100}:.1')+str('%')
    return b
print(analyt(input('input analytics----->')))
    


