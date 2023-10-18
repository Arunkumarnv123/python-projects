def binary_search(l,t,lw,hi):

    while(lw<hi):
        mp = (lw + hi) // 2
        if l[mp]==t:
            return mp
        elif t<l[mp]:
            hi=mp-1
        else :
            lw=mp+1
    return -1
l=[1,2,3,4,5,7,9]
t=9
print("binary_search pose = ",binary_search(l,t,0,len(l)))

def binary_search_rec(l,t,lw,hi):

    if hi<lw:
        return -1

    mp = (lw + hi) // 2
    if l[mp]==t:
        return mp
    elif t<l[mp]:
        return binary_search_rec(l,t,lw,mp-1)
    else :
        return binary_search_rec(l, t, mp+1,hi)
l=[1,2,3,4,5,7,9]
t=9
print("binary_search using recurtion  pos = ",binary_search_rec(l,t,0,len(l)))
