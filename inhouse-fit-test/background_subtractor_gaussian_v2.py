import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd


def subtract_background(centers, fwhms, background_fwhms, centre_windows):
    fwhms_corrected = []
    locs = []
    for pos, background_fwhm in enumerate(background_fwhms):
        filter_lower = centre_windows[pos][0]
        filter_upper = centre_windows[pos][1]

        for loc, center in enumerate(centers):
            if filter_lower <= center <= filter_upper:
                corrected_value = np.sqrt((fwhms[loc] ** 2) - (background_fwhm ** 2))
                fwhms_corrected.append(corrected_value)
                locs.append(loc)
    return fwhms_corrected, locs


if __name__ == "__main__":
    """
    get the background fwhms from instrumental profiles, and interpolation.
    take the output from this code and put it into 
    """


    '''
    start input params
    '''

    storage_dir = 'D:/PyCharmProjects/fityk_scripting_2022/inhouse-fit-test/test_project/results_new/'
    input_file_name = 'new_results_all_params.txt'
    output_file_name = 'GE1_APS316_new.txt'

    background_fwhms = [0.016719033468952767, 0.017138578860802736, 0.01862491022563727, 0.019637252185565675, 0.019965075151194042, 0.02123658494638189, 0.022146272107705946, 0.02244298615843852, 0.02362320448776832]

    center_windows = [
        [4.5, 5],
        [5, 6],
        [7.5, 8],
        [9, 9.4],
        [9.4, 10],
        [11, 11.5],
        [12, 12.25],
        [12.25, 13],
        [13, 14]
    ]

    max_corrected_fwhm = 0.1
    min_number_of_peaks = 4
    '''
        end input params
    '''

    raw_data = storage_dir + input_file_name
    output_file = storage_dir + output_file_name

    df = pd.read_table(raw_data, engine='python', delimiter=', ')
    df.columns = ['patternNumber', 'centre', 'deltaCentre', 'fwhm', 'deltaFwhm', 'lhwhm', 'deltaLhwhm', 'rhwhm', 'deltaRhwhm', 'height', 'delta_height', 'lshape', 'deltaLshape', 'rshape', 'deltaRshape', 'info']
    print(df)

    patternNumbers = df['patternNumber'].tolist()
    infos = df['info'].tolist()
    centers = df['centre'].tolist()
    fwhms = df['fwhm'].tolist()

    fwhms_corrected, locs = subtract_background(centers, fwhms, background_fwhms, center_windows)

    patternNumbers_corrected = []
    infos_corrected = []
    centers_corrected = []
    for loc in locs:
        patternNumbers_corrected.append(patternNumbers[loc])
        infos_corrected.append(infos[loc])
        centers_corrected.append(centers[loc])

    unique_patterns = list(set(patternNumbers_corrected))

    sorted_patterns = []
    sorted_centers = []
    sorted_fwhms = []
    sorted_infos = []
    for pattern in unique_patterns:
        counter = 0
        for loc, original_pattern in enumerate(patternNumbers_corrected):
            if pattern == original_pattern and fwhms_corrected[loc] < max_corrected_fwhm:
                sorted_patterns.append(pattern)
                sorted_centers.append(centers_corrected[loc])
                sorted_fwhms.append(fwhms_corrected[loc])
                sorted_infos.append(infos_corrected[loc])
                counter += 1
        print(counter)

        if counter < min_number_of_peaks:
            sorted_patterns = sorted_patterns[:-counter or None]
            sorted_centers = sorted_centers[:-counter or None]
            sorted_fwhms = sorted_fwhms[:-counter or None]
            sorted_infos = sorted_infos[:-counter or None]

    print(sorted_patterns)
    print(len(sorted_patterns))
    print(sorted_centers)
    print(len(sorted_centers))
    print(sorted_fwhms)
    print(len(sorted_fwhms))
    print(sorted_infos)
    print(len(sorted_infos))

    # Create the dataset to optimize
    with open(output_file, 'w+') as file:
        file.write(f'pattern, info, centre, fwhm\n')
        for ele, fwhm in enumerate(sorted_fwhms):
            # print(ele)
            if np.isfinite(fwhm):
                file.write(f'{sorted_patterns[ele]}, {sorted_infos[ele]}, {sorted_centers[ele]}, {fwhm}\n')

