"""
-----------
__main__.py
-----------
- Executes file input and output via "process_files" function
- Initializes argument parser for terminal entry of input and output file paths
- Provides exception handling for file IO
"""


import threading
from Lab4 import process
from Lab4.quicksort import *
from Lab4.natural_merge_sort import *
from Lab4.process import *
from Lab4.utility import *
from sys import stderr
import argparse

# Maximize permissible recursion depth
sys.setrecursionlimit(10000)
threading.stack_size(2**15)

############################### Tracking Parameters ####################################################
# This list contains the file access sequence for processing using individual sort algorithms
# and will be sequentially accessed using iteration
file_list = ['ran50', 'rev50', 'asc50', 'dup50', 'ran500', 'rev500', 'asc500', 'dup500',
             'ran1k', 'rev1k', 'asc1k', 'dup1k', 'ran2k', 'rev2k', 'asc2k', 'dup2k',
             'ran3k', 'rev3k', 'asc3k', 'dup3k']

# Disable output messages for stage by stage commentary of analysis - index corresponds to file list index
disable_msgs = [False, False, False, False, True, True, True, True, True, True, True, True,
                True, True, True, True, True, True, True, True]

# Stores partition size cut off for triggering of insertion sort
QS_ins_limit = [0, 50, 100, 0, 0]

# Stores pivot type:
# 1 - First Index position
# 2 - Median of Three
# 3 - Middle index
QS_pivot = [1, 1, 1, 2, 3]
QS_pivot_type = ["First Index", "First Index", "First Index", "Median of Three", "Middle Index"]
############################################################################################################


# Set up arguments for terminal run commands
arg_parser = argparse.ArgumentParser()
# Argument to accept input file path
arg_parser.add_argument("in_dir", type=str, help="Input Directory Pathname")
# Argument to accept output file path
arg_parser.add_argument("out_dir", type=str, help="Output Directory Pathname")
# Argument '--all' (optional) to accept option to produce output report sort result files for all file sizes
# and to output Pandas dataframe summaries
arg_parser.add_argument('-a', '--all', action='store_true', help='Produce output files for all files <= size 3000')

args = arg_parser.parse_args()

in_dir_path = args.in_dir  # Input directory path
out_dir_path = args.out_dir # Output directory path

# Optional args: '--all'
if args.all:  # Run output to process all files
    file_range = len(file_list)
else:  # Only size 50 input files will be processed
    file_range = 4

# Initialize counters to store the number of operations for each sorting algorithm
comp_swap_list = []  # comparison and swap counter list of lists
comb_comp_swap_list = []  # combined total of comparison and swaps counter list
sort_name_list = []  # stores all the names of the sort + file combinations

