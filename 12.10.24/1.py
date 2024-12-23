a=[1, -99999, 7878723, 2, 8758, 123124, -1, 12326713123, -1, 555, 600, 86]
c=1
def func(a,c):
    raz=max(a)+2
    sum=0
    list2=[0,0,0,0]
    for q in range(len(a)-3):
        for w in range(q+1,len(a)-2):
            for e in range(w+1,len(a)-1):
                for r in range(e+1,len(a)):
                    if (a[q]+a[w]+a[e]+a[r])>c:
                        if ((a[q]+a[w]+a[e]+a[r])-c)<raz:
                            raz = ((a[q]+a[w]+a[e]+a[r])-c)
                            list2[0]=(a[q])
                            list2[1]=(a[w])
                            list2[2]=(a[e])
                            list2[3]=(a[r])
                            sum = (a[q]+a[w]+a[e]+a[r])
                    if (a[q]+a[w]+a[e]+a[r])<c:
                        if (c-(a[q]+a[w]+a[e]+a[r]))<raz:
                            raz = (c-(a[q]+a[w]+a[e]+a[r]))
                            list2[0]=(a[q])
                            list2[1]=(a[w])
                            list2[2]=(a[e])
                            list2[3]=(a[r])
                            sum = (a[q]+a[w]+a[e]+a[r])
                    if (a[q]+a[w]+a[e]+a[r])==c:
                        raz=0
                        list2[0]=(a[q])
                        list2[1]=(a[w])
                        list2[2]=(a[e])
                        list2[3]=(a[r])
                        sum = (a[q]+a[w]+a[e]+a[r])
                        return (list2,sum)
    return(list2, sum)                   
print(func(a,c))