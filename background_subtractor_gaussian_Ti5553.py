import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd


def subtract_background(centres, fwhms, background_fwhms, centre_windows):
    fwhms_corrected = []
    for pos, background_fwhm in enumerate(background_fwhms):
        filter_lower = centre_windows[pos][0]
        filter_upper = centre_windows[pos][1]
        print(filter_lower)
        print(filter_upper)
        print(background_fwhm)

        # go through the df and subtract the background_fwhm from each fwhm within the filter bounds
        for loc, centre in enumerate(centres):
            print(centre)
            print(fwhms.loc[loc])

            centre = float(centre)
            fwhm_val = float(fwhms.loc[loc])
            if filter_lower <= centre <= filter_upper:
                corrected_value = np.sqrt((fwhm_val ** 2) - (background_fwhm ** 2))
                print(corrected_value)
                if corrected_value is not np.nan:
                    fwhms_corrected.append(corrected_value)
                else:
                    fwhms_corrected.append(0)

    # print(fwhms)
    # print(centres)
    return fwhms_corrected


if __name__ == "__main__":
    '''
    start input params
    '''

    storage_dir = 'D:/PyCharmProjects/fityk_scripting_2022/LANL-Ti-5553_results/'
    file_name = 'mWH-worthy-LANL-Ti5553.txt'

    background_fwhms = [
        0.0130221,
        0.0134550,
        0.0140106,
        0.0146335,
        0.0152974,
        0.0159828,
        0.0167001
    ]

    centre_windows = [
        [5.2, 5.9],
        [7.5, 8.2],
        [9.4, 10.0],
        [11.0, 11.5],
        [12.2, 12.7],
        [13.5, 14.0],
        [14.6, 15.0]
    ]

    '''
        end input params
    '''

    raw_data = storage_dir + file_name

    df = pd.read_table(raw_data, engine='python', delimiter=', ')
    df.columns = ['patternNumber', 'centre', 'deltaCentre', 'fwhm', 'deltaFwhm', 'lhwhm', 'deltaLhwhm', 'rhwhm', 'deltaRhwhm', 'lshape', 'deltaLshape', 'rshape', 'deltaRshape', 'info']
    print(df)

    patternNumbers = df['patternNumber'].tolist()
    infos = df['info'].tolist()
    centres = df['centre']
    fwhms = df['fwhm']

    fwhms_corrected = subtract_background(centres, fwhms, background_fwhms, centre_windows)

    print(patternNumbers)
    print(infos)

    centres = centres.tolist()
    print(centres)
    # print(fwhms.tolist())
    # print(fwhms_corrected)

    # CONVERT nan to 0
    # fwhms_corrected = np.array(fwhms_corrected)
    # fwhms_corrected = np.nan_to_num(fwhms_corrected)
    # fwhms_corrected = fwhms_corrected.tolist()

    print(fwhms_corrected)

    # # pick out particular pattern number and info
    # '''
    # single pattern version
    # '''
    # centres_to_fit = []
    # fwhms_to_fit = []
    #
    # filter_pattern_number = 180.0  # 158.0 + "'-120--110'", 180.0 + "'-120--110'" for nan example
    # filter_info = "'-120--110'"
    #
    # for pos, pattern_number in enumerate(patternNumbers):
    #     if pattern_number == filter_pattern_number:
    #         if infos[pos] == filter_info:
    #             centres_to_fit.append(centres[pos])
    #             fwhms_to_fit.append(fwhms_corrected[pos])
    #
    # print(centres_to_fit)
    # print(fwhms_to_fit)
    # #
    # '''
    # end single pattern version
    # '''

    # pick out particular pattern number and info
    '''
    multiple pattern version
    '''
    list_of_infos_to_fit = []
    list_of_patterns_to_fit = []
    list_of_centres_to_fit = []
    list_of_fwhms_to_fit = []

    # centres_to_fit = []
    # fwhms_to_fit = []

    list_inp = patternNumbers
    res_list = []
    for item in list_inp:
        if item not in res_list:
            res_list.append(item)
    list_of_filter_pattern_number = sorted(res_list)
    print(list_of_filter_pattern_number)
    print(len(list_of_filter_pattern_number))

    list_of_filter_info = ["'Ti555'"]

    for pattern_filter in list_of_filter_pattern_number:
        # print(pattern_filter)
        for info_filter in list_of_filter_info:
            centres_to_fit = []
            fwhms_to_fit = []
            for pos, pattern_number in enumerate(patternNumbers):
                # print(pattern_number)
                if pattern_number == pattern_filter:
                    if infos[pos] == info_filter:
                        centres_to_fit.append(centres[pos])
                        fwhms_to_fit.append(fwhms_corrected[pos])

            list_of_patterns_to_fit.append(pattern_filter)
            list_of_infos_to_fit.append(info_filter)
            list_of_centres_to_fit.append(centres_to_fit)
            list_of_fwhms_to_fit.append(fwhms_to_fit)

    print(list_of_patterns_to_fit)
    print(list_of_infos_to_fit)
    print(list_of_centres_to_fit)
    print(list_of_fwhms_to_fit)
    #
    '''
    end multiple pattern version
    '''

    # CREATE THE DATASET TO OPTIMIZE - REMEMBER TO UNCOMMENT OUT OTHER SECTION TOO
    with open('Ti5553_to_mwh_optimize.txt', 'w') as f:
        f.write(f'pattern, info, centre, fwhm\n')

    # FIND ALL THE PATTERNS WHERE AT LEAST 4 POINTS INCLUDING NANs ARE GOOD
    number_of_peaks = 4  # was 4 before
    for pos, fwhms in enumerate(list_of_fwhms_to_fit):
        if len(fwhms) >= number_of_peaks:
            # print(fwhms)
            fwhms_corrected = np.array(fwhms)
            fwhms_corrected = np.nan_to_num(fwhms_corrected)
            fwhms_corrected = fwhms_corrected.tolist()

            counter = 0
            loc_to_del = []
            for loc, fwhm in enumerate(fwhms_corrected):
                if fwhm == 0:
                    counter += 1
                    loc_to_del.append(loc)

            # print(loc_to_del)
            # if loc_to_del is not None or [0]:
            #     for loc in loc_to_del.reverse():
            #         del fwhms[loc]
            #         del list_of_centres_to_fit[pos][loc]

            # print(counter)
            if (len(fwhms) - counter) >= number_of_peaks:
                print('---------')

                # THIS CLEARS THE nan AND THE CORRESPONDING centre VALUE, BUT I HAVE NO CLUE WHY IT WORKS
                print(loc_to_del)
                if len(loc_to_del) > 0:
                    loc_to_del_rev = loc_to_del.reverse()
                    print(loc_to_del_rev)
                    if loc_to_del is not None:
                        for loc in loc_to_del:
                            del fwhms[loc]
                            del list_of_centres_to_fit[pos][loc]

                print(list_of_patterns_to_fit[pos])
                print(list_of_infos_to_fit[pos])
                print(list_of_centres_to_fit[pos])
                print(fwhms)

                # CREATE THE DATASET TO OPTIMIZE - REMEMBER TO UNCOMMENT OUT OTHER SECTION TOO
                with open('Ti5553_to_mwh_optimize.txt', 'a') as f:
                    for ele, fwhm in enumerate(fwhms):
                        f.write(f'{list_of_patterns_to_fit[pos]}, {list_of_infos_to_fit[pos]}, {list_of_centres_to_fit[pos][ele]}, {fwhm}\n')


    # ele = 4
    # for ele in range(8, 16):
    #     plt.plot(list_of_centres_to_fit[ele], list_of_fwhms_to_fit[ele], marker='o', linestyle='',
    #             markersize=3.5, markerfacecolor='none', label=f'PN:{list_of_patterns_to_fit[ele]}, CAKE:{list_of_infos_to_fit[ele]}')
    # plt.legend(loc='upper left')
    # plt.xlabel('K')
    # plt.ylabel('FWHMs corrected')
    # # plt.title(f'FWHMs corrected vs. K - SS316 Block3b PN:{list_of_patterns_to_fit[ele]}, CAKE:{list_of_infos_to_fit[ele]} - GE1')
    # plt.show()
    # interactive(True)
