# Current Author: Lucas A. Ravkov
# Version: March 2020
# Contact: Lravkov@gmail.com

import pandas as pd
# import time


# Function to convert list to string separated by spaces
def list_to_string(s):
    # initialize an empty string and a counter so that you don't add an extra space at the end
    str1 = ""
    counter = 0

    # traverse in the string
    for ele in s:
        counter += 1
        str1 += str(ele)
        if counter < len(s):  # add spaces between all strings and make sure to not add one after last entry
            str1 += ' '

        # return string
    return str1


# Function to convert name list to name string separated by the correct delimiting
def name_list_to_string(s):
    # initialize an empty string
    str1 = ""
    counter = 0

    # traverse in the string
    for ele in s:
        counter += 1
        str1 += str(ele)
        if counter == 1 or 2 or 3 or 4:
            str1 += '\t'
        if counter == 5:
            # str1 += '\t'
            str1 += ' '
    # return string
    return str1


def get_filename(spectra_p, data_temp_p, first_file_p, num_peaks_p):
    if spectra_p == first_file_p:
        # print('--------------')  # determining file name information for the fixed file that will be produced later on
        file_name_list_p = str(data_temp_p.iloc[0, :]).split()
        file_name_needed_p_list_p = [file_name_list_p[0], file_name_list_p[1]]
        file_name_needed_p = list_to_string(file_name_needed_p_list_p)
        # print(file_name_needed_p)
        # print('--------------')
        return file_name_needed_p
    elif first_file_p == 1:
        # print('--------------')  # determining file name information for the fixed file that will be produced later on
        position_p = 0 + ((spectra_p - 1) * (num_peaks_p + 2)) - 1
        # position_p = 0 + ((spectra_p - first_file_p - 1) * (num_peaks_p + 2)) - first_file_p - 1
        # print(position_p)
        file_name_list_p = str(data_temp_p.iloc[position_p, :]).split()
        file_name_needed_p_list_p = [file_name_list_p[4], file_name_list_p[5]]
        file_name_needed_p = list_to_string(file_name_needed_p_list_p)
        file_name_needed_p = file_name_needed_p[1:]  # removing first character
        file_name_needed_p = file_name_needed_p[:-1]  # removing last character
        # print(file_name_needed_p)
        # print('--------------')
        return file_name_needed_p
    else:
        # print('--------------')  # determining file name information for the fixed file that will be produced later on
        position_p = 0 + ((spectra_p - first_file_p) * (num_peaks_p + 2)) - 1
        # position_p = 0 + ((spectra_p - first_file_p - 1) * (num_peaks_p + 2)) - first_file_p - 1
        # print(position_p)
        file_name_list_p = str(data_temp_p.iloc[position_p, :]).split()
        file_name_needed_p_list_p = [file_name_list_p[4], file_name_list_p[5]]
        file_name_needed_p = list_to_string(file_name_needed_p_list_p)
        file_name_needed_p = file_name_needed_p[1:]  # removing first character
        file_name_needed_p = file_name_needed_p[:-1]  # removing last character
        # print(file_name_needed_p)
        # print('--------------')
        return file_name_needed_p


def get_dataframe(data_temp_p, spectra_p, num_peaks_p, first_file_p):
    # data_p = data_temp_p[(1 + ((spectra_p - 1) * (num_peaks_p + 2))):(num_peaks_p + 1 + ((spectra_p - 1) * (num_peaks_p + 2)))]
    data_p = data_temp_p[(1 + ((spectra_p - first_file_p) * (num_peaks_p + 2))):(num_peaks_p + 1 + ((spectra_p - first_file_p) * (num_peaks_p + 2)))]

    data_array_p = []

    # print('data_p')
    # print(data_p)

    # MIGHT NEED TO USE:  for i_p in range(num_peaks_p - 1):
    for i_p in range(num_peaks_p):
        # separate the dataBlock (dataS1) into the constituent sections, iloc[i ,0] is used where x is the row you want
        data_str_p = data_p.iloc[i_p, 0]
        data_str_p = str(data_str_p)
        param_list_p_p = data_str_p.split()
        for j_p in range(len(param_list_p_p)):
            if param_list_p_p[j_p] == '+/-':
                param_list_p_p[j_p] = param_list_p_p[j_p]
            elif param_list_p_p[j_p] == '?':
                param_list_p_p[j_p] = param_list_p_p[j_p]
            else:
                param_list_p_p[j_p] = float(param_list_p_p[j_p])
        data_array_p.append(param_list_p_p)
    data_fr_p = pd.DataFrame(data_array_p)

    # print('data_fr_p')
    # print(data_fr_p)

    return data_fr_p, data_p


