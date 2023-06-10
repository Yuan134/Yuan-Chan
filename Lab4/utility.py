"""
-------
utility.py
-------
This module processes a list of Count class objects holding the comparison and sort counts after the sorting
algorithms have been run and extracts the counts to be presented in a Pandas dataframe
"""
import pandas as pd
import sys

def make_data_frame(data_type, comb_list):
    """
    Constructs a data frame from a list containing the total count of comparisons and swaps
    :param data_type: whether data is random("ran"), reversed("rev"), ascending("asc") or with 20% duplicates ("dup")
    :param comb_list: List containing the total count of comparisons and swaps per file size and sort
    :return: Dataframe containing the total number of steps (comparisons + swaps) for stated file type / sort type
    """

    # These are the lists that will be used to match the count output contained in comb_list
    ran_list = ['ran_QS1_0', 'ran_QS1_50', 'ran_QS1_100', 'ran_QS2_0', 'ran_QS3_0', 'ran_NMS']
    rev_list = ['rev_QS1_0', 'rev_QS1_50', 'rev_QS1_100', 'rev_QS2_0', 'rev_QS3_0', 'rev_NMS']
    asc_list = ['asc_QS1_0', 'asc_QS1_50', 'asc_QS1_100', 'asc_QS2_0', 'asc_QS3_0', 'asc_NMS']
    dup_list = ['dup_QS1_0', 'dup_QS1_50', 'dup_QS1_100', 'dup_QS2_0', 'dup_QS3_0', 'dup_NMS']

    # Extract the counts from comb_list and transfer to the corresponding sub-lists
    if data_type == 'ran_list':
        sort_name_list = ran_list
        size50 = comb_list[0:6]
        size500 = comb_list[24:30]
        size1k = comb_list[48:54]
        size2k = comb_list[72:78]
        size3k = comb_list[96:112]
    elif data_type == 'rev_list':
        sort_name_list = rev_list
        size50 = comb_list[6:12]
        size500 = comb_list[30:36]
        size1k = comb_list[54:60]
        size2k = comb_list[78:84]
        size3k = comb_list[112:118]
    elif data_type == 'asc_list':
        sort_name_list = asc_list
        size50 = comb_list[12:18]
        size500 = comb_list[36:42]
        size1k = comb_list[60:66]
        size2k = comb_list[84:90]
        size3k = comb_list[108:114]
    elif data_type == 'dup_list':
        sort_name_list = dup_list
        size50 = comb_list[18:24]
        size500 = comb_list[42:48]
        size1k = comb_list[66:72]
        size2k = comb_list[90:96]
        size3k = comb_list[114:120]
    else:
        print("Unknown / Incorrect file type!")
        sys.exit(1)

    # Make dictionary of lists of various sort run sizes
    input_dict = {'50': size50, '500': size500, '1000': size1k, '2000': size2k, '3000': size3k}

    df = pd.DataFrame(input_dict, index=sort_name_list)

    return df

def extract_comp_swaps(comp_swap_list, sort_name_list, start_index, end_index):
    """
    Accepts a list of lists containing the comparison and sort counts separately. Extracts the results into individual
    lists so that these can be combined into dataframe format.
    :param comp_swap_list: list of lists containing separate comparison and swap counts
    :param sort_name_list: this is the list containing each of the sorts that were configured to produce the counts
    :param start_index: start index to extract list count contents
    :param end_index: end index to extract list count contents
    :return: Dataframe containing the separate number of steps (comparisons or swaps) for stated file type / sort type
    """
    # Lists to store count results of comparisons and swaps
    comp_swap_list_comparisons = []
    comp_swap_list_swaps = []

    if start_index < 0 or end_index > len(comp_swap_list)-1:
        print("Error! Invalid indexing! Enter non-negative integer less than length of list")
        sys.exit()

    sort_name_list = sort_name_list[start_index:end_index+1]

    for i in range(start_index, end_index+1):
        comp_swap_list_comparisons.append(comp_swap_list[i][0])
        comp_swap_list_swaps.append(comp_swap_list[i][1])

    df = pd.DataFrame(list(zip(comp_swap_list_comparisons, comp_swap_list_swaps)),
                      columns=['Compare', 'Swaps'], index=sort_name_list)

    return df
