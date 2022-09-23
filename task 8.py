c=int(input('input number-->'))
def rect(a=c):
    b = 0
    b = int(a)
    b = b*b
    return b

def rect2(a=c):
    b=c
    b*=c
    if b!=c*c:
        return rect2()
    else:
        return b
print(rect())
print(rect2())