# Set up standard naming for input files
for i in range(file_range):
    in_file_name = ""
    in_file_name = in_file_name + file_list[i] + "_ccy.dat"
    in_path = Path(in_dir_path + '\\' + in_file_name)

    for j in range(5):
        pivot_select = QS_pivot[j]
        ins_limit_select = QS_ins_limit[j]

        out_file_name = ""
        out_file_name = file_list[i] + "_QS" + str(pivot_select) + "_" + str(ins_limit_select) + "_out.dat"
        out_path = Path(out_dir_path + '\\' + out_file_name)
        sort_name = file_list[i] + "_QS" + str(pivot_select) + "_" + str(ins_limit_select)

        try:
            with in_path.open('r') as input_file, out_path.open('w') as output_file:

                # Incorrect input and output file type exception
                if in_path.suffix != '.dat':
                    print('Error! Incorrect input file type. Supplied file type:', in_path.suffix,
                          ' Required file type: .txt', file=stderr)
                    sys.exit()

                # Empty file exception
                elif in_path.stat().st_size == 0:
                    print("Error! File is empty!", file=stderr)
                    sys.exit()

                # Invalid output directory
                elif Path(out_dir_path).is_dir() is False:
                    print("Invalid output path directory:", out_path, file=stderr)
                    sys.exit()

                # collect Quicksort + file combination names
                sort_name_list.append(sort_name)
                # Read input text files, process into array lists
                num_array = process.process_files(input_file)
                # Output file descriptive Quicksort parameters
                output_file.write("in_path:" + in_dir_path + '/' + in_file_name + "\n")
                output_file.write("out_path:" + out_dir_path + '/' + out_file_name + "\n")
                output_file.write("\n----------------")
                output_file.write("\n<<<QUICKSORT>>>\n")
                output_file.write("----------------\n")
                output_file.write("Quicksort parameters:\n")
                output_file.write("\tInput Type: " + str(file_list[i]) + "\n")
                output_file.write("\tPivot type: " + str(QS_pivot_type[j]) + "\n")
                output_file.write("\tInsertion Sort Size Limit: " + str(QS_ins_limit[j]) + "\n")
                output_file.write("\tNOTE: Scroll down to bottom for results summary\n")
                if QS_ins_limit[j] == 0:
                    output_file.write("\tNOTE: Quick sort only - Insertion sort not activated.\n")
                elif QS_ins_limit[j] == 50 or QS_ins_limit[j] == 100:
                    output_file.write("\nNOTE: Insertion sort activated for partition sizes <=" +
                                      str(QS_ins_limit[j]) + "\n")

                if disable_msgs[i] is False:  # "play by play" output of sort algorithm enabled
                    output_file.write("\nUnsorted Array:" + "\n")
                    num_array_str = " ".join(map(str, num_array))
                    output_file.write(num_array_str + "\n")

                qs_counter = Counter()  # Initialize counter to track Quick Sort comparisons and swaps
                quicksort(num_array, QS_pivot[j], qs_counter, QS_ins_limit[j], output_file,
                                    disable_msgs[i])
                num_array_str = " ".join(map(str, num_array))
                if disable_msgs[i] is False:
                    output_file.write('Sorted Array in Ascending Order:\n' + num_array_str + "\n")

                # Summary of analysis results: comparisons, sorts and total number of steps (comps + sorts)
                output_file.write("\nRESULTS SUMMARY")
                output_file.write("\n+++++++++++++++++++++++++++++")
                output_file.write("\nQUICKSORT on " + str(file_list[i]) + " data:\n")
                output_file.write("Pivot Type: " + str(QS_pivot_type[j]) + "\n")
                output_file.write("Insertion Sort Limit: " + str(QS_ins_limit[j]) + "\n")
                output_file.write("\nNumber of Comparisons:" + str(qs_counter.comparisons) + "\n")
                output_file.write("Number of Swaps:" + str(qs_counter.swaps) + "\n")
                output_file.write("Total number of steps:" + str(qs_counter.comparisons + qs_counter.swaps) + "\n")
                output_file.write("+++++++++++++++++++++++++++++\n")

                # Lists storing the comparisons and swaps from Quick Sort (QS)
                step_list = []  # This will store a pair of a comparison and a swap
                step_list.append(qs_counter.comparisons)
                step_list.append(qs_counter.swaps)
                comp_swap_list.append(step_list)  # comp_swap_list is a list of lists
                comb_comp_swap_list.append(
                    qs_counter.comparisons + qs_counter.swaps)  # Store the sum of comparisons + swaps

        # File path error
        except FileNotFoundError:
            print('Input file does not exist in supplied path: ', in_path, file=stderr)

        # Set up standard naming format for Natural Merge Sort output files
        out_file_name = ""
        out_file_name = file_list[i] + "_NMS" + "_out.dat"
        out_path = Path(out_dir_path + '\\' + out_file_name)
        sort_name = file_list[i] + "_NMS"

    try:
        with in_path.open('r') as input_file, out_path.open('w') as output_file:

            # Incorrect input and output file type exception
            if in_path.suffix != '.dat':
                print('Error! Incorrect input file type. Supplied file type:', in_path.suffix,
                        ' Required file type: .txt', file=stderr)
                sys.exit()

            # Empty file exception
            elif in_path.stat().st_size == 0:
                print("Error! File is empty!", file=stderr)
                sys.exit()

            # Invalid output directory
            elif Path(out_dir_path).is_dir() is False:
                print("Invalid output path directory:", out_path, file=stderr)
                sys.exit()

            # collect Quicksort + file combination names
            sort_name_list.append(sort_name)
            num_array = process.process_files(input_file)  # Process input text file into array list
            num_ll = arrayToList(num_array)  # Convert the array into a numbers linked list
            nms_counter = Counter()  # Counter for Natural Merge Sort (NMS) swaps and comparisons

            ("\n########################\n")
            output_file.write("<<<NATURAL MERGE SORT>>>\n")
            output_file.write("------------------------\n")
            output_file.write("in_path:" + in_dir_path + '/' + in_file_name + "\n")
            output_file.write("out_path:" + out_dir_path + '/' + out_file_name + "\n")
            output_file.write("\nInput Type: " + file_list[i] + "\n")
            output_file.write("NOTE: Scroll down to bottom for results summary\n\n")
            if disable_msgs[i] is False:
                output_file.write("Unsorted list: ")
                output_file.write(" ".join(map(str, print_list(num_ll))) + "\n")

            # Convert the number array into a linked list format for input into Natural Merge Sort
            num_queue = get_num_queue(num_ll, nms_counter, output_file, disable_msgs[i])
            # Obtain the sorted linked list
            sorted = natural_merge_sort(num_queue, nms_counter, output_file, disable_msgs[i])

            if disable_msgs[i] is False:
                # Re-convert sorted linked list into array, then string format for output
                output_file.write(
                    "Sorted list: " + " ".join(map(str, print_list(sorted))) + "\n")

            # Summary of analysis results: comparisons, sorts and total number of steps (comps + sorts)
            output_file.write("\nRESULTS SUMMARY")
            output_file.write("\n+++++++++++++++++++++++++++++++++")
            output_file.write("\nNATURAL MERGE SORT on " + str(file_list[i]) + " data:\n")
            output_file.write("Number of Comparisons:" + str(nms_counter.comparisons) + "\n")
            output_file.write("Number of Swaps:" + str(nms_counter.swaps) + "\n")
            output_file.write("Total number of steps:" + str(nms_counter.comparisons + nms_counter.swaps) + "\n")
            output_file.write("+++++++++++++++++++++++++++++++++\n")

            # Lists storing the comparisons and swaps from Natural Merge Sort (NMS)
            step_list = []  # This will store a pair of a comparison and a swap
            step_list.append(nms_counter.comparisons)
            step_list.append(nms_counter.swaps)
            comp_swap_list.append(step_list)  # comp_swap_list is a list of lists
            comb_comp_swap_list.append(
                nms_counter.comparisons + nms_counter.swaps)  # Store the sum of comparisons + swaps

    # File path error
    except FileNotFoundError:
        print('Input file does not exist in supplied path: ', in_path, file=stderr)