def generate_init_bool_and_data_arrays(data_fr_p):
    h1_array = data_fr_p.iloc[:, 6]  # hwhm1 array
    h2_array = data_fr_p.iloc[:, 9]  # hwhm2 array

    h1_array_bool = []
    h2_array_bool = []

    s1_array = data_fr_p.iloc[:, 12]  # shape1 array
    s2_array = data_fr_p.iloc[:, 15]  # shape2 array

    s1_array_bool = []
    s2_array_bool = []

    return h1_array, h2_array, h1_array_bool, h2_array_bool, s1_array, s2_array, s1_array_bool, s2_array_bool


def generate_init_bool_and_data_arrays_poly(data_fr_p, num_peaks_p):
    h1_array = data_fr_p.iloc[:-1, 6]  # hwhm1 array
    h2_array = data_fr_p.iloc[:-1, 9]  # hwhm2 array

    h1_array_bool = []
    h2_array_bool = []

    s1_array = data_fr_p.iloc[:-1, 12]  # shape1 array
    s2_array = data_fr_p.iloc[:-1, 15]  # shape2 array

    s1_array_bool = []
    s2_array_bool = []

    polynomial_data = data_fr_p.iloc[num_peaks_p - 1, :]
    # print(polynomial_data)

    return h1_array, h2_array, h1_array_bool, h2_array_bool, s1_array, s2_array, s1_array_bool, s2_array_bool


def generate_init_bool_and_data_arrays_poly2(data_fr_p, include_p6_p):
    if not include_p6_p:
        h1_array = data_fr_p.iloc[:, 6]  # hwhm1 array
        h2_array = data_fr_p.iloc[:, 9]  # hwhm2 array

        h1_array_bool = []
        h2_array_bool = []

        s1_array = data_fr_p.iloc[:, 12]  # shape1 array
        s2_array = data_fr_p.iloc[:, 15]  # shape2 array

        s1_array_bool = []
        s2_array_bool = []

    if include_p6_p:
        h1_array = data_fr_p.iloc[:-1, 6]  # hwhm1 array
        h2_array = data_fr_p.iloc[:-1, 9]  # hwhm2 array

        h1_array_bool = []
        h2_array_bool = []

        s1_array = data_fr_p.iloc[:-1, 12]  # shape1 array
        s2_array = data_fr_p.iloc[:-1, 15]  # shape2 array

        s1_array_bool = []
        s2_array_bool = []

        # polynomial_data = data_fr_p.iloc[num_peaks_p - 1, :]
        # print(polynomial_data)

    return h1_array, h2_array, h1_array_bool, h2_array_bool, s1_array, s2_array, s1_array_bool, s2_array_bool


