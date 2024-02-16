import math


print(str.capitalize("vincent"))
print("vincent".capitalize())
print("vincent".upper())
print("VINCENT".lower())
print("g"*3)
print(('TTA' + 'G' * 3).count('T'))
print("vincent n'lam".count("n"))
print("vincent".endswith("vi"))
print("vincent".find("n"))
print("vincent".islower())
print("vincent".isupper())
print("VINCENT".isupper())
first_name = "vincent      "
first_name = first_name.strip()
last_name = "n'lam         "
last_name = last_name.strip()
print(f"{first_name} {last_name}")
print(first_name.swapcase())
print('species'.startswith('spe'))
print('"{0}" is derived from "{1}"'.format('none', 'no one'))
print('"{0}" is my first name and "{1}" is my last name'.format("Vincent", "N'lam"))
print(math.pi)
print('Pi rounded to {0} decimal places is {1:.2f}.'.format(2, math.pi))
print("vincent".__add__("n'lam"))
print(3 + 5)
print(3 .__add__(5))
print("hello".upper())
print("Happy Birthday!".lower())
print("WeeeEEEeeeEEEeee".swapcase())
print("ABC123".isupper())
print("aeiouAEIOU".count("a"))
print("hello".endswith("o"))
print("hello".startswith("H"))
print("Hello {0}".format("Python"))
print("Hello {0}! Hello {1}! {2}".format("Python", "World", "A"))
print("tomato".count("o"))
print("tomato".find("o"))
print("tomato".find( "o", 2))
print("tomato".find("o", 1 + ("tomato".find("o"))))
print("avocado".find("o", 1 + ("avocado".find("o"))))
print("runner".replace("n","b"))
s = " yes  "
print(s.strip())
fruit = "pineapple"
print(fruit.find("p", fruit.count("p")))
print(fruit.count(fruit.upper().swapcase()))
print(fruit.replace(fruit.swapcase(), fruit.lower()))
#finished number 8
print("My Name is {0} {1}".format(first_name, last_name))
print(f"My name is {first_name} {last_name}")
season = "summer"
print(f"I love {season}")
print("I love {0}!".format(season))
side1 = 3
side2 = 4
side3 = 5
print("The sides have lengths {0}, {1}, {2}.".format(side1, side2, side3))
print(f"The sides have lengths {side1}, {side2}, {side3}.")
print("boolean".capitalize())
print("CO2 H2O".find("2"))
print("CO2 H2O".find("2", 1 + ("CO2 H2O".find("2"))))
print("Boolean".islower())
print("MoNDay".lower().capitalize())
print("  Monday".lstrip())
def total_occurrences(s1, s2, ch):
    return ((s1.count(ch)) + (s2.count(ch)))
    
print(total_occurrences("color", "yellow", "l"))
print(total_occurrences("red", "blue", "l"))
print(total_occurrences("green", "purple", "b"))