# Optional args: '--all' are required to produce Dataframe summaries
# NOTE: Pandas must be installed for the Dataframes
if args.all:  # All files must be fully processed if dataframes are to be extracted
    file_range = len(file_list)

    # Construct dataframes to summarize result output (comparisons + swaps combined)
    ran_df = make_data_frame('ran_list', comb_comp_swap_list)
    rev_df = make_data_frame('rev_list', comb_comp_swap_list)
    asc_df = make_data_frame('asc_list', comb_comp_swap_list)
    dup_df = make_data_frame('dup_list', comb_comp_swap_list)

    out_path = Path(out_dir_path + '\\z_dataframes_out.dat')

    # Construct dataframe with separate comparisons and swaps
    comp_swap_50_df = extract_comp_swaps(comp_swap_list, sort_name_list, start_index=0, end_index=23)
    comp_swap_500_df = extract_comp_swaps(comp_swap_list, sort_name_list, start_index=24, end_index=47)
    comp_swap_1000_df = extract_comp_swaps(comp_swap_list, sort_name_list, start_index=48, end_index=71)
    comp_swap_2000_df = extract_comp_swaps(comp_swap_list, sort_name_list, start_index=72, end_index=95)
    comp_swap_3000_df = extract_comp_swaps(comp_swap_list, sort_name_list, start_index=96, end_index=119)

    # Write summary of swap and comparison totals to text file
    try:
        with out_path.open('w') as output_file:
            ran_df_str = ran_df.to_string()
            rev_df_str = rev_df.to_string()
            asc_df_str = asc_df.to_string()
            dup_df_str = dup_df.to_string()
            comp_swap_50_df_str = comp_swap_50_df.to_string()
            comp_swap_500_df_str = comp_swap_500_df.to_string()
            comp_swap_1000_df_str = comp_swap_1000_df.to_string()
            comp_swap_2000_df_str = comp_swap_2000_df.to_string()
            comp_swap_3000_df_str = comp_swap_3000_df.to_string()
            output_file.write("Sort results on Random Numbers:\n")
            output_file.write(ran_df_str)
            output_file.write("\n\nSort results on Reverse Sorted Numbers:\n")
            output_file.write(rev_df_str)
            output_file.write("\n\nSort results on Ascending Sorted Numbers:\n")
            output_file.write(asc_df_str)
            output_file.write("\n\nSort results on Random Numbers with 20% duplicates:\n")
            output_file.write(dup_df_str)
            output_file.write("\n\n Comparisons and swaps on size 50 files:\n")
            output_file.write(comp_swap_50_df_str)
            output_file.write("\n\n Comparisons and swaps on size 500 files:\n")
            output_file.write(comp_swap_500_df_str)
            output_file.write("\n\n Comparisons and swaps on size 1000 files:\n")
            output_file.write(comp_swap_1000_df_str)
            output_file.write("\n\n Comparisons and swaps on size 2000 files:\n")
            output_file.write(comp_swap_2000_df_str)
            output_file.write("\n\n Comparisons and swaps on size 3000 files:\n")
            output_file.write(comp_swap_3000_df_str)

    # File path error
    except FileNotFoundError:
        print('Supplied output path does not exist: ', out_path, file=stderr)


