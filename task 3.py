def get_analytics(s):
    analytics={}
    memory=[]
    for i in list(s):
        i=i.lower()
        if i not in memory: 
            analytics[i]=0
            analytics[i]+=1
            memory.append(i)
        else:
            analytics[i]+=1



    return analytics
print (get_analytics(input("write sentense-->")))
         
