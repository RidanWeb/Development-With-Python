import math
import time
import datetime


def timer(func):


    def inner(*args, **kwargs):
        print("Time started")
        print(datetime.datetime.now())
        time.sleep(2)
        func(*args, **kwargs)
        print(datetime.datetime.now())
        print("Time Ended")

    return inner





# timer()#return nothing
# timer()()


@timer
def getFactorial(n):
    print("Factorial started")
    fact = math.factorial(n)
    print(f"Factorial of {n} is {fact}")

    print("Factorial ended")



getFactorial(n = 5)

#longCut
# timer(getFactorial)()

