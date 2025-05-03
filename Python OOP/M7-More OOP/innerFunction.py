def outerFunction():

    print("Outer function")

    def innerFunction():
        print("Inner function")

        return "Inner function return value"
    
    return innerFunction


print(outerFunction())
print(outerFunction()())



def doSomething(work):
    print("Doing something started")

    work()

    print("Done something ended")



def work():
    print("Doing work")


doSomething(work)