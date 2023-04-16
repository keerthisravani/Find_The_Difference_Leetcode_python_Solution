def findTheDifference(s, t):
    n=len(t)
    for i in t:
        if s.count(i)<t.count(i):
            return i
s="abcd"
t="abcde"
print(findTheDifference(s,t))



    