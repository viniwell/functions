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
def lenght(i=-1,a=str(n)):
    a=list(a)
    i+=1
    if i!=len(a):
        return(lenght(i=i))
    else:
        return i
print(lenght())
