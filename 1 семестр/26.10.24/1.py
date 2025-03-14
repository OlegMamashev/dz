a = "qwe ewq asd dsa dsas qwee zxc cxz xxz z s qweasdzxc zzxc"
list = a.split()

def getletters(word):
    letters = dict()
    if word:
        for n in range(len(word)):
            if word[n] in letters:
                letters[f'{word[n]}'] = letters.get(f'{word[n]}',0) + 1 
            else:
                letters.setdefault(word[n],1)
        return(letters)
    else:
        return 0

words = []
for i in range(len(list)):
    letter1 = getletters(list[i])
    schet=0
    for n in range(i+1, len(list)):
        letter2 = getletters(list[n])
        if letter1 == letter2:
            words.append([list[i], list[n]])
            list[n] = None
            schet = 1
            break

    if schet == 0 and list[i]:
        words.append([list[i]])
print(words)