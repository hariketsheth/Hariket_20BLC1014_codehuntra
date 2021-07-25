list1 = list(map(int, input().split(',')))
list2 = list(map(int, input().split(',')))
list1.sort()
list3 = []
for i in list2:
    for j in range(len(list1)):
        if(list1[j] == i):
            list3.append(list1[j])
    list4 = list3.copy()
for i in list1:
    if i not in list4:
        list3.append(i)
for i in list3:
    if(i+96 == 123):
        print("/", end='')
    else:
        print(chr(i+96), end='')

