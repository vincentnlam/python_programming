import os

directory = os.getcwd()
print('directory', directory)
my_file = f'{directory}/test.txt'
print(my_file)
#open a file with read mode
with open(my_file, 'r') as file:
    contents = file.read()
print(contents)
topics_file = f'{directory}/topics.txt'
#open a file with write mode
with open(topics_file, 'w') as output_file:
    output_file.write('Computer Science\n')
    output_file.write('English\n')#open a file with append mode
with open(topics_file, 'a') as output_file:
    output_file.write('Software Engineering')


with open(my_file, 'r') as file:
    lines = file.readlines()


for i in range(len(lines)):
    print(lines[i].strip())

for line in lines:
    print(line.strip(),len(line)-1)

with open('hopedale.txt', 'r') as hopedale_file:
    # Read and skip the description line.
    hopedale_file.readline()
    # Keep reading and skipping comment lines until we read the first piece
    # of data.
    data = hopedale_file.readline().strip()
    print("DATA:", data)
    while data.startswith('#'):
        data = hopedale_file.readline().strip()
        print("DATA inside while:", data)
    # Now we have the first piece of data. Accumulate the total number of
    # pelts.
    total_pelts = int(data)
    # Read the rest of the data.
    for data in hopedale_file:
        total_pelts = total_pelts + int(data.strip())
print("Total number of pelts:", total_pelts)


import urllib.request
# url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
url = "https://vincentnlam.github.io"
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        try:
            line = line.decode('utf-8')
        except:
            pass
        print(line)
# file_name = input("Please enter a file name.")
# print(file_name)
# with open(file_name, "r") as input_file:
#     lines = input_file.readlines()

# print(lines)

#exercise 1
# new_file_name = f"{file_name}.bak"
# print(new_file_name)
# with open(new_file_name, "w") as output_file:
#     for line in lines:
#         output_file.write(line)

#exercise 2

with open("alkaline_metals.txt", "r") as input_file:
    lines = input_file.readlines()

metals = []
print("metals", metals)
for line in lines:

    line = line.strip()
    # print(line)
    elements = line.split()
    # print(elements) 
    metals.append(elements)
    
print("metals", metals)

#exercise 3
with open("alkaline_metals.txt", "r") as input_file:
    lines = input_file.readlines()
for line in lines:
    line = line.strip()
    print(line[::-1])
print("-" * 20)
with open("alkaline_metals.txt", "r") as input_file:
    lines = input_file.readlines()
lines.reverse()
for line in lines:
    line = line.strip()
    print(line[::-1])

#exercise 4
#refer to read_lynx.py

for i in range(5):
    if i == 2:
        continue
    print(i)

#exercise 5 and 6 refer to read_smallest_skip.py

