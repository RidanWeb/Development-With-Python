from collections import Counter


n = int(input())


count = 0

myList = list(map(int, input().split()))



myDist = Counter(myList)




for num, val in myDist.items():

    if val < num:

        count += val

    elif val > num:

        count += (val - num)








print(count)

