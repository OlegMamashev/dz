text="}{[()]}{}}}{(({{[[]]}})){{{[[[(((())))]]]}}}}{"
a=[]
n=0
text1=""
text2=""
num=0

def F(n,s):
    if len(n)>len(s):
        return n
    else:
        return s
def R(n):
    text1=""
    text2=""
    n=n[::-1]
    for i in n:
        if i==")" or i=="]" or i=="}":
            if i==")":
                text2=text2+"("
                text1=i+text1
            if i=="]":
                text2=text2+"["
                text1=i+text1
            if i=="}":
                text2=text2+"{"
                text1=i+text1
        else:
            break
    return (text2+text1)


for i in text:

    if i=="(" or i=="[" or i=="{":
        if text1:
            if text1[-1]==")" or text1[-1]=="]" or text1[-1]=="}":
                text2=F(R(text1),R(text2))
                text1=""
        a.append(i)
        text1=text1+i

    if i==")" and "(" in a:
        if a[-1]=="(":
            a.remove("(")
            text1 = text1 + i
        else:
            a.clear()
            text2=F(R(text1),R(text2))
            text1=""
            num+=1

    if i=="]" and "[" in a:
        if a[-1] == "[":
            a.remove("[")
            text1 = text1 + i
        else:
            a.clear()
            text2 = F(R(text1),R(text2))
            text1 = ""
            num+=1

    if i=="}" and "{" in a:
        if a[-1] == "{":
            a.remove("{")
            text1 = text1 + i
        else:
            a.clear()
            text2 = F(R(text1),R(text2))
            text1 = ""
            num+=1
print(text2)
if num==0:
    print("True")
else:
    print(R(text2))