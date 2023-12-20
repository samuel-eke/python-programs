from collections import namedtuple
goou = namedtuple('goou', 'x,y') #creates a class with x and y arguments
pi = goou(2, 4)#call it and supply arguments
print(pi)