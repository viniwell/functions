def tom(d,m,y):
    """returns tomomorrow and yesterday date
    args:
    d,m,y-int"""
    d+=1
    d31=[1,3,5,7,8,10,12]
    d28=[2]
    d30=[2,4,7,9]
    if y%4==0:
        if m in d31:
            if d>32:
                m+=1
                if m>12:
                    m=1
                    y+=1
                d%=32
        if m in d31:
            if d>30:
                m+=1
                if m>12:
                    m=1
                    y+=1
                d%=31
        if m in d28:
            if d>30:
                m+=1
                if m>12:
                    m=1
                    y+=1
                d%=30


    if y%4!=0:
        if m in d31:
            if d>32:
                m+=1
                if m>12:
                    m=1
                    y+=1
                d%=32
        if m in d30:
            if d>30:
                m+=1
                if m>12:
                    m=1
                    y+=1
                d%=31
        if m in d28:
            if d>28:
                m+=1
                if m>12:
                    m=1
                    y+=1
                d%=29


    
    return [d, m, y] 
def yest(d,m,y):
    d-=1
    d31=[1,3,5,7,8,10,12]
    d28=[2]
    d30=[2,4,7,9]
    if y%4==0:
        if m in d31:
            if d==0:
                m-=1
                if m==0:
                    m=12
                    y-=1
                d=31
        if m in d30:
            if d==0:
                m-=1
                if m==0:
                    m=12
                    y-=1
                d=30
        if m in d28:
            if d==0:
                m-=1
                if m==0:
                    m=12
                    y-=1
                d=29


    if y%4!=0:
        if m in d31:
            if d==0:
                m-=1
                if m==0:
                    m=12
                    y-=1
                d=31
        if m in d30:
            if d==0:
                m-=1
                if m==0:
                    m=12
                    y-=1
                d=30
        if m in d28:
            if d==0:
                m-=1
                if m==0:
                    m=1
                    y-=1
                d=28
    return [d,m,y]                      
print(tom(*list(map(int, input('date-->').split('.'))))) 
print(yest(*list(map(int, input('date-->').split('.')))))       

