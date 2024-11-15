import time
import random
def linear_search(L, num):
    for i in range(len(L)):
        # print(L[i])
        if L[i] == num:
            return True
    return False

my_list = [3, 5, 8, 0, 1, 2, 6, 9, 5, 7,]
my_list = list(range(1, 5000))
# print(my_list)
print("linear search")
t1 = time.perf_counter()
print(linear_search(my_list, 450000))
t2 = time.perf_counter()
print(f'The code took {(t2 - t1)* 1000}')
print("-"*20)
def binary_search(L, v):
# Mark the left and right indices of the unknown section.
    i = 0
    j = len(L) - 1
    while i != j + 1:
        m = (i + j) // 2
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1
    if 0 <= i < len(L) and L[i] == v:
        return i
    else:
        return -1

my_list = list(range(1, 5000))
print("binary search")
t1 = time.perf_counter()
print(binary_search(my_list, 450000))
t2 = time.perf_counter()
print(f'The code took {(t2 - t1)* 1000}')
print("-"*20)

def find_largest(n, L):
    copy = sorted(L)
    return copy[-n:]

L = [2, 0, 5, 8, 1]
print(find_largest(4, my_list))
def find_min(L: list, b: int) -> int:
    smallest = b # The index of the smallest so far.
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            smallest = i
        i = i + 1
    return smallest
def selection_sort(L):
    i = 0
    while i != len(L):
        # print(L[i])
        smallest = find_min(L, i) 
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1

my_list = list(range(1, 5000))
print("selection sort")
t1 = time.perf_counter()
print(selection_sort(my_list))
t2 = time.perf_counter()
print(f'The code took {(t2 - t1)* 1000}')
print("-"*20)

my_list = list(range(1, 5000))
print("sorted")
t1 = time.perf_counter()
sorted(my_list)
t2 = time.perf_counter()
print(f'The code took {(t2 - t1)* 1000}')
print("-"*20)

def insertion_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    i = 0
    while i != len(L):
        # Insert L[i] where it belongs in L[0:i+1].
        insert(L, i)
        i = i + 1   
        
        
def insert(L: list, b: int) -> None:
    """Precondition: L[0:b] is already sorted.
    Insert L[b] where it belongs in L[0:b + 1].
    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    >>> insert(L, 4)
    >>> L
    [-1, 2, 3, 4, 7, 5]
    """
    # Find where to insert L[b] by searching backwards from L[b]
    # for a smaller item.
    i = b
    while i != 0 and L[i - 1] >= L[b]:
        i = i - 1
    # Move L[b] to index i, shifting the following values to the right.
    value = L[b]
    del L[b]
    L.insert(i, value)
    
my_list = list(range(1, 5000))
print("insertion sort")
t1 = time.perf_counter()
print(insertion_sort(my_list))
t2 = time.perf_counter()
print(f'The code took {(t2 - t1)* 1000}')
print("-"*20)

def merge(L1: list, L2: list) -> list:
    """Merge sorted lists L1 and L2 into a new list and return that new list.
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """
    newL = []
    i1 = 0
    i2 = 0
    # For each pair of items L1[i1] and L2[i2], copy the smaller into newL.
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1
    # Gather any leftover items from the two sections.
    # Note that one of them will be empty because of the loop condition.
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL

def mergesort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    # Make a list of 1-item lists so that we can start merging.
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])
    # The next two lists to merge are workspace[i] and workspace[i + 1].
    i = 0
    # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2
    # Copy the result back into L.
    if len(workspace) != 0:
        L[:] = workspace[-1][:]

def built_in(L: list) -> None:
    """Call list.sort --- we need our own function to do this so that we can
    treat it as we treat our own sorts.
    """
    L.sort()
def print_times(L: list) -> None:
    """Print the number of milliseconds it takes for selection sort, insertion
    sort, and list.sort to run.
    """
    print(len(L), end='\t')
    for func in (selection_sort, insertion_sort, mergesort, built_in):
        if func in (selection_sort, insertion_sort) and len(L) > 10000:
            continue
        L_copy = L[:]
        t1 = time.perf_counter()
        func(L_copy)
        t2 = time.perf_counter()
        print("{0:7.1f}".format((t2 - t1) * 1000.), end='\t')
    print() # Print a newline.
print("List Length\tselectionsort\tinsertionsort\tmergesort\tlist.sort")
for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]:
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)