velocities = [0.0, 9.81, 19.62, 29.43]
print(velocities)
print(velocities[0]*3.28)
print(velocities[1]*3.28)
print(velocities[2]*3.28)
print(velocities[3]*3.28)

for i in range(len(velocities)):
    print(velocities[i]*3.28)

for velocity in velocities:
    print(velocity*3.28)

country = 'United States of America'

for ch in country:
    if ch.isupper():
        print(ch)

print(range(10))

print(list(range(5)))

for i in range(10):
    print(i)

outer = ['Li', 'Na','K']
inner = ['F', 'Cl', 'Br']
for m in outer:
    for h in inner:
        print(m + h)

# Exercise 1
celegans_phenotypes = ['Emb','Him', 'Unc', 'Lon', 'Dpy', 'Sma']
for item in celegans_phenotypes:
    print(item)

for i in range(len(celegans_phenotypes)):
    print(celegans_phenotypes[i])

# Exercise 2 
half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
for item in half_lives:
    print(item, end = "\n")

more_whales = []
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
for item in whales:
    more_whales.append(item + 1)
print(more_whales)

alkaline_earth_metals = [["beryluim", 4, 9.012], ["magnesium", 12, 24.305], ["calcium", 20, 40.078], ["strontium", 38, 87.62], ["barium", 56, 137.327], ["radium", 88, 226]]
for item in alkaline_earth_metals:
    print(f"{item[0]}\n{item[1]}\n{item[2]}")
number_and_weight = []
for item in alkaline_earth_metals:
    number_and_weight.append(item[1])
    number_and_weight.append(item[2])
print(number_and_weight)

#Exercise 6
# while True:
#     text = input("Please enter a chemical formula (or 'quit' to exit): ")
#     if text.lower() == "quit":
#         print("…exiting program")
#         break
#     elif text == "H2O":
#         print("Water")
#     elif text == "NH3":
#         print("Ammonia")
#     elif text == "CH4":
#         print("Methane")
#     else:
#         print("Unknown compound")

#Exercise 7
total = 0
country_populations = [1295, 23, 7, 3, 47, 21]
for item in country_populations:
    # print(item)
    total = item + total 

print(total)

#Exercise 8
rat_1 = [11,2,3,4,5,6,7,8,9,10]
rat_2 = [10,9,8,7,6,5,4,3,2,11]
if rat_1[0] > rat_2[0]:
    print("Rat 1 weighed more than rat 2 on day 1") 
else:
    print("Rat 1 weighed less than rat 2 on day 1")
if rat_1[0] > rat_2[0]:
    if rat_1[9] > rat_2[9]:
        print("Rat 1 remained heavier than rat 2")
    else:
        print("Rat 2 became heavier than Rat 1")

#Exercise 9
for i in range(33,50):
    print(i)

#Exercise 10
for i in range(10,0,-1):
    print(i)

#Exercise 11
sum = 0
for i in range(2,23):
    sum = i + sum
    print(i,sum)
print(sum)

#Exercise 12
from typing import List
def remove_neg(num_list: List[float]) -> None:
    """Remove the negative numbers from the list num_list.
    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numbers
    [1, 2]
    """

    new_list = []
    for item in num_list:
        print("item", item)
        if item > 0:
            new_list.append(item)
    
    return new_list

numbers = [1,2,3,-3,6,-1,-3,1]
print(numbers)
new_numbers = remove_neg(numbers)
print(new_numbers)

def draw_triangle(rows, columns):
    for i in range(1, rows +1, 1):
        for j in range(1, i +1, 1):
            print("T", end = "")
        print("")

draw_triangle(4,4)
print("-" * 10)


def draw_triangle2(rows, columns):
    for i in range(1, rows +1, 1):
        for j in range(columns, 0, -1):
            # print('i:', i, "j", j)
            if (i >= j):
                print("T", end = "")
            else:
                print(" ", end = "")
        print("")

draw_triangle2(5,5)





# for i in range(0, 10, 1):
#     print(i)

# print("-" * 10)
# for i in range(7, 2, -1):
#     print(i)


# 16

i = 0
while (i<5):
    print(i)
    i=i+1

rat_1_weight = 10
rat_2_weight = 12
rat_1_rate = 0.1
rat_2_rate = 0.05
week = 1

rat_1_orig_weight = rat_1_weight
while (rat_1_weight < (rat_1_weight + (rat_1_orig_weight * .25))):
    rat_1_weight = rat_1_weight + rat_1_weight * rat_1_rate
    print(f"Week {week}: {rat_1_weight}")
    week = week + 1

print(f"rat 1 weighs {rat_1_weight} after {week} week(s).")

rat_1_weight = 10
rat_2_weight = 10
rat_1_rate = 0.2
rat_2_rate = 0.1
week = 1

while (rat_1_weight < (rat_2_weight + (rat_2_weight * .10))):
    rat_1_weight = rat_1_weight + rat_1_weight * rat_1_rate
    rat_2_weight = rat_2_weight + rat_2_weight * rat_2_rate
    print(f"Week {week}: {rat_1_weight}")
    week = week + 1

print(f"it takes {week} weeks for rat 1 to be 10 percent heavier than rat 2")
