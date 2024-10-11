import time
import random
counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
# using random.sample()
# to generate random number list
counts = random.sample(range(1, 100), 50)
print(counts)

print(min(counts))
low = min(counts)
print(low)
print(counts.index(low))

def find_two_smallest(L):
    smallest = min(L)
    min1 = L.index(smallest)
    # print(smallest)
    # print(min1)
    L.remove(smallest)
    next_smallest = min(L)
    min2 = L.index(next_smallest)
    # print(next_smallest, min2)
    L.insert(min1, smallest)
    if min1 <= min2:
        min2 += 1

    return(min1, min2)

def find_two_smallest2(L):
    temp_list = sorted(L)
    print(temp_list)
    smallest = temp_list[0]
    for i in range(len(temp_list)):
        if temp_list[i] > smallest:
            next_smallest = temp_list[i]
            break
    # print(smallest, next_smallest)
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)
    return (min1, min2)

t1 = time.perf_counter()
print(find_two_smallest(counts))
t2 = time.perf_counter()
print(f'The code took {t2 - t1}')

t1 = time.perf_counter()
print(find_two_smallest2(counts))
t2 = time.perf_counter()
print(f'The code took {t2 - t1}')


# Exercise 1
def DNA_complement(s):
    complement = ''
    for letter in s:
        if letter == 'A':
            complement += 'T'
        if letter == 'T':
            complement += 'A'
        if letter == 'G':
            complement += 'C'
        if letter == 'C':
            complement += 'G'
    return complement

def DNA_complement2(s):
    s = s.replace('A','W')
    s = s.replace('T','X')
    s = s.replace('G','Y')
    s = s.replace('C','Z')

    s = s.replace('W','T')
    s = s.replace('X','A')
    s = s.replace('Y','C')
    s = s.replace('Z','G')
    return s

DNA = "AATTGCCGT"
t1 = time.perf_counter()
print(DNA_complement(DNA))
t2 = time.perf_counter()
print(f'The code took {t2 - t1}')

t1 = time.perf_counter()
print(DNA_complement2(DNA))
t2 = time.perf_counter()
print(f'The code took {t2 - t1}')

# Exercise 2
def min_or_max(l,min = True):
    if min == True:
        min = l[0] 
        min_index = 0
        for i in range(len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        return (min_index, min)
    elif min == False:
        max = l[0] 
        max_index = 0
        for i in range(len(l)):
            if l[i] > max:
                max = l[i]
                max_index = i
        return (max_index, max)

counts = [100, 809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
print(min_or_max(counts, min = True))
print(min_or_max(counts, min = False))

# Exercise 6

L2 = [4, 9, 8, 0, 0, 2, 1]
print(find_two_smallest2(L2))


# Exercise 7

def dutch_flag(f):
    ordered_flags = []
    for flag in f:
        if flag == 'red':
            ordered_flags.append(flag)
    for flag in f:
        if flag == 'green':
            ordered_flags.append(flag) 
    for flag in f:
        if flag == 'blue':
            ordered_flags.append(flag)       
    return ordered_flags
flags = ['red', 'red', 'green', 'blue', 'red', 'green']
print(dutch_flag(flags))