print("__name__ is", __name__)

def FtoC(f):
    c = (f-32)*5/9
    return c

def CtoF(c):
    f = (c*9/5)+32
    return f

def above_freezing(celsius):
    return celsius > 0

if __name__ == "__main__":
    print(above_freezing(-4))