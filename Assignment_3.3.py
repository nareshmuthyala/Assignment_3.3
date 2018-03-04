def longestWord(lst):
    if len(lst)==0:
        print("list is empty")
        return
    length = 0
    index = 0
    for x in range(0,len(lst)):
        if(len(lst[x])>length):
            length = len(lst[x])
            index = x
    return lst[index]
string3 = 'abcdef'
list1 = [i*string3[i] for i in range(0,len(string3))]
print(list1)
longestWord(list1)