__author__ = 'xyax'

pal = raw_input()

def anagrams(word):
    if len(word) == 1:
        yield word
    for i, letter in enumerate(word):
        for s in anagrams(word[i+1:] + word[:i]):
            yield '%s%s' % (letter, s)

lout= list(anagrams(pal))
lout.sort()
for o in lout:
    print o