# # Second parameter can be optional if you give the default value like in the first programe.
def increment(num,by=1):
    return num+by
print(increment(2))

# #If the user provide the second parameter, the value of the second parameter will not be the default one(by=5)
def increment(num,by=0):
    return num+by
print(increment(2,5))

#If you did not provide the default value for the second parameter and pass only one parameter, it will cause error(ypeError: increment() missing 1 required positional argument: 'by')
def increment(num, by):
    return num+by
print(increment(2))
