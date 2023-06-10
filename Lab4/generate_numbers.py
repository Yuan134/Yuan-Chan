"""
-------
generate_numbers.py
-------
This is a STANDALONE script to generate a series of numbers sequenced to either random, reversed, ascending or random
with duplication.
"""

import random
import os

def generate_nums(size_numbers, num_type, duplicate_percent=None):
    """
    Generates a sequence of numbers according to the desired configuration of random, reversed, ascending or random
    with duplication.
    :param size_numbers:
    :param num_type:
    :param duplicate_percent:
    :return:
    """
    # Type1: random - no duplicates
    # Type2: sorted in reverse order
    # Type3: sorted in ascending order
    # Type4: random - with duplicates

    final_num_list = []

    if num_type == 1:
        # Generate list of unique random integers
        num_list = random.sample(range(size_numbers + 1), size_numbers)
        random.shuffle(num_list)
        final_num_list.extend(num_list)

    elif num_type == 2:

        # Loop through integers
        for i in range(size_numbers + 1):
            final_num_list.append(i)

        final_num_list.reverse()

    elif num_type == 3:
        # Loop through integers
        for i in range(size_numbers + 1):
            final_num_list.append(i)

    elif num_type == 4:
        duplicates = int(round((duplicate_percent / 100) * size_numbers, 0))
        non_duplicates = size_numbers - duplicates

        # Generate list of unique random integers
        num_list = random.sample(range(size_numbers+1), non_duplicates)
        random.shuffle(num_list)

        dupl_nums = random.choices(num_list, k=duplicates)

        num_list.extend(dupl_nums)

        random.shuffle(num_list)
        final_num_list = num_list


    # write to output file
    filename = ""

    if num_type == 1:
        if size_numbers >= 1000:
            filename = "ran" + str(int(size_numbers / 1000)) + "k_ccy.dat"

        else:
            filename = "ran" + str(size_numbers) + "_ccy.dat"

    elif num_type == 2:
        if size_numbers >= 1000:
            filename = "rev" + str(int(size_numbers / 1000)) + "k_ccy.dat"

        else:
            filename = "rev" + str(size_numbers) + "_ccy.dat"

    elif num_type == 3:
        if size_numbers >= 1000:
            filename = "asc" + str(int(size_numbers / 1000)) + "k_ccy.dat"

        else:
            filename = "asc" + str(size_numbers) + "_ccy.dat"

    elif num_type == 4:

        if size_numbers >= 1000:
            filename = "dup" + str(int(size_numbers / 1000)) + "k_ccy.dat"

        else:
            filename = "dup" + str(size_numbers) + "_ccy.dat"

    file_path = 'C:\\Users\\yuanc\\PycharmProjects\\JHU\\Lab4\\resources\\'
    file_path += filename
    print("filepath:", file_path)

    with open(file_path, 'w') as file:
        for i in range(size_numbers):
            number = str(final_num_list[i])
            file.writelines(number+'\n')

    final_num_list = []

# driver code

# Generate size 50 files
generate_nums(50, 1, duplicate_percent=None)
generate_nums(50, 2, duplicate_percent=None)
generate_nums(50, 3, duplicate_percent=None)
generate_nums(50, 4, duplicate_percent=20)

# Generate size 500 files
generate_nums(500, 1, duplicate_percent=None)
generate_nums(500, 2, duplicate_percent=None)
generate_nums(500, 3, duplicate_percent=None)
generate_nums(500, 4, duplicate_percent=20)

# Generate size 1000 files
generate_nums(1000, 1, duplicate_percent=None)
generate_nums(1000, 2, duplicate_percent=None)
generate_nums(1000, 3, duplicate_percent=None)
generate_nums(1000, 4, duplicate_percent=20)

# Generate size 2000 files
generate_nums(2000, 1, duplicate_percent=None)
generate_nums(2000, 2, duplicate_percent=None)
generate_nums(2000, 3, duplicate_percent=None)
generate_nums(2000, 4, duplicate_percent=20)

# Generate size 5000 files
generate_nums(5000, 1, duplicate_percent=None)
generate_nums(5000, 2, duplicate_percent=None)
generate_nums(5000, 3, duplicate_percent=None)
generate_nums(5000, 4, duplicate_percent=20)

# Generate size 10000 files
generate_nums(10000, 1, duplicate_percent=None)
generate_nums(10000, 2, duplicate_percent=None)
generate_nums(10000, 3, duplicate_percent=None)
generate_nums(10000, 4, duplicate_percent=20)

# Generate size 20000 files
generate_nums(20000, 1, duplicate_percent=None)
generate_nums(20000, 2, duplicate_percent=None)
generate_nums(20000, 3, duplicate_percent=None)
generate_nums(20000, 4, duplicate_percent=20)