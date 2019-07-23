

def frequencyDict(s):
    s = s.lower()
    d = {}
    for c in s:
        if c.isalpha():
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    return d

def canMake(w,fdict):
    d = frequencyDict(w)
    return all(d[c] <= fdict.get(c,0) for c in d)

def candidates(wlist,fdict):
    return [w for w in wlist if canMake(w,fdict)]


def anagrams(wlist,fdict):
    if len(wlist) == 0 or len(fdict) == 0:
        return "no anagrams"
    hits = []
    firstWords = candidates(wlist,fdict)
    if len(firstWords) == 0:
        return "no anagrams"
    for w in firstWords:
        #create reduced frequency dict
        d = fdict.copy() 
        for c in w:
            d[c] -= 1
            if d[c] == 0: del d[c]
        #if d is empty, the first word is also a the last word
        if len(d) == 0:
            hits.append(w)
        else:
            #create reduced word list
            rlist = [v for v in wlist if canMake(v,d)]
            tails = anagrams(rlist, d)
            if tails != "no anagrams":
                hits.extend(w + " " + t for t in tails)
    if len(hits) == 0:
        return "no anagrams"
    else:
        return hits

def findAnagrams(wlist,s):
    return anagrams(wlist,frequencyDict(s.lower()))

f = open("words_alpha.txt")
words = f.read().split('\n')
f.close()
words = [w.strip().lower() for w in words if not '-' in w]
test = findAnagrams(words, "Donald Trump")