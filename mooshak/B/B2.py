__author__ = 'xyax'

pal = raw_input().strip()
def anagrams(word):
    if len(word) < 2:
        return word
    else:
        tmp = list()
        for i, letter in enumerate(word):
            for j in anagrams(word[:i]+word[i+1:]):
                tmp.append(j+letter)
    return tmp

out = anagrams(pal)
if len(out) > 1:
    out.sort()
    print '\n'.join(out)
else:
    print out