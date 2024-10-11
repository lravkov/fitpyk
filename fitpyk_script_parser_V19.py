# Current Author: Lucas A. Ravkov
# Version: March 2020
# Contact: Lravkov@gmail.com
#
import pandas as pd


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


def pretext_list_to_string(s):
    # initialize an empty string and a counter so that you don't add an extra space at the end
    str1 = ""
    counter = 0

    # traverse in the string
    for ele in s:
        counter += 1
        str1 += str(ele)
        if counter < len(s):  # add spaces between all strings and make sure to not add one after last entry
            str1 += ''

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


def polynomial6_to_string(p6_p, num_peaks_p):
    p6_list_p = p6_p.values.tolist()
    p6_str = list_to_string(p6_list_p)
    p6_sep_list = p6_str.split()

    counter = 0
    for ele in p6_sep_list:
        # print(ele)
        if counter == 1:
            a0 = ele
        elif counter == 4:
            a1 = ele
        elif counter == 7:
            a2 = ele
        elif counter == 10:
            a3 = ele
        elif counter == 13:
            a4 = ele
        elif counter == 16:
            a5 = ele
        elif counter == 19:
            a6 = ele
        counter += 1
    print_str = 'guess %' + '_' + '%s = Polynomial6(a0=~%s, a1=~%s, a2=~%s, a3=~%s, a4=~%s, a5=~%s, a6=~%s)\n' % (
        str(3 * num_peaks_p + 3), a0, a1, a2, a3, a4, a5, a6)
    return print_str


def boolean_checker(param_list, i_position, j_position, boolean_array):
    if boolean_array[i_position] == '0':
        return_str = '~' + str(param_list[j_position])
    elif boolean_array[i_position] == '1':
        return_str = str(param_list[j_position])
    else:
        pass

    return return_str


def gen_fityk_commands(first_file, num_peaks, data_fr, hwhm1_bool_array, hwhm2_bool_array, shape1_bool_array, shape2_bool_array, fout, pretext_data, spectra, original_filename_prefix_g, info_filename_p, include_p6_p, pulling_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, file_spacer_p, peak_types_string_p):
    data_array = []

    load_string_prefix = "@0 < '_EXECUTED_SCRIPT_DIR_/" + '{}'.format(data_dir_p) + '/' + original_filename_prefix_g
    load_string = load_string_prefix + '{}'.format(file_spacer_p) + str(spectra).zfill(z_fill_p) + '{}'.format(file_suffix_p) + ".{}'".format(file_type_p)
    fout.write(load_string + '\n')
    # print(pretext_data)
    fout.write(pretext_data)  # was (pretext_ data + '\n') before

    if not include_p6_p:
        peak_range_p = num_peaks
    elif include_p6_p:
        peak_range_p = num_peaks - 1

    peak_type_p = '0'  # default peak type is SplitPearson7
    peak_types_list_p = peak_types_string_p.split(', ')
    # print(peak_types_list_p)  # commented out MAR-17-2022

    for dataset in range(1, 2):
        for i in range(peak_range_p):

            peak_type_temp_list_p = peak_types_list_p[i].split('\n')

            if peak_type_temp_list_p[0] == '0':
                # print('SplitPearson7')  # commented out MAR-17-2022
                peak_type_p = '0'
            elif peak_type_temp_list_p[0] == '1':
                # print('SplitPseudoVoigt')
                peak_type_p = '1'
            else:
                # print(peak_type_temp_list_p[0])  # commented out MAR-17-2022
                print('Invalid Peak Type.')

            data_str = data_fr.iloc[i, 0]
            data_str = str(data_str)
            param_list = data_str.split()
            for j in range(len(param_list)):
                if param_list[j] == '+/-':
                    param_list[j] = param_list[j]
                elif param_list[j] == '?':
                    param_list[j] = param_list[j]
                else:
                    if j == 0:  # %_{3*i + 3}.height()
                        pass
                    if j == 3:  # %_{3*i + 3}.center()
                        pass
                    if j == 6:  # %_{3*i + 3}.hwhm1()
                        hwhm1_str = boolean_checker(param_list, i, j, hwhm1_bool_array)
                    if j == 9:  # %_{3*i + 3}.hwhm2()
                        hwhm2_str = boolean_checker(param_list, i, j, hwhm2_bool_array)
                    if j == 12:  # %_{3*i + 3}.shape1()
                        shape1_str = boolean_checker(param_list, i, j, shape1_bool_array)
                    if j == 15:  # %_{3*i + 3}.shape2()
                        shape2_str = boolean_checker(param_list, i, j, shape2_bool_array)

            data_array.append(param_list)
            if peak_type_p == '0':  # SplitPearson7
                print_str = 'guess %' + '_' + '%s = SplitPearson7(height=~%s, center=~%s, hwhm1=%s, hwhm2=%s, shape1=%s, shape2=%s)\n' % (str(3 * i + 3), param_list[0], param_list[3], hwhm1_str, hwhm2_str, shape1_str, shape2_str)
            elif peak_type_p == '1':  # will have to change to SplitPseudoVoigt
                print_str = 'guess %' + '_' + '%s = SplitPseudoVoigt(height=~%s, center=~%s, hwhm1=%s, hwhm2=%s, shape1=%s, shape2=%s)\n' % (str(3 * i + 3), param_list[0], param_list[3], hwhm1_str, hwhm2_str, shape1_str, shape2_str)
            else:
                print_str = 'INVALID PEAK TYPE'

            fout.write(print_str)

        if include_p6_p:
            fout.write(polynomial6_to_string(data_fr.iloc[-1:,:], num_peaks))

        if not pulling_p:
            fout.write('fit\n')
            # save info to info_filename
            save_location = "'_EXECUTED_SCRIPT_DIR_/" + info_filename_p + "'"
            # if this is the first spectra, create a new file, overwriting if old exists
            if spectra == first_file:
                fout.write('info filename > ' + save_location + '\n')
            else:
                fout.write('info filename >> ' + save_location + '\n')
            fout.write('info peaks_err >> ' + save_location + '\n')
            fout.write('\n')


