text=str(input())

def F(n):
    text = ""
    break1=0
    for i in range(0,len(n)-1):
        for x in range(i+1,len(n)):
            if n[i]==n[x]:
                text=n[i:x]
                break1=100
                break
        if break1==100:
            break
    if len(text)!=0:
        return text
    else:
        return ""

def max_text_bez_povtora(n):

    text = ""
    break1=0

    for i in range(0,len(n)-1):

        for x in range(i+1,len(n)):

            if n[i]==n[x]:
                if len(text)<len(n[:x]) or len(text)<len(n[i:x]) or len(text)<len(F(n[x:])):
                    if len(n[:x])>=len(n[i:x]):
                        text=n[:x]
                    if len(n[:i])<len(n[i:x]):
                        text=n[i:x]
                    if len(text)<len(F(n[x:])):
                        text=F(n[x:])

                    break1=100
                    break

        if break1==100:
            break

    if len(text)!=0:
        return(text)
    else:
        return("False")

text1=max_text_bez_povtora(text)
while max_text_bez_povtora(text1)!="False":
    text1=max_text_bez_povtora(text1)


print(text1)