def fix_shape_values(s_array_p, s_array_bool_p, pretext_filename_p):

    with open(pretext_filename_p, "r") as file:
        first_line_p = file.readline()
        for last_line_p in file:
            pass
    # print(last_line_p)
    peak_types_string_p = last_line_p

    peak_type_p = '0'  # default peak type is SplitPearson7
    peak_types_list_p = peak_types_string_p.split(', ')
    # print(peak_types_list_p)

    for i_p in range(len(s_array_p)):
        peak_type_temp_list_p = peak_types_list_p[i_p].split('\n')

        if peak_type_temp_list_p[0] == '0':
            # print('SplitPearson7')
            peak_type_p = '0'
        elif peak_type_temp_list_p[0] == '1':
            # print('SplitPseudoVoigt')
            peak_type_p = '1'
        else:
            # print(peak_type_temp_list_p[0])
            print('Invalid Peak Type.')

        # print(s_array_p.iloc[i_p]
        if peak_type_p == '0':  # this is for SplitPearson7
            if s_array_p.iloc[i_p] <= 1:  # check if the leftShape value is less than 1 (unphysical)
                s_array_p.iloc[i_p] = 1  # set the value to 1 (cauchy) if above true
                s_array_bool_p.append(1)  # indicates value has been locked to 1
            elif s_array_p.iloc[i_p] >= 100:  # check if the leftShape value is greater than 100
                s_array_p.iloc[i_p] = 100  # cap value at 100 (pseudo gaussian)
                s_array_bool_p.append(1)  # indicates values has been locked to 100
            else:
                s_array_bool_p.append(0)  # indicates value is not locked
        elif peak_type_p == '1':  # this is for SplitPseudoVoigt
            if s_array_p.iloc[i_p] <= 0.0:  # check if the leftShape value is less than 0 (unphysical)
                s_array_p.iloc[i_p] = 0  # set the value to 0 (100% gaussian) if above true
                s_array_bool_p.append(1)  # indicates value has been locked to 1
            elif s_array_p.iloc[i_p] >= 1.0:  # check if the leftShape value is greater than 1
                s_array_p.iloc[i_p] = 1  # cap value at 1 (100% lorentzian)
                s_array_bool_p.append(1)  # indicates values has been locked to 100
            else:
                s_array_bool_p.append(0)  # indicates value is not locked

    s_array_bool_str_p = list_to_string(s_array_bool_p)
    return s_array_p, s_array_bool_str_p, s_array_bool_p


def fix_width_values(h1_array_p, h1_array_bool_p, h2_array_p, h2_array_bool_p):
    for i in range(len(h1_array_p)):
        if h1_array_p.iloc[i] <= 0 and h2_array_p.iloc[i] <= 0:  # if both are -ve, set them to a small +ve value
            h1_array_p.iloc[i] = 0.001
            h2_array_p.iloc[i] = 0.001
            h1_array_bool_p.append(0)  # CHANGE TO 1 IF ABOVE UNCOMMENTED
            h2_array_bool_p.append(0)
        elif h1_array_p.iloc[i] <= 0:  # if the left HWHM is -ve
            h1_array_p.iloc[i] = h2_array_p.iloc[i]  # set them equal
            h1_array_bool_p.append(0)  # CHANGE TO 1 IF ABOVE UNCOMMENTED
            h2_array_bool_p.append(0)
        elif h2_array_p.iloc[i] <= 0:  # check the vise versa
            h2_array_p.iloc[i] = h1_array_p.iloc[i]  # set them equal
            h1_array_bool_p.append(0)  # CHANGE TO 1 IF ABOVE UNCOMMENTED
            h2_array_bool_p.append(0)
        else:
            h1_array_bool_p.append(0)
            h2_array_bool_p.append(0)

    h1_array_bool_str_p = list_to_string(h1_array_bool_p)
    h2_array_bool_str_p = list_to_string(h2_array_bool_p)
    return h1_array_p, h1_array_bool_str_p, h1_array_bool_p, h2_array_p, h2_array_bool_str_p, h2_array_bool_p


def generate_spectra_name(filename_prefix_p, spectra_p):
    spectra_name_p = filename_prefix_p + ' ' + str(spectra_p).zfill(6)
    return spectra_name_p


