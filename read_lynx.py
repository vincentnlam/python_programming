from typing import TextIO
from io import StringIO
import time_series

def find_largest(line: str) -> int:
    """Return the largest value in line, which is a whitespace-delimited string
    of integers that each end with a '.'.

    >>> find_largest('1. 3. 2. 5. 2.')
    5
    """
    # The largest value seen so far.
    largest = -1
    for value in line.split():
        # Remove the trailing period.
        v = int(value[:-1])
        # If we find a larger value, remember it.
        if v > largest:
            largest = v

    return largest

def process_file(reader: TextIO) -> int:
    """Read and process reader, which must start with a time_series header.
    Return the largest value after the header.  There may be multiple pieces
    of data on each line.

    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """

    line = time_series.skip_header(reader).strip()
    # The largest value so far is the largest on this first line of data.
    largest = find_largest(line)

    # Check the rest of the lines for larger values.
    for line in reader:
        print(line)
        print("-" * 5)
        large = find_largest(line)
        print(large)
        print("=" * 10)
        if large > largest:
            largest = large
    return largest

def process_file2(reader: TextIO) -> int:
    """Read and process reader, which must start with a time_series header.
    Return the largest value after the header.  There may be multiple pieces
    of data on each line.

    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """

    lines = reader.readlines()

    lines = lines[1:]


    largest = 0
    for line in lines:
        if line.startswith("#"):
            continue
        # print(line)
        # print("-" * 5)
        large = find_largest(line)
        # print(large)
        # print("=" * 10)
        if large > largest:
            largest = large
    return largest



if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file:
        print("The Largest Number is:")
        print(process_file2(input_file))
