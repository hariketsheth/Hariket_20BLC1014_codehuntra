t = int(input())
ss = 0
for i in range(t):
    count = 0
    visited, pair= [], []
    k, p = input(), list(input().split())
    k = [c for c in k]
    flag = True
    for i in range(len(k)):
        if(flag == True):
            if k[i] in visited:
                ind = visited.index(k[i])
                if (p[i][-1] == pair[ind]):
                    count += 1
                else:
                    flag = False
            else:
                if(p[i][-1] not in pair):
                    visited.append(k[i])
                    pair.append(p[i][-1])
                    count += 1
                else:
                    flag = False
        else:
            break
    ss += count
    print(count)
print(ss)
    
