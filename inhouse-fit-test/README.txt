run fitpyk_2023_v15.py
# ================================================================================================================
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/inhouse-fit-test/'  # include / at the end of the base path
    project_path = 'test_project/'
    data_dir = 'data/'  # no / at end of data dir name
    storage_dir_name = 'results_new/'
    file_prefix = 'K_lr_dt_hu_1_4permm2'
    file_spacer = '_'
    file_suffix = ''
    data_type = '.dat'  # do not include '.' before the file type
    z_fill = 6  # number of integers in pattern name (e.g 00XXX) would be 5
    first_file = 43  #
    number_of_spectra = 1512  # 1512 (756)

    min_x = 4.00
    max_x = 14.00

    peak_centers = [4.800, 5.558, 7.858, 9.215, 9.621, 11.11, 12.11, 12.43, 13.621]
    peak_heights = [4500, 4000, 2000, 2000, 250, 240, 300, 400, 100]
    peak_types = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 = PS7, 1 = PSV

    bckgrd_pts = [4.025, 4.58, 5.01, 5.311, 5.85, 7.62, 8.10, 8.98, 9.38, 9.514, 9.761, 10.925, 11.34, 11.9, 12.23,
                  12.30, 12.60, 13.47, 13.74, 13.975]
    half_window = 0.025
    divs = 4

    use_poly6 = True

    min_cutoff = 200

    max_nfev = 10000  # maximum number of function evaluations
    num_cores = 7
# ================================================================================================================

run fitpyk_result_compiler_v4.py
# ================================================================================================================
    output_file = 'new_results_all_params.txt'
    info = 'SS316L'

    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/inhouse-fit-test/'  # include / at the end of the base path
    project_path = 'test_project/'
    data_dir = 'data/'
    storage_dir_name = 'results_new/'
    file_prefix = 'K_lr_dt_hu_1_4permm2'
    file_spacer = '_'
    file_suffix = ''
    data_type = '.dat'  # do not include '.' before the file type
    z_fill = 4  # number of integers in pattern name (e.g 00XXX) would be 5
    first_file = 43  #
    number_of_spectra = 1512  # 1512 (756)

    min_x = 4.00
    max_x = 14.00

    peak_centers = [4.800, 5.558, 7.858, 9.215, 9.621, 11.11, 12.11, 12.43, 13.621]
    peak_heights = [4500, 4000, 2000, 2000, 250, 240, 300, 400, 100]
    peak_types = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 = PS7, 1 = PSV

    bckgrd_pts = [4.025, 4.58, 5.01, 5.311, 5.85, 7.62, 8.10, 8.98, 9.38, 9.514, 9.761, 10.925, 11.34, 11.9, 12.23,
                  12.30, 12.60, 13.47, 13.74, 13.975]
    half_window = 0.025
    divs = 4

    use_poly6 = True

    min_cutoff = 200

    max_nfev = 10000  # maximum number of function evaluations
    num_cores = 7
# ================================================================================================================
OUTPUT > base_path + output_file

run fitpyk_2023_v7_instrumental.py
# ================================================================================================================
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/inhouse-fit-test/'  # include / at the end of the base path
    project_path = 'test_project/'
    data_dir = 'instrumentals/'
    storage_dir_name = 'results_instr_test/'
    file_prefix = 'CeO'
    file_spacer = '_'
    file_suffix = ''
    data_type = '.dat'  # do not include '.' before the file type
    z_fill = 4  # number of integers in pattern name (e.g 00XXX) would be 5
    first_file = 7  #
    number_of_spectra = 1  # 1512 (756)

    min_x = 2.50
    max_x = 13.65

    peak_centers = [3.093, 3.583, 5.087, 5.949, 6.220, 7.183, 7.809, 8.030, 8.806, 9.330, 10.158, 10.631, 10.783,
                    11.353, 11.770, 11.910, 12.443, 12.828, 12.956, 13.437]
    peak_heights = [17000, 5000, 10500, 8600, 1600, 1700, 3500, 2300, 3000, 2700, 900, 2300, 1000, 1100, 700, 450, 200,
                    1000, 350, 1000]
    peak_types = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 = PS7, 1 = PSV

    bckgrd_pts = [2.525, 2.856, 3.288, 3.414, 3.855, 4.704, 5.412, 5.632, 6.451, 6.938, 7.379, 7.615, 8.260, 8.575,
                  9.015, 9.141, 9.566, 9.975, 10.321, 10.447, 10.950, 11.186, 11.517, 11.627, 12.052, 12.288, 12.587,
                  12.697, 13.106, 13.247, 13.593, 13.625]
    half_window = 0.025
    divs = 4

    use_poly6 = True

    min_cutoff = 200  # at least one maxima must be larger than this value

    max_nfev = 10000  # maximum number of function evaluations
    num_cores = 7
# ================================================================================================================

run instr_fxn generator_v1.py
# ==================================================================================================================
    # xpos = [3.112, 3.593, 5.079, 5.956, 6.22, 7.182, 7.826, 8.03,  8.796, 9.329, 10.16, 10.62, 10.77, 11.36, 11.77,
    #         11.91, 12.44, 12.82, 12.95, 13.44]
    # ypos = [0.015919, 0.015733, 0.017228, 0.017484, 0.018025, 0.017334, 0.018814, 0.018746, 0.019427, 0.019401,
    #         0.02068, 0.0208, 0.02115, 0.02104, 0.02237, 0.021379, 0.031, 0.0219299, 0.02379, 0.02361]

    # removed the outlier point (4th last in commented out section)
    xpos = [3.112, 3.593, 5.079, 5.956, 6.22, 7.182, 7.826, 8.03, 8.796, 9.329, 10.16, 10.62, 10.77, 11.36, 11.77,
            11.91, 12.82, 12.95, 13.44]
    ypos = [0.015919, 0.015733, 0.017228, 0.017484, 0.018025, 0.017334, 0.018814, 0.018746, 0.019427, 0.019401,
            0.02068, 0.0208, 0.02115, 0.02104, 0.02237, 0.021379, 0.0219299, 0.02379, 0.02361]

    peak_xpos = [4.812030308, 5.559123035, 7.860357978, 9.215537623, 9.627431311, 11.12557791, 12.11697605, 12.4281252, 13.61425024]
# ==================================================================================================================
OUTPUT > background_fwhms

run background_subtractor_gaussian_v2.py
# ==================================================================================================================
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
# ==================================================================================================================

run mwh_optimize_v1.py
# ==================================================================================================================

# ==================================================================================================================
OUTPUT > storage_dir + output_file_name

run mwh_output_plotting_v1.py
# ==================================================================================================================

# ==================================================================================================================
OUTPUT >
