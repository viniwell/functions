def analyt(a,c=0):
    a=list(a)
    b={}
    for i in a:
        if i!=0:
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
                b[str(i)]=str(len(b[i]))+str('|')+str(f'{len(b[1])/c*100}:.1')+str('%')
    return b
print(analyt(input('input analytics----->')))
    


