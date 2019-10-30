def myfunction():
    'this function prints "hello function"'
    print('hello function')

print(myfunction.__doc__)
# print(myfunction.__annotations__)
myfunction()

def functionWithAnnotations(arg1: str, arg2: int):
    'this function has arguments annotations'
    print(functionWithAnnotations.__annotations__)

functionWithAnnotations(1,2)

# Lambda
def getIncrementorLambdaFunction(n):
    'this function returns a lambda function that will get a value and increment it.'
    return lambda x: x+n

incrementorlambda = getIncrementorLambdaFunction(5)

print(incrementorlambda(2))