def gen_fityk_commands_V2(first_file, num_peaks, data_fr, hwhm1_bool_array, hwhm2_bool_array, shape1_bool_array, shape2_bool_array, fout, pretext_data, spectra, original_filename_prefix_g, info_filename_p, include_p6_p, pulling_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, file_spacer_p, peak_types_string_p):
    data_array = []
    if not pulling_p:
        load_string_prefix = "@0 < '_EXECUTED_SCRIPT_DIR_/" + '{}'.format(data_dir_p) + '/' + original_filename_prefix_g
    else:
        load_string_prefix = "@0 < '{}".format(data_dir_p) + original_filename_prefix_g

    load_string = load_string_prefix + '{}'.format(file_spacer_p) + str(spectra).zfill(z_fill_p) + '{}'.format(file_suffix_p) + ".{}'".format(file_type_p)
    fout.write(load_string + '\n')
    fout.write(pretext_data)  # was (pretext_ data + '\n') before

    if not include_p6_p:
        peak_range_p = num_peaks
    elif include_p6_p:
        peak_range_p = num_peaks - 1

    peak_type_p = '0'  # default peak type is SplitPearson7
    peak_types_list_p = peak_types_string_p.split(', ')
    # print(peak_types_list_p)  # commented out MAR-17-2022

    for dataset in range(1, 2):
        for i in range(peak_range_p):
            peak_type_temp_list_p = peak_types_list_p[i].split('\n')

            if peak_type_temp_list_p[0] == '0':
                # print('SplitPearson7')  # commented out MAR-17-2022
                peak_type_p = '0'
            elif peak_type_temp_list_p[0] == '1':
                # print('SplitPseudoVoigt')
                peak_type_p = '1'
            else:
                # print(peak_type_temp_list_p[0])  # commented out MAR-17-2022
                print('Invalid Peak Type.')

            data_str = data_fr.iloc[i, 0]
            data_str = str(data_str)
            param_list = data_str.split()
            for j in range(len(param_list)):
                if param_list[j] == '+/-':
                    param_list[j] = param_list[j]
                elif param_list[j] == '?':
                    param_list[j] = param_list[j]
                else:
                    if j == 0:  # %_{3*i + 3}.height()
                        pass
                    if j == 3:  # %_{3*i + 3}.center()
                        pass
                    if j == 6:  # %_{3*i + 3}.hwhm1()
                        hwhm1_str = boolean_checker(param_list, i, j, hwhm1_bool_array)
                    if j == 9:  # %_{3*i + 3}.hwhm2()
                        hwhm2_str = boolean_checker(param_list, i, j, hwhm2_bool_array)
                    if j == 12:  # %_{3*i + 3}.shape1()
                        shape1_str = boolean_checker(param_list, i, j, shape1_bool_array)
                    if j == 15:  # %_{3*i + 3}.shape2()
                        shape2_str = boolean_checker(param_list, i, j, shape2_bool_array)

            data_array.append(param_list)
            if peak_type_p == '0':  # SplitPearson7
                print_str = 'guess %' + '_' + '%s = SplitPearson7(height=~%s, center=~%s, hwhm1=%s, hwhm2=%s, shape1=%s, shape2=%s)\n' % (
                str(3 * i + 3), param_list[0], param_list[3], hwhm1_str, hwhm2_str, shape1_str, shape2_str)
            elif peak_type_p == '1':  # will have to change to SplitPseudoVoigt
                print_str = 'guess %' + '_' + '%s = SplitPseudoVoigt(height=~%s, center=~%s, hwhm1=%s, hwhm2=%s, shape1=%s, shape2=%s)\n' % (
                str(3 * i + 3), param_list[0], param_list[3], hwhm1_str, hwhm2_str, shape1_str, shape2_str)
            else:
                print_str = 'INVALID PEAK TYPE'

            fout.write(print_str)

        if include_p6_p:
            fout.write(polynomial6_to_string(data_fr.iloc[-1:,:], num_peaks))

        if not pulling_p:
            fout.write('fit\n')
            # save info to info_filename
            save_location = "'_EXECUTED_SCRIPT_DIR_/" + info_filename_p + "'"
            # if this is the first spectra, create a new file, overwriting if old exists
            if spectra == first_file:
                fout.write('info filename > ' + save_location + '\n')
            else:
                fout.write('info filename >> ' + save_location + '\n')
            fout.write('info peaks_err >> ' + save_location + '\n')
            fout.write('\n')


