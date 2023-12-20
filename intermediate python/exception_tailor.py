class valuetoohigh (Exception):
    pass
class Valuetoosmall (Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 149:
        raise valuetoohigh ('Value is high')
    elif x < 10:
        raise Valuetoosmall ('Value is small', x)

try:
    test_value(2)
except valuetoohigh as e:
    print(e)
except Valuetoosmall as e:
    print(e.message, e.value)


