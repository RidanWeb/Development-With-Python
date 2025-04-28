
n = int(input())

myList = list(map(int, input().split()))

count = 0

flag = True

while flag:

    for i, v in enumerate(myList):

        if myList[i] % 2 != 0:
            flag = False
            break

    if flag:
        myList = [x // 2 for x in myList]
        count += 1



print(count)


        
