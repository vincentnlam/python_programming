kingdoms = ["Bacteria", "Protozoa", "Chromista", "Plantae", "Fungi", "Animalia"]
print(kingdoms[0])
print(kingdoms[5])
print(kingdoms[0:3])
print(kingdoms[2:5])
print(kingdoms[4:6])
print(kingdoms[3:])
print(kingdoms[:4])

print(kingdoms[-6])
print(kingdoms[-1])
print(kingdoms[-6:-3])
print(kingdoms[-4:-1])
print(kingdoms[-2:])

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
print(whales[-1])
print(whales[-2])
print(whales[-14])
# whales = []
print(whales)
print(max(whales))
print(min(whales))
print(sum(whales))
print(sorted(whales))
print(sorted(whales, reverse=True))


krypton = ["Krypton", "Kr", -157.2, -153.4]
print(krypton[0])
print(krypton[-1])
krypton[2] = "John"
print(krypton)
krypton[3] = "James"
print(krypton)
print(len(krypton))


nobles = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
print(nobles)

gas = "Helium"
if gas.lower() in nobles:
    print(f"{gas} is in the list")
else:
    print(f"{gas} is not in the list")


appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
# appointments.append("16:30")
print(appointments)
appointments = appointments + ["16:30"]
print(appointments)


ids = [4353, 2314, 2956, 3382, 9362, 3900]
ids.remove(3382)
print(ids)
print(ids.index(9362))
ids.insert(4, 4499)
print(ids)
ids.extend([5566,1830])
print(ids)
ids.reverse()
print(ids)
ids = sorted(ids)
# ids.sort()
print(ids)

alkaine_earth_metals = [4, 12, 20, 56, 88]
print(alkaine_earth_metals[4])
print(alkaine_earth_metals[-1])
print(len(alkaine_earth_metals))
print(sum(alkaine_earth_metals))
print(max(alkaine_earth_metals))

temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
print(sorted(temps))
temps.sort()
print(temps)
cool_temps = temps[0:2]
print(cool_temps)
warm_temps = temps[2:6]
print(warm_temps)
temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)

def same_first_last(L: list) -> bool:
    """Precondition: len(L) >= 2
    Return True if and only if first item of the list is the same as the
    last.
    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    >>> same_first_last([4.0, 4.5])
    """
    first_item = L[0]
    last_item = L[-1]
    if first_item ==last_item:
        return True
    else:
        return False
    
print(same_first_last([3, 4, 2, 8, 3]))
print(same_first_last(["apple", "banana", "pear"]))
print(same_first_last([4.0, 4.5]))

values = [0, 1, 2]
print(values)
values[1] = values
print(values)

# To do, 8, 10, 11

def is_longer(L1: list, L2: list) -> bool:
    """Return True if and only if the length of L1 is longer than the length
    of L2.
    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3]
    """
    if len(L1) > len(L2):
        return True
    else: 
        return False

print(is_longer([1, 2, 3], [4, 5]))    
print(is_longer(['abcdef'], ['ab', 'cd', 'ef']))
print(is_longer(['a', 'b', 'c'], [1, 2, 3]))

# exercise 10
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print(units[0])
print(units[1])
print(units[0][0])
print(units[1][0])
print(units[0][1:])
print(units[1][0:2])
print(units[-2])
print(units[-1])
print(units[-2][-3])
print(units[-1][-3])
print(units[-2][-2:])
print(units[-1][-3:-1])