def write_boolean_table_to_file(bool_filename_p, h1_array_bool_str_p, h2_array_bool_str_p, s1_array_bool_str_p, s2_array_bool_str_p, filename_prefix_p, spectra_p):
    spectra_name_p = generate_spectra_name(filename_prefix_p, spectra_p)
    with open(bool_filename_p, 'a') as the_file_p:
        the_file_p.write('boolean_table' + ' ' + spectra_name_p + '\n')  # -------------------------- SHOULD WRITE THE SPECTRA NAME FOR EACH TABLE
        the_file_p.write(h1_array_bool_str_p + '\n')
        the_file_p.write(h2_array_bool_str_p + '\n')
        the_file_p.write(s1_array_bool_str_p + '\n')
        the_file_p.write(s2_array_bool_str_p + '\n')


def write_fixed_peaks_to_file(fixed_filename_p, file_name_needed_p, num_peaks_p, data_fr_p, h1_array_p, h1_array_bool_p, h2_array_p, h2_array_bool_p, s1_array_p, s2_array_p):
    with open(fixed_filename_p, 'a') as the_file_p:
        the_file_p.write(file_name_needed_p + '\n')
        the_file_p.write('# PeakType	Center	Height	Area	FWHM	parameters...\n')

    for i_p in range(num_peaks_p):
        # separate the dataBlock (dataS1) into the constituent sections, iloc[i ,0] is used where x is the row you want
        data_name_p = data_fr_p.iloc[i_p, :].name[:]  # this is the left half (peak information)
        data_str_p = data_fr_p.iloc[i_p, 0]  # this is the right half (parameter information)
        data_str_p = str(data_str_p)
        param_list_p = data_str_p.split()

        for j_p in range(len(param_list_p)):
            if param_list_p[j_p] == '+/-':
                param_list_p[j_p] = param_list_p[j_p]
            elif param_list_p[j_p] == '?':
                param_list_p[j_p] = param_list_p[j_p]
            else:
                param_list_p[j_p] = float(param_list_p[j_p])
                if j_p == 6:
                    if h1_array_bool_p[i_p] == 1:
                        param_list_p[j_p] = h1_array_p.iloc[i_p]  # set the value in the paramlist for leftWidth to the Fixed value
                        param_list_p[j_p + 2] = '?'
                    elif h1_array_bool_p[i_p] == 0:
                        param_list_p[j_p] = h1_array_p.iloc[i_p]  # set the value in the paramlist for leftWidth to the Fixed value
                        param_list_p[j_p + 2] = '?'
                if j_p == 9:
                    if h2_array_bool_p[i_p] == 1:
                        param_list_p[j_p] = h2_array_p.iloc[i_p]  # set the value in the paramlist for leftWidth to the Fixed value
                        param_list_p[j_p + 2] = '?'
                    elif h2_array_bool_p[i_p] == 0:
                        param_list_p[j_p] = h2_array_p.iloc[i_p] # set the value in the paramlist for leftWidth to the Fixed value
                        param_list_p[j_p + 2] = '?'
                if j_p == 12:
                    param_list_p[j_p] = s1_array_p.iloc[i_p] # set the value in the paramlist for leftShape to the Fixed value
                    param_list_p[j_p + 2] = '?'
                if j_p == 15:
                    param_list_p[j_p] = s2_array_p.iloc[i_p] # set the value in the paramlist for the rightShape to the fixed value
                    param_list_p[j_p + 2] = '?'

        data_name_str_g_p = name_list_to_string(data_name_p)
        param_list_str_p = list_to_string(param_list_p)
        row_data_p = [data_name_str_g_p, param_list_str_p]
        row_str_p = list_to_string(row_data_p)

        with open(fixed_filename_p, 'a') as the_file_p:
            the_file_p.write(row_str_p + '\n')

    # ------------------------------------------ done putting the arrays back together and printing new file --------

    # inserting empty line after each entry
    with open(fixed_filename_p, 'a') as the_file_p:
        _ = the_file_p.write('\n')
    # done inserting empty line, sleep so that everything has time to write and close
    # time.sleep(0.0001)


