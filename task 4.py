alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cezar(s):
    res=''
    
    
    for i in list(s):
        num=0
        while i!=alph[num]:
            num+=1


        if num+3>26:
            num=(num+3)%26
        res+=alph[num+3]

    return res


def cesar_back(s):
    restwo=''
    for i in list(s):
        num=0
        while i!=alph[num]:
            num+=1


        if num-3<=0:
            num=26+num-3
        restwo+=alph[num-3]
    return restwo
print(f'The code is {cezar(input("write spy sentense--->"))}')
code=int(2807)
if int(input('input code to see any true sentense-->'))==code:
    print(  f'Welcome!The real sentense is {cesar_back(input  ())   }')  


