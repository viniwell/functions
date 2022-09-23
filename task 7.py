def pol_otr(a):
    a=list(a)
    pol={}
    for i in a:
        if i<0:
            pol['-'].append(i)
