'''
lambda function assigns a one-line function to a variable
'''
multi5 = lambda b: b * 5
print("Result of a lambda function",multi5(23)) #with one argument

subfunc =  lambda b, c: b - c

print("Result of a lambda function with 2 arguments",subfunc(32, 42))