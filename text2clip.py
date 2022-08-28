def text2list(text):
    blist = []
    text = text.split('\n')

    for a in text:
        if ',' in a:
            blist.append(a)

        for b in range(len(blist)):
            if blist[b][::-1].find(',') ==4:
                blist[b] = blist[b][:-1]
            blist[b] = blist[b].replace(",","")

    return blist

def list2clipboard(list):
    clip = ""
    for a in list:
        clip += a + "\n"

    return clip[:-1]