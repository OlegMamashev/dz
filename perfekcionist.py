text=str(input())
a=int(input())


def Nedostatok_bukv(n):
    sm = n - 2
    if (len(text)//2)>=n:
        skolkoDolzno=(len(text)//n)*n+sm*((len(text)//n)-1)
        nedostatok_bukv=skolkoDolzno-len(text)

        return(nedostatok_bukv)
    else:
        skolkoDolzno=2*n+sm
        nedostatok_bukv=skolkoDolzno-len(text)
        return(nedostatok_bukv)





def F(n):

    if n==1:
        return(text)

    sm = n - 2
    prBukv = (n-1) + sm
    newWord=''
    nedostatokBukv=Nedostatok_bukv(a)
    newtext=text + nedostatokBukv*"I" +(sm+1)*"I"
    skok=(len(newtext)//(prBukv+1))+1
    prBukv1=(prBukv+1)


    for i in range(0,n):
        if i!=0:
            prBukv1=prBukv1-2
        if i==0:
            for x in range(0,len(newtext),(prBukv+1)):
                newWord=newWord+newtext[x]
                newtext=newtext[:x] + "I" + newtext[x+1:]
        if i==(n-1):
            for x in range((n-1), len(newtext), (prBukv + 1)):
                newWord = newWord + newtext[x]
                newtext=newtext[:x] + "I" + newtext[x+1:]
        if i!=0 and i!=(n-1):
            schet = 2
            pp=0
            tt=0
            for x in range(i,len(newtext),prBukv1):
                tt+=1
                if tt==4:
                    tt=0
                    pp=0
                    schet=2

                schet = schet + 1
                if x<(len(newtext)-(prBukv)):
                    if schet%2==0:
                        newWord= newWord + newtext[x] + newtext[x+i*2]
                        newtext=newtext[:x] + "I" + newtext[x+1:]
                        newtext = newtext[:(x+i*2)] + "I" + newtext[(x+i*2) + 1:]
                        pp=i*2
                    if schet%2!=0:
                        newWord = newWord + newtext[x+pp]
                        newtext=newtext[:(x+pp)] + "I" + newtext[(x+pp)+1:]





    while "I" in newWord:
        newWord=newWord.replace("I","",1)


    return(newWord)


print(F(a))