def parse(data_filename_bool, pretext_filename_p, data_filename, first_file_p, number_of_spectra_p, filename_prefix_p, original_filename_prefix_p, info_filename_p, include_p6_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, file_spacer_p):
    num_peaks = int(pd.read_csv(pretext_filename_p, sep='\t').iloc[3, 0])
    bool_data = pd.read_csv(data_filename_bool)

    with open(pretext_filename_p) as myfile:
        head_p = [next(myfile) for x in range(4)]
    pretext_data = pretext_list_to_string(head_p)

    with open(pretext_filename_p, "r") as file:
        first_line_p = file.readline()
        for last_line_p in file:
            pass
    # print(last_line_p)
    peak_types_string_p = last_line_p

    data_temp = pd.read_csv(data_filename, sep="\t")

    _script_name = '_script_' + filename_prefix_p.lower() + '.fit'
    fout = open(_script_name, 'w')
    for spectrum in range(first_file_p, first_file_p + number_of_spectra_p):
        hwhm1_bool_array = bool_data.iloc[0 + 5 * (spectrum - first_file_p), 0].split()  # hwhm1 bool array
        hwhm2_bool_array = bool_data.iloc[1 + 5 * (spectrum - first_file_p), 0].split()  # hwhm2 bool array
        shape1_bool_array = bool_data.iloc[2 + 5 * (spectrum - first_file_p), 0].split()  # shape1 bool array
        shape2_bool_array = bool_data.iloc[3 + 5 * (spectrum - first_file_p), 0].split()  # shape2 bool array

        # in first term after :, added in the extra + 2
        df = data_temp[((spectrum - first_file_p) * num_peaks + 1) + 2 * (spectrum - first_file_p):(num_peaks + 1) + (2 + num_peaks) * (spectrum - first_file_p)]

        # decide whether or not it's a poly then do the right one
        gen_fityk_commands(first_file_p, num_peaks, df, hwhm1_bool_array, hwhm2_bool_array, shape1_bool_array,
                                shape2_bool_array, fout, pretext_data, spectrum, original_filename_prefix_p,
                                info_filename_p, include_p6_p, False, data_dir_p, file_type_p, z_fill_p, file_suffix_p,
                                file_spacer_p, peak_types_string_p)

    fout.write('# End of ' + _script_name)

    # print('\n')
    # print(_script_name, 'generated.')  # python 3.7


