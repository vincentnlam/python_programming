print(True and not False)
print(True or (True and False))
print(not True or not False)
print(not 1)
print(True and not 0)
print(52 < 52.3)
print(1 + 52 < 52.3)
print(4 != 4.0)
light = 0.0
temperature = 1.0
if (light < 0.01) or (temperature > 0.0):
    if not ((light < 0.01) and (temperature > 0.0)):
        print("camera is on")
if (light < 0.01) != (temperature > 0.0):
    print("camera is on")
x = -3
print(x == abs (x)) 
def different(a, b):
    if a != b:
        return True
    elif a == b:
        return False 
    
print(different(1, 4))
population = 10000.00
land_area = 100.00
if population < 10000000:
    print(population)
if (population > 10000000) and (population < 35000000):
    print(population)
land_density = population/land_area 
if land_density > 100:
    print(land_density)
    print("Densley populated")
else:
    print("Sparsely populated")