def write_fixed_peaks_to_file_poly(fixed_filename_p, file_name_needed_p, num_peaks_p, data_fr_p, h1_array_p, h1_array_bool_p, h2_array_p, h2_array_bool_p, s1_array_p, s2_array_p, include_p6_p):
    # with open(fixed_filename_p, 'a') as the_file_p:
    #     the_file_p.write(file_name_needed_p + '\n')
    #     the_file_p.write('# PeakType	Center	Height	Area	FWHM	parameters...\n')

    if include_p6_p:
        with open(fixed_filename_p, 'a') as the_file_p:
            the_file_p.write(file_name_needed_p + '\n')
            the_file_p.write('# PeakType	Center	Height	Area	FWHM	parameters...\n')
        for i_p in range(num_peaks_p):
            if i_p < num_peaks_p - 1:
                # separate the dataBlock (dataS1) into the constituent sections, iloc[i ,0] is used where x is the row you want
                data_name_p = data_fr_p.iloc[i_p, :].name[:]  # this is the left half (peak information)
                data_str_p = data_fr_p.iloc[i_p, 0]  # this is the right half (parameter information)
                data_str_p = str(data_str_p)
                param_list_p = data_str_p.split()

                for j_p in range(len(param_list_p)):
                    if param_list_p[j_p] == '+/-':
                        param_list_p[j_p] = param_list_p[j_p]
                    elif param_list_p[j_p] == '?':
                        param_list_p[j_p] = param_list_p[j_p]
                    else:
                        param_list_p[j_p] = float(param_list_p[j_p])
                        if j_p == 6:
                            if h1_array_bool_p[i_p] == 1:
                                param_list_p[j_p] = h1_array_p.iloc[i_p]  # set the value in the paramlist for leftWidth to the Fixed value
                                param_list_p[j_p + 2] = '?'
                            elif h1_array_bool_p[i_p] == 0:
                                param_list_p[j_p] = h1_array_p.iloc[i_p]  # set the value in the paramlist for leftWidth to the Fixed value
                                param_list_p[j_p + 2] = '?'
                        if j_p == 9:
                            if h2_array_bool_p[i_p] == 1:
                                param_list_p[j_p] = h2_array_p.iloc[i_p]  # set the value in the paramlist for leftWidth to the Fixed value
                                param_list_p[j_p + 2] = '?'
                            elif h2_array_bool_p[i_p] == 0:
                                param_list_p[j_p] = h2_array_p.iloc[i_p] # set the value in the paramlist for leftWidth to the Fixed value
                                param_list_p[j_p + 2] = '?'
                        if j_p == 12:
                            param_list_p[j_p] = s1_array_p.iloc[i_p] # set the value in the paramlist for leftShape to the Fixed value
                            param_list_p[j_p + 2] = '?'
                        if j_p == 15:
                            param_list_p[j_p] = s2_array_p.iloc[i_p] # set the value in the paramlist for the rightShape to the fixed value
                            param_list_p[j_p + 2] = '?'

                data_name_str_g_p = name_list_to_string(data_name_p)
                param_list_str_p = list_to_string(param_list_p)
                row_data_p = [data_name_str_g_p, param_list_str_p]
                row_str_p = list_to_string(row_data_p)

                with open(fixed_filename_p, 'a') as the_file_p:
                    _ = the_file_p.write(row_str_p + '\n')

            elif i_p == num_peaks_p - 1:
                data_name_p = data_fr_p.iloc[i_p, :].name[:]  # this is the left half (peak information)
                data_name_str_g_p = name_list_to_string(data_name_p)
                data_str_p = data_fr_p.iloc[i_p, 0]  # this is the right half (parameter information)
                data_str_p = str(data_str_p)
                row_data_p = [data_name_str_g_p, data_str_p]
                row_str_p = list_to_string(row_data_p)
                # print(row_str_p)
                with open(fixed_filename_p, 'a') as the_file_p:
                    _ = the_file_p.write(row_str_p + '\n')
        # inserting empty line after each entry
        with open(fixed_filename_p, 'a') as the_file_p:
            _ = the_file_p.write('\n')
            # done inserting empty line, sleep so that everything has time to write and close
    elif not include_p6_p:
        write_fixed_peaks_to_file(fixed_filename_p, file_name_needed_p, num_peaks_p, data_fr_p, h1_array_p,
                                  h1_array_bool_p, h2_array_p, h2_array_bool_p, s1_array_p, s2_array_p)


