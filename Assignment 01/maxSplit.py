myStr = input()

start = 0
balance = 0
count = 0
subStr = []

for  i, char in enumerate(myStr):
    if(char == 'L'):
        balance += 1
    elif(char == 'R'):
        balance -= 1
    if(balance == 0):
        count += 1
        subStr.append(myStr[start:i+1])
        start = i + 1

print(len(subStr))

for sub in subStr:
    print(sub)
