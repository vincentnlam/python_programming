print("__name__ is", __name__)

def FtoC(f):
    c = (f-32)*5/9
    return c

def CtoF(c):
    f = (c*9/5)+32
    return f

def above_freezing(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.
    >>> above_freezing(5.2)
    True
    >>> above_freezing(-2)
    False
    """
    return celsius > 0

# print(above_freezing(0))

def above_freezing_v2(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.
    >>> above_freezing_v2(5.2)
    True
    >>> above_freezing_v2(-2)
    False
    """
    return celsius >= 0
# print(above_freezing_v2(0))

if __name__ == "__main__":
    print(above_freezing(-4))