def create_fityk_single_frame_no_fit(data_filename_bool, pretext_filename_p, data_filename, first_file_p, spectra_p, filename_prefix_p, original_filename_prefix_p, info_filename_p, include_p6_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, file_spacer_p):
    num_peaks = int(pd.read_csv(pretext_filename_p, sep='\t').iloc[3, 0])
    bool_data = pd.read_csv(data_filename_bool)

    with open(pretext_filename_p) as myfile:
        head_p = [next(myfile) for x in range(4)]
    pretext_data = pretext_list_to_string(head_p)

    data_temp = pd.read_csv(data_filename, sep="\t")

    _script_name = '_script_' + filename_prefix_p.lower() + '.fit'
    fout = open(_script_name, 'w')
    # for spectrum in range(first_file_p, first_file_p + number_of_spectra_p):
    hwhm1_bool_array = bool_data.iloc[0 + 5 * (spectra_p - first_file_p), 0].split()  # hwhm1 bool array
    hwhm2_bool_array = bool_data.iloc[1 + 5 * (spectra_p - first_file_p), 0].split()  # hwhm2 bool array
    shape1_bool_array = bool_data.iloc[2 + 5 * (spectra_p - first_file_p), 0].split()  # shape1 bool array
    shape2_bool_array = bool_data.iloc[3 + 5 * (spectra_p - first_file_p), 0].split()  # shape2 bool array

        # in first term after :, added in the extra + 2
    df = data_temp[((spectra_p - first_file_p) * num_peaks + 1) + 2 * (spectra_p - first_file_p):(num_peaks + 1) + (2 + num_peaks) * (spectra_p - first_file_p)]

        # decide whether or not it's a poly then do the right one
    gen_fityk_commands(first_file_p, num_peaks, df, hwhm1_bool_array, hwhm2_bool_array, shape1_bool_array,
                            shape2_bool_array, fout, pretext_data, spectra_p, original_filename_prefix_p,
                            info_filename_p, include_p6_p, True, data_dir_p, file_type_p, z_fill_p, file_suffix_p,
                            file_spacer_p)

    fout.write('# End of ' + _script_name)

    # print('\n')
    # print(_script_name, 'generated.')  # python 3.7


def create_fityk_single_frame_no_fit_v2(data_filename_bool, pretext_filename_p, data_filename, first_file_p, spectra_p, filename_prefix_p, original_filename_prefix_p, info_filename_p, include_p6_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, file_spacer_p, file_storage_loc_p):
    # pretext_filename_loc_p = file_storage_loc_p + pretext_filename_p
    num_peaks = int(pd.read_csv(pretext_filename_p, sep='\t').iloc[3, 0])
    bool_data = pd.read_csv(data_filename_bool)

    with open(pretext_filename_p) as myfile:
        head_p = [next(myfile) for x in range(4)]
    pretext_data = pretext_list_to_string(head_p)

    with open(pretext_filename_p, "r") as file:
        first_line_p = file.readline()
        for last_line_p in file:
            pass
    # print(last_line_p)
    peak_types_string_p = last_line_p

    data_temp = pd.read_csv(data_filename, sep="\t")

    _script_name = '_script_' + filename_prefix_p.lower() + '.fit'
    fout = open(_script_name, 'w')
    # for spectrum in range(first_file_p, first_file_p + number_of_spectra_p):
    hwhm1_bool_array = bool_data.iloc[0 + 5 * (spectra_p - first_file_p), 0].split()  # hwhm1 bool array
    hwhm2_bool_array = bool_data.iloc[1 + 5 * (spectra_p - first_file_p), 0].split()  # hwhm2 bool array
    shape1_bool_array = bool_data.iloc[2 + 5 * (spectra_p - first_file_p), 0].split()  # shape1 bool array
    shape2_bool_array = bool_data.iloc[3 + 5 * (spectra_p - first_file_p), 0].split()  # shape2 bool array

        # in first term after :, added in the extra + 2
    df = data_temp[((spectra_p - first_file_p) * num_peaks + 1) + 2 * (spectra_p - first_file_p):(num_peaks + 1) + (2 + num_peaks) * (spectra_p - first_file_p)]

        # decide whether or not it's a poly then do the right one
    gen_fityk_commands_V2(first_file_p, num_peaks, df, hwhm1_bool_array, hwhm2_bool_array, shape1_bool_array,
                          shape2_bool_array, fout, pretext_data, spectra_p, original_filename_prefix_p,
                          info_filename_p, include_p6_p, True, data_dir_p, file_type_p, z_fill_p, file_suffix_p,
                          file_spacer_p, peak_types_string_p)

    fout.write('# End of ' + _script_name)

    # print('\n')
    # print(_script_name, 'generated.')  # python 3.7


# ############################################### START OF SCRIPT #####################################################
if __name__ == "__main__":
    original_filename_prefix = 'K_Sample'
    filename_prefix = 'K_Sample_fixed'
    first_file = 1
    number_of_spectra = 3
    info_filename = 'testResultsVariableBG.txt'
    # number_of_fit_cycles = 1
    numPeaks = 13
    dataFilenameBool = 'testResultsVariableBG_fixed_bool.txt'
    pretextFilename = 'testResultsVariableBG_pretext.txt'
    dataFilename = 'testResultsVariableBG_fixed.txt'

    parse(dataFilenameBool, pretextFilename, dataFilename, first_file, number_of_spectra, numPeaks, filename_prefix, original_filename_prefix, info_filename)
