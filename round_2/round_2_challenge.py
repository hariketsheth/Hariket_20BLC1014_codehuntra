s = input()
final = []
for i in range (1,len(s)+1):
    temp = s[:i]
    if(temp == temp [::-1]):
        final.append(temp)
final.sort()
word = ''.join(final)
for i in range(len(word)):
    if(i%47==0 and i!=0):
        print(word[i],end='')
