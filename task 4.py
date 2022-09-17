def cezar(s):
    res=[]
    
    alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in list(s):
        num=0
        while i!=alph[num]:
            num+=1


        if num+3>26:
            num=(num+3)%26
        res.append(alph[num+3])

    return res
print(cezar(input("write spy sentense--->")))

