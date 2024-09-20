vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)
vowels = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
print(vowels)

numbers = set([2, 3, 2, 5])
print(numbers)
numbers2 = set(range(15))
print(numbers2)
vowels.add('y')
print(vowels)
lows = {0, 1, 2, 3, 4}
odds = {1, 3, 5, 7, 9}
print(lows)
print(f"odds: {odds}")
lows.add(9)
print(f"lows: {lows}")
x = lows.difference(odds)
print(f"x: {x}")
y = lows.intersection(odds)
print(f"y: {y}")
ten = set(range(10))
print(f"ten: {ten}")
z = lows.union(odds)
print(z)
print(lows.issubset(ten))
print(lows.issuperset(ten))
print(ten.issuperset(lows))
bases = ('A', 'C', 'G', 'T')
print(bases)
for base in bases:
    print(base)

life = (['Canada', 76.5],['United states', 75.5],['Mexico', 72.0], ['Thailand', 70])
print(life[0])
print(life[0][0])
print(life[0][1])
print(life[1][0])
print(life[1][1])
print(life[2][0])
print(life[2][1])
for item in life:
    print(f"country: {item[0]} age: {item[1]}")

bird_to_observations = {'canada goose': 3, 'northern fulmar': 1, "eagle": 4}
print(bird_to_observations)

for key,value in bird_to_observations.items():
    print(f"bird: {key} observation: {value}")

if "canada goose" in bird_to_observations:
    print(f"We saw canada goose {bird_to_observations['canada goose']} times")

if "eagle" in bird_to_observations:
    print(f"We saw eagle {bird_to_observations['eagle']} times")
else:
    print("We did not see eagle")

print(bird_to_observations.get("canada goose"))
print(bird_to_observations.get("tiger"))

print(bird_to_observations.get("canada goose", 0))
print(bird_to_observations.get("tiger", 0))
print(bird_to_observations.keys())
print(bird_to_observations.items())
bird_to_observations.pop("eagle")
print(bird_to_observations)
print(bird_to_observations.values())

bird_to_observations2 = {"canada goose": 10, "eagle": 6}

bird_to_observations.update(bird_to_observations2)
print(bird_to_observations)

#exercise 1 
numbers = [3,4,6,9,5,1,2,5,5,7,8,4,9]
def find_dups(nums):
    #print(nums)
    seen = {}
    for num in nums:
        #print(num)
        if num in seen:
            seen[num] += 1
        else: 
            seen[num] = 1
    #print(seen)
    answer = []
    for key, value in seen.items(): 
        #print(key, value)
        if value >= 2:
            answer.append(key)
    return answer
ans = find_dups(numbers)
print(ans)
# Exercise 2
# Refer to multimol2.py
# Exercise 3
males = {"James", "John", "Joseph", "Tom", "Bob"}
females = {"Mary", "Cathy", "Barbara", "Julia", "Katherine"}
def pairs(a, b):
    # print(a)
    # print(b)
    result = set()
    for x,y in zip(a, b):
        # print(x,y)
        result.add((x,y))
    return result


print(pairs(males, females))
 
#Exercise 5 

def count_values(d):
    result = set()
    for k,v in d.items(): 
        result.add(v)
    return len(result)
colors = {"red": 1, "green": 1, "blue": 2, "gray" :3, "purple" :5}
print(count_values(colors))      

p = {"neutron": 0.55, "proton": 0.21, "meson": 0.03, "muon": 0.07, "neutrino": 0.14}
def least_likley_particles(particles):
    least_likley_particle = None
    smallest_probability = None
    for k,v in particles.items():
        # print(k,v)
        if not smallest_probability:
            smallest_probability = v
        elif v < smallest_probability:
            smallest_probability = v
            least_likley_particle = k
    return least_likley_particle
print(least_likley_particles(particles = p))     

#Exercise 7

def count_duplicates(d):
    result = set()
    answer = []
    for k,v in d.items(): 
        if v not in result:
            result.add(v)
        else:
            answer.append(v)
    return len(answer)
colors = {"red": 1, "green": 2, "blue": 2, "gray" :1, "purple" :5, "pink": 5, "white": 6, "black": 6}
print(count_duplicates(colors)) 


#Exercise 8

colors = {"R": 0.3, "G": 0.3, "B": 0.4}
def is_balanced(c):
    total = 0
    for k,v in c.items():
        total += v
    if total == 1:
        return True
    else:
        return False
print(is_balanced(colors))

#Exercise 9

A = {"R": 0.1, "G": 0.2, "B": 0.5, "Y": 0.9}
B = {"R": 0.1, "P": 0.5, "Y": 0.9}

def dict_intersect(a,b):
    result = {}
    for k,v in a.items():
        print(k,v)
        if b.get(k):
            value = b.get(k)
            print(f"value: {value}")
            result[k] = value
    return result
print(dict_intersect(A,B))

#Exercise 10

authors = {
    'jgoodall' : {'surname' : 'Goodall',
            'forename' : 'Jane',
            'born' : 1934,
            'died' : None,
            'notes' : 'primate researcher',
            'author' : ['In the Shadow of Man',
            'The Chimpanzees of Gombe']},
    'rfranklin' : {'surname' : 'Franklin',
            'forename' : 'Rosalind',
            'born' : 1920,
            'died' : 1957,
            'author' : ['The Wimpy Kid'],
            'notes' : 'contributed to discovery of DNA'},
    'rcarson' : {'surname' : 'Carson',
            'forename' : 'Rachel',
            'born' : 1907,
            # 'died' : 1964,
            'notes' : 'raised awareness of effects of DDT',
            'author' : ['Silent Spring']}
}

def dbheadings(d):
    headings = set()
    for k,v in d.items():
        # print(f"key: {k}")
        # print(f"VALUE: {v}")
        for g,h in v.items():
            # print(g,h)
            headings.add(g)
    return headings

print(f"ex.10: {dbheadings(authors)}")

def db_consistent(d):
    headings = set()
    print(f"headings in the beginning: {headings}")
    for k,v in d.items():
        # print(f"key: {k}")
        # print(f"VALUE: {v}")
        for g,h in v.items():
            # print(g,h)
            headings.add(g)
    # print(f"headings at the end of the loop: {headings}")
    for k,v in d.items():
        inner_headings = set()
        for g,h in v.items():
            inner_headings.add(g)
        # print(k, inner_headings)
        # print(f"headings:  {headings - inner_headings}")
        if (headings - inner_headings):
            return False
    return True
print(db_consistent(authors)) 

#Exercise 12

d1 = {0:1, 1:2, 2:3}
d2 = {0:4, 1:5, 2:6}

# print(d1.get(6))
# print(d2.get(7))
# print(d1.get(9) or 0)


def sparse_add(d1, d2):
    f1 = {}
    for key in set(list(d1.keys()) + list(d2.keys())):
        value1 = d1.get(key) or 0
        value2 = d2.get(key) or 0
        # print(key, value1, value2)
        answer = value1 + value2
        f1[key] = answer
    return f1
print(sparse_add(d1, d2))

def sparse_dot(d1, d2):
    f1 = {}
    total = 0
    for key in set(list(d1.keys()) + list(d2.keys())):
        value1 = d1.get(key) or 0
        value2 = d2.get(key) or 0
        # print(key, value1, value2)
        answer = value1 * value2
        f1[key] = answer
    for key, value in f1.items():
        total = total + value
    return total
print(sparse_dot(d1, d2))