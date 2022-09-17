def get_lucky_tic(a, b):
    """return count of lucky tickets()
    
    
    a, b- int
    list returns lucky tickets from a to b
    """
    lucky_tic=[]
    for i in range(a, b+1):
        digits = 0
        num=i
        while num>0:
            if num%10%2==0:
                digits+=1
            num//=10
        if 2*digits==len(str(i)):
            lucky_tic.append(i)
    return lucky_tic

print(get_lucky_tic(*list(map(int, input().split(' ')))))            

