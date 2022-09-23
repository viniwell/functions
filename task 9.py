n=(input("input number-->"))


def sum(a=str(n),i=-1,suma=0):
    i+=1
    a=list(a)
    suma+=int(a[i])
    if i+1==len(a):
        return suma
    else: 
        return(sum(i=i,suma=suma))
print(sum())