def identify_and_fix_values(data_filename_p, fixed_filename_p, bool_filename_p, first_file_p, number_of_spectra_p, pretext_filename_p, filename_prefix_p, include_p6_p):

    data_temp_p = pd.read_csv(data_filename_p, sep="\t")
    num_peaks_p = int(pd.read_csv(pretext_filename_p, sep='\t').iloc[3, 0])

    # for spectra in range(first_file, (last_file + 1)):
    for spectra_p in range(first_file_p, (number_of_spectra_p + first_file_p)):
        # generate name for each spectra from the original file
        file_name_needed_p = get_filename(spectra_p, data_temp_p, first_file_p, num_peaks_p)

        # get the dataframe
        data_fr_p, data_s1_p = get_dataframe(data_temp_p, spectra_p, num_peaks_p, first_file_p)

        # print("data_fr_p:")
        # print(data_fr_p)

        # generate initial bool and data arrays
        # h1_array_p, h2_array_p, h1_array_bool_p, h2_array_bool_p, s1_array_p, s2_array_p, s1_array_bool_p, s2_array_bool_p = generate_init_bool_and_data_arrays_poly(data_fr_p, num_peaks_p)
        h1_array_p, h2_array_p, h1_array_bool_p, h2_array_bool_p, s1_array_p, s2_array_p, s1_array_bool_p, s2_array_bool_p = generate_init_bool_and_data_arrays_poly2(data_fr_p, include_p6_p)

        # FIX LEFTSHAPE VALUES TO REALISTIC NUMBERS
        s1_array_p, s1_array_bool_str_p, s1_array_bool_p = fix_shape_values(s1_array_p, s1_array_bool_p, pretext_filename_p)

        # FIX RIGHTSHAPE VALUES TO REALISTIC NUMBERS
        s2_array_p, s2_array_bool_str_p, s2_array_bool_p = fix_shape_values(s2_array_p, s2_array_bool_p, pretext_filename_p)

        # CHECK THE WIDTH VALUES (WE DON'T ACTUALLY CHANGE ANYTHING HERE)
        h1_array_p, h1_array_bool_str_p, h1_array_bool_p, h2_array_p, h2_array_bool_str_p, h2_array_bool_p = fix_width_values(h1_array_p,
                                                                                                      h1_array_bool_p,
                                                                                                      h2_array_p,
                                                                                                      h2_array_bool_p)

        # create the boolean file so that we can lock in values
        write_boolean_table_to_file(bool_filename_p, h1_array_bool_str_p, h2_array_bool_str_p, s1_array_bool_str_p, s2_array_bool_str_p, filename_prefix_p, spectra_p)

        write_fixed_peaks_to_file_poly(fixed_filename_p, file_name_needed_p, num_peaks_p, data_s1_p, h1_array_p, h1_array_bool_p,
                                  h2_array_p, h2_array_bool_p, s1_array_p, s2_array_p, include_p6_p)


if __name__ == "__main__":
    filename_prefix = 'K_Sample'
    # fixed_filename_prefix = 'K_Sample_fixed'
    first_file = 1
    number_of_spectra = 5
    # number_of_fit_cycles = 1
    numPeaks = 13
    dataFilename = 'testResultsVariableBG.txt'
    fixedFilename = 'testResultsVariableBG_fixed.txt'
    boolFilename = 'testResultsVariableBG_fixed_bool.txt'
    pretextFilename = 'testResultsVariableBG_pretext.txt'
    include_poly6 = False

    identify_and_fix_values(dataFilename, fixedFilename, boolFilename, first_file, number_of_spectra, pretextFilename, filename_prefix, include_poly6)
