# put your peak definitions for various materials in this file
from fitpyk_material_backend import *


# ############################################# AlSi10Mg Data ##############################################
def add_al_si10_mg_info():
    # SET ACTIVE RANGE AND ZOOM
    active_range_val = 'A = (x > 2.36395 and x < 10.15)'
    zoom_val = 'plot [2.3:10.2] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = False
    num_peaks = 13 + 0
    # SET BACKGROUND BY USING A WINDOW WITH DELTA x OF +- 0.002
    background_val = '%bg0 = Spline(1.268,45.7,argmin(y if x > 2.214 and x < 2.218),min(y if x > 2.214 and x < 2.218),' \
        'argmin(y if x > 3.668 and x < 3.672),min(y if x > 3.668 and x < 3.672),' \
        'argmin(y if x > 4.648 and x < 4.652),min(y if x > 4.648 and x < 4.652),' \
        'argmin(y if x > 6.503 and x < 6.508),min(y if x > 6.503 and x < 6.508),' \
        'argmin(y if x > 7.228 and x < 7.232),min(y if x > 7.228 and x < 7.232),' \
        'argmin(y if x > 7.692 and x < 7.696),min(y if x > 7.692 and x < 7.696),' \
        'argmin(y if x > 10.220 and x < 10.224),min(y if x > 10.220 and x < 10.224))'
    # peak_types = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6


def add_al_si10_mg_peaks(file_out):
    file_out.write('guess %_3 = SplitPearson7 [2.8936 : 3.34]\n')
    file_out.write('guess %_6 = SplitPearson7 [4.065 : 4.498]\n')
    file_out.write('guess %_9 = SplitPearson7 [4.9166 : 4.9745]\n')
    file_out.write('guess %_12 = SplitPearson7 [5.17 : 5.273]\n')
    file_out.write('guess %_15 = SplitPearson7 [6.03 : 6.18]\n')
    file_out.write('guess %_18 = SplitPearson7 [6.90 : 7.10]\n')
    file_out.write('guess %_21 = SplitPearson7 [7.308 : 7.45]\n')
    file_out.write('%_21.center = 7.371\n')
    file_out.write('guess %_27 = SplitPearson7 [8.11 : 8.3]\n')
    file_out.write('guess %_24 = SplitPearson7 [7.96 : 8.10]\n')
    file_out.write('%_24.center = 8.04\n')
    file_out.write('guess %_30 = SplitPearson7 [8.5 : 8.62]\n')
    file_out.write('guess %_33 = SplitPearson7 [8.94 : 9.1]\n')
    file_out.write('%_33.height = ~9.127\n')
    file_out.write('%_33.hwhm1 = ~0.08\n')
    file_out.write('%_33.hwhm2 = ~0.08\n')
    file_out.write('guess %_36 = SplitPearson7 [9.47 : 9.66]\n')
    file_out.write('guess %_39 = SplitPearson7 [9.85 : 9.94]\n')
# ###########################################################################################

# ############################################ V11 AlSiMg Data ####################################
def add_alsimg_test_info():
    # SET ACTIVE RANGE AND ZOOM
    active_range_val = 'A = (x > 2.36395 and x < 10.15)'
    zoom_val = 'plot [2.3:10.2] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = False
    num_peaks = 13 + 0
    # SET BACKGROUND BY USING A WINDOW WITH DELTA x OF +- 0.002
    list_of_bckgrd_pts_p = [2.31, 2.53, 2.78, 3.56, 3.75, 4.00, 4.58, 4.68, 5.50, 5.75, 5.87, 6.37, 6.53, 6.72, 7.19, 7.58, 7.79, 8.40, 8.75, 9.22, 9.39, 9.75, 10.10, 10.30]
    list_of_bckgrd_pts_y_p = [39.2]
    half_window_p = 0.02
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6


def add_alsimg_test_peaks(file_out):
    file_out.write('guess %_3 = SplitPearson7 [2.8936 : 3.34]\n')
    file_out.write('guess %_6 = SplitPearson7 [4.065 : 4.498]\n')
    file_out.write('guess %_9 = SplitPearson7 [4.9166 : 4.9745]\n')
    file_out.write('guess %_12 = SplitPearson7 [5.17 : 5.273]\n')
    file_out.write('guess %_15 = SplitPearson7 [6.03 : 6.18]\n')
    file_out.write('guess %_18 = SplitPearson7 [6.90 : 7.10]\n')
    file_out.write('guess %_21 = SplitPearson7 [7.308 : 7.45]\n')
    file_out.write('%_21.center = 7.371\n')
    file_out.write('guess %_27 = SplitPearson7 [8.11 : 8.3]\n')
    file_out.write('guess %_24 = SplitPearson7 [7.96 : 8.10]\n')
    file_out.write('%_24.center = 8.04\n')
    file_out.write('guess %_30 = SplitPearson7 [8.5 : 8.62]\n')
    file_out.write('guess %_33 = SplitPearson7 [8.94 : 9.1]\n')
    file_out.write('%_33.height = ~9.127\n')
    file_out.write('%_33.hwhm1 = ~0.08\n')
    file_out.write('%_33.hwhm2 = ~0.08\n')
    file_out.write('guess %_36 = SplitPearson7 [9.47 : 9.66]\n')
    file_out.write('guess %_39 = SplitPearson7 [9.85 : 9.94]\n')
###################################################################################################

# ############################################# AlSiMg SplitPseudoVoigt #############################
def add_alsimg_spv_info():
    # SET ACTIVE RANGE AND ZOOM
    active_range_val = 'A = (x > 2.36395 and x < 10.15)'
    zoom_val = 'plot [2.3:10.2] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = False
    num_peaks = 13 + 0
    # SET BACKGROUND BY USING A WINDOW WITH DELTA x OF +- 0.002
    list_of_bckgrd_pts_p = [2.31, 2.53, 2.78, 3.56, 3.75, 4.00, 4.58, 4.68, 5.50, 5.75, 5.87, 6.37, 6.53, 6.72, 7.19, 7.58, 7.79, 8.40, 8.75, 9.22, 9.39, 9.75, 10.10, 10.30]
    list_of_bckgrd_pts_y_p = [39.2]
    half_window_p = 0.02
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1'
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_alsimg_spv_peaks(file_out):
    file_out.write('guess %_3 = SplitPearson7 [2.8936 : 3.34]\n')
    file_out.write('guess %_6 = SplitPseudoVoigt [4.065 : 4.498]\n')
    file_out.write('guess %_9 = SplitPseudoVoigt [4.9166 : 4.9745]\n')
    file_out.write('guess %_12 = SplitPearson7 [5.17 : 5.273]\n')
    file_out.write('guess %_15 = SplitPearson7 [6.03 : 6.18]\n')
    file_out.write('guess %_18 = SplitPearson7 [6.90 : 7.10]\n')
    file_out.write('guess %_21 = SplitPearson7 [7.308 : 7.55]\n')
    file_out.write('%_21.center = 7.371\n')
    file_out.write('guess %_24 = SplitPearson7 [7.96 : 8.10]\n')
    file_out.write('%_24.center = 8.04\n')
    file_out.write('guess %_27 = SplitPseudoVoigt [8.11 : 8.3]\n')
    file_out.write('guess %_30 = SplitPearson7 [8.5 : 8.62]\n')
    file_out.write('guess %_33 = SplitPearson7 [8.94 : 9.1]\n')
    file_out.write('%_33.height = ~9.127\n')
    file_out.write('%_33.hwhm1 = ~0.08\n')
    file_out.write('%_33.hwhm2 = ~0.08\n')
    file_out.write('guess %_36 = SplitPearson7 [9.47 : 9.66]\n')
    file_out.write('guess %_39 = SplitPseudoVoigt [9.85 : 9.94]\n')
########################################################################################################

# ############################################# Cu Neutron Data ##############################################
def add_cu_neutron_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.0 and x < 17.0)'
    zoom_val = 'plot [3.95:17.05] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = False
    num_peaks = 13 + 0
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.87, 5.147, 6.787, 8.547, 10.317, 11.597, 12.997, 13.997, 15.227, 15.997, 16.997]
    list_of_bckgrd_pts_y_p = [0.168]
    background_val = bg_spline_generator(list_to_string(background_generator(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p)))
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6


def add_cu_neutron_peaks(file_out):
    file_out.write('guess %_3 = SplitPearson7 [4.575 : 4.975]\n')
    file_out.write('guess %_6 = SplitPearson7 [5.319 : 5.750]\n')
    file_out.write('guess %_9 = SplitPearson7 [7.555 : 8.083]\n')
    file_out.write('guess %_12 = SplitPearson7 [8.922 : 9.322]\n')
    file_out.write('guess %_15 = SplitPearson7 [9.400 : 9.818]\n')
    file_out.write('guess %_18 = SplitPearson7 [10.885 : 11.228]\n')
    file_out.write('guess %_21 = SplitPearson7 [11.838 : 12.182]\n')
    file_out.write('guess %_24 = SplitPearson7 [12.239 : 12.525]\n')
    file_out.write('guess %_27 = SplitPearson7 [13.325 : 13.745]\n')
    file_out.write('guess %_30 = SplitPearson7 [14.183 : 14.584]\n')
    file_out.write('guess %_33 = SplitPearson7 [15.499 : 15.823]\n')
    file_out.write('guess %_36 = SplitPearson7 [16.204 : 16.433]\n')
    file_out.write('guess %_39 = SplitPearson7 [16.509 : 16.795]\n')
# ###########################################################################################

# ############################################# Cu Neutron Data 16 peaks #######################################
def add_cu_neutron_test_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.0 and x < 18.8)'
    zoom_val = 'plot [3.95:18.85] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = False
    num_peaks = 16 + 0
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.87, 5.147, 6.787, 8.547, 10.317, 11.597, 12.997, 13.997, 15.227, 15.997, 16.997, 17.847, 18.627, 18.947]
    list_of_bckgrd_pts_y_p = [0.168]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    # background_val = bg_spline_generator(list_to_string(background_generator(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_cu_neutron_test_peaks(file_out):
    file_out.write('guess %_3 = SplitPearson7 [4.575 : 4.975]\n')
    file_out.write('guess %_6 = SplitPearson7 [5.319 : 5.750]\n')
    file_out.write('guess %_9 = SplitPearson7 [7.555 : 8.083]\n')
    file_out.write('guess %_12 = SplitPearson7 [8.922 : 9.322]\n')
    file_out.write('guess %_15 = SplitPearson7 [9.400 : 9.818]\n')
    file_out.write('guess %_18 = SplitPearson7 [10.885 : 11.228]\n')
    file_out.write('guess %_21 = SplitPearson7 [11.838 : 12.182]\n')
    file_out.write('guess %_24 = SplitPearson7 [12.239 : 12.525]\n')
    file_out.write('guess %_27 = SplitPearson7 [13.325 : 13.745]\n')
    file_out.write('guess %_30 = SplitPearson7 [14.183 : 14.584]\n')
    file_out.write('guess %_33 = SplitPearson7 [15.499 : 15.823]\n')
    file_out.write('guess %_36 = SplitPearson7 [16.204 : 16.433]\n')
    file_out.write('guess %_39 = SplitPearson7 [16.509 : 16.795]\n')
    file_out.write('guess %_42 = SplitPearson7 [17.425 : 17.600]\n')
    file_out.write('guess %_45 = SplitPearson7 [18.050 : 18.205]\n')
    file_out.write('guess %_48 = SplitPearson7 [18.300 : 18.450]\n')
# ###########################################################################################

# ############################################# Cu Neutron Data 8 peaks #######################################
def add_cu_neutron_test2_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.0 and x < 12.90)'
    zoom_val = 'plot [3.95:12.95] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 8 + 1
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.87, 5.147, 6.787, 8.547, 10.317, 11.597, 12.997]
    list_of_bckgrd_pts_y_p = [0.168]
    background_val = bg_spline_generator(list_to_string(background_generator(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p)))
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6


def add_cu_neutron_test2_peaks(file_out):
    file_out.write('guess %_3 = SplitPearson7 [4.575 : 4.975]\n')
    file_out.write('guess %_6 = SplitPearson7 [5.319 : 5.750]\n')
    file_out.write('guess %_9 = SplitPearson7 [7.555 : 8.083]\n')
    file_out.write('guess %_12 = SplitPearson7 [8.922 : 9.322]\n')
    file_out.write('guess %_15 = SplitPearson7 [9.400 : 9.818]\n')
    file_out.write('guess %_18 = SplitPearson7 [10.885 : 11.228]\n')
    file_out.write('guess %_21 = SplitPearson7 [11.838 : 12.182]\n')
    file_out.write('guess %_24 = SplitPearson7 [12.239 : 12.525]\n')
    file_out.write('guess %_27 = Polynomial6\n')
# ###########################################################################################


# ############################################# Cu Neutron Data 16 peaks #######################################
def add_cu_neutron_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.0 and x < 18.8)'
    zoom_val = 'plot [3.95:18.85] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 16 + 1
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.87, 5.147, 5.977, 6.787, 8.547, 9.367, 10.317, 11.597, 12.997, 13.997, 15.227, 15.997, 16.997, 17.847, 18.627, 18.947]
    list_of_bckgrd_pts_y_p = [0.168]
    # half_window_p = 0.005
    # background_val = bg_spline_generator(list_to_string(background_generator_V2(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p)))
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_cu_neutron_poly_peaks(file_out):
    file_out.write('guess %_3 = SplitPearson7 [4.575 : 4.975]\n')
    file_out.write('guess %_6 = SplitPearson7 [5.319 : 5.750]\n')
    file_out.write('guess %_9 = SplitPearson7 [7.555 : 8.083]\n')
    file_out.write('guess %_12 = SplitPearson7 [8.922 : 9.322]\n')
    file_out.write('guess %_15 = SplitPearson7 [9.400 : 9.818]\n')
    file_out.write('guess %_18 = SplitPearson7 [10.885 : 11.228]\n')
    file_out.write('guess %_21 = SplitPearson7 [11.838 : 12.182]\n')
    file_out.write('guess %_24 = SplitPearson7 [12.239 : 12.525]\n')
    file_out.write('guess %_27 = SplitPearson7 [13.325 : 13.745]\n')
    file_out.write('guess %_30 = SplitPearson7 [14.183 : 14.584]\n')
    file_out.write('guess %_33 = SplitPearson7 [15.499 : 15.823]\n')
    file_out.write('guess %_36 = SplitPearson7 [16.204 : 16.433]\n')
    file_out.write('guess %_39 = SplitPearson7 [16.509 : 16.795]\n')
    file_out.write('guess %_42 = SplitPearson7 [17.425 : 17.600]\n')
    file_out.write('guess %_45 = SplitPearson7 [18.050 : 18.205]\n')
    file_out.write('guess %_48 = SplitPearson7 [18.300 : 18.450]\n')
    file_out.write('guess %_51 = Polynomial6\n')
# ###########################################################################################


# ################################################ CeO Synchrotron Data ###############################################
def add_ceo_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 2.642 and x < 16.211)'
    zoom_val = 'plot [2.600:16.250] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 25 + 1
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [2.451, 2.971, 3.586, 4.021, 4.477, 4.944, 6.026, 6.737, 7.331, 7.734, 8.031, 8.626, 9.082,
                            9.411, 9.655, 10.015, 10.514, 10.822, 11.023, 11.522, 11.819, 12.084, 12.275, 12.668,
                            12.986, 13.209, 13.389, 13.771, 14.005, 14.302, 14.429, 14.684, 15.002, 15.267, 15.384,
                            15.745, 15.957, 16.180, 16.296]
    list_of_bckgrd_pts_y_p = [2200]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ceo_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3.268, hw_peaks_p, 3.268, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3.766, hw_peaks_p, 3.766, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.337, hw_peaks_p, 5.337, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.260, hw_peaks_p, 6.260, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.535, hw_peaks_p, 6.535, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.565, hw_peaks_p, 7.565, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.233, hw_peaks_p, 8.233, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.456, hw_peaks_p, 8.456, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.252, hw_peaks_p, 9.252, hw_peaks_p))
    file_out.write('guess %_30 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.814, hw_peaks_p, 9.814, hw_peaks_p))
    file_out.write('guess %_33 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.694, hw_peaks_p, 10.694, hw_peaks_p))
    file_out.write('guess %_36 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.182, hw_peaks_p, 11.182, hw_peaks_p))
    file_out.write('guess %_39 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.270, 2*hw_peaks_p, 11.270, 2*hw_peaks_p))
    file_out.write('guess %_42 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.957, hw_peaks_p, 11.957, hw_peaks_p))
    file_out.write('guess %_45 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.424, hw_peaks_p, 12.424, hw_peaks_p))
    file_out.write('guess %_48 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.530, hw_peaks_p, 12.530, hw_peaks_p))
    file_out.write('guess %_51 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.103, hw_peaks_p, 13.103, hw_peaks_p))
    file_out.write('guess %_54 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.506, hw_peaks_p, 13.506, hw_peaks_p))
    file_out.write('guess %_57 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.644, hw_peaks_p, 13.644, hw_peaks_p))
    file_out.write('guess %_60 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.174, hw_peaks_p, 14.174, hw_peaks_p))
    file_out.write('guess %_63 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.546, hw_peaks_p, 14.546, hw_peaks_p))
    file_out.write('guess %_66 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(15.140, hw_peaks_p, 15.140, hw_peaks_p))
    file_out.write('guess %_69 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(15.501, hw_peaks_p, 15.501, hw_peaks_p))
    file_out.write('guess %_72 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(15.607, hw_peaks_p, 15.607, hw_peaks_p))
    file_out.write('guess %_75 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(16.073, hw_peaks_p, 16.073, hw_peaks_p))
    file_out.write('guess %_78 = Polynomial6\n')
# ###########################################################################################


# ################################################ CeO Synchrotron Data ###############################################
def add_lanl_74_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 2.642 and x < 16.211)'
    zoom_val = 'plot [2.600:16.250] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 25 + 1
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [2.451, 2.971, 3.586, 4.021, 4.477, 4.944, 6.026, 6.737, 7.331, 7.734, 8.031, 8.626, 9.082,
                            9.411, 9.655, 10.015, 10.514, 10.822, 11.023, 11.522, 11.819, 12.084, 12.275, 12.668,
                            12.986, 13.209, 13.389, 13.771, 14.005, 14.302, 14.429, 14.684, 15.002, 15.267, 15.384,
                            15.745, 15.957, 16.180, 16.296]
    list_of_bckgrd_pts_y_p = [2200]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p

# ##########################################################################################

# ################################################ ANSTO ss316 Synchrotron Data ###############################################

# block3a_ss316_110--100
def add_ge1_block3a_ss316_110100_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 12.93)'
    zoom_val = 'plot [4.25:13.18] []'
    # SET ADDITIONAL POLYNOMIAL BACKGROUND TERM
    include_polynomial6 = True
    # SET NUMBER OF PEAKS TO EVALUATE
    num_peaks = 6 + 1  # + 1 if include_polynomial6, + 0 if NOT include_polynomial6
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.600, 4.900, 5.457, 5.734, 5.915, 6.373,
                            6.845, 7.026, 7.137, 7.664, 7.970, 8.275,
                            8.789, 9.219, 9.58, 9.761, 10.302, 10.761,
                            11.219, 11.608, 11.913, 12.371, 12.677]
    list_of_bckgrd_pts_y_p = [0.56]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    # SET PEAK TYPES
    peak_types_p = '0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_110100_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.241, hw_peaks_p, 5.241, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.054, hw_peaks_p, 6.054, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.574, hw_peaks_p, 8.574, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.039, hw_peaks_p, 10.039, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.483, hw_peaks_p, 10.483, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.114, hw_peaks_p, 12.114, hw_peaks_p))
    file_out.write('guess %_21 = Polynomial6\n')


# block3a_ss316_110--100 --------- voigt
def add_ge1_block3a_ss316_110100_poly_voigt_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 12.93)'
    zoom_val = 'plot [4.25:13.18] []'
    # SET ADDITIONAL POLYNOMIAL BACKGROUND TERM
    include_polynomial6 = True
    # SET NUMBER OF PEAKS TO EVALUATE
    num_peaks = 6 + 1
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.600, 4.900, 5.457, 5.734, 5.915, 6.373,
                            6.845, 7.026, 7.137, 7.664, 7.970, 8.275,
                            8.789, 9.219, 9.58, 9.761, 10.302, 10.761,
                            11.219, 11.608, 11.913, 12.371, 12.677]
    list_of_bckgrd_pts_y_p = [0.56]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    # SET PEAK TYPES
    peak_types_p = '1, 1, 1, 1, 1, 1'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_110100_poly_voigt_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(5.241, hw_peaks_p, 5.241, hw_peaks_p))
    file_out.write('guess %_6 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(6.054, hw_peaks_p, 6.054, hw_peaks_p))
    file_out.write('guess %_9 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(8.574, hw_peaks_p, 8.574, hw_peaks_p))
    file_out.write('guess %_12 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(10.039, hw_peaks_p, 10.039, hw_peaks_p))
    file_out.write('guess %_15 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(10.483, hw_peaks_p, 10.483, hw_peaks_p))
    file_out.write('guess %_18 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(12.114, hw_peaks_p, 12.114, hw_peaks_p))
    file_out.write('guess %_21 = Polynomial6\n')


# block3a_ss316_110--100 --------- mixed
def add_ge1_block3a_ss316_110100_poly_mixed_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 12.93)'
    zoom_val = 'plot [4.25:13.18] []'
    # SET ADDITIONAL POLYNOMIAL BACKGROUND TERM
    include_polynomial6 = True
    # SET NUMBER OF PEAKS TO EVALUATE
    num_peaks = 6 + 1
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.600, 4.900, 5.457, 5.734, 5.915, 6.373,
                            6.845, 7.026, 7.137, 7.664, 7.970, 8.275,
                            8.789, 9.219, 9.58, 9.761, 10.302, 10.761,
                            11.219, 11.608, 11.913, 12.371, 12.677]
    list_of_bckgrd_pts_y_p = [0.56]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    # SET PEAK TYPES
    peak_types_p = '1, 0, 1, 1, 0, 1'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_110100_poly_mixed_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(5.241, hw_peaks_p, 5.241, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.054, hw_peaks_p, 6.054, hw_peaks_p))
    file_out.write('guess %_9 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(8.574, hw_peaks_p, 8.574, hw_peaks_p))
    file_out.write('guess %_12 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(10.039, hw_peaks_p, 10.039, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.483, hw_peaks_p, 10.483, hw_peaks_p))
    file_out.write('guess %_18 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(12.114, hw_peaks_p, 12.114, hw_peaks_p))
    file_out.write('guess %_21 = Polynomial6\n')


# block3a_ss316_120--110
def add_ge1_block3a_ss316_120110_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 3.5 and x < 14.25)'
    zoom_val = 'plot [3.25:14.5] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 8 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.373, 3.750, 4.295, 4.869, 5.512, 5.880,
                            6.270, 6.707, 7.223, 7.763, 8.211, 8.912,
                            9.325, 9.830, 10.267, 10.600, 11.059, 11.496,
                            11.852, 12.334, 12.701, 12.954, 13.379, 13.666,
                            13.896, 14.160]
    list_of_bckgrd_pts_y_p = [0.640]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    # [111] > [400] (6 peaks)


    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_120110_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.240, hw_peaks_p, 5.240, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.050, hw_peaks_p, 6.050, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.555, hw_peaks_p, 8.555, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.034, hw_peaks_p, 10.034, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.475, hw_peaks_p, 10.475, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.106, hw_peaks_p, 12.106, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.190, hw_peaks_p, 13.190, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.535, hw_peaks_p, 13.535, hw_peaks_p))
    file_out.write('guess %_27 = Polynomial6\n')

# block3a_ss316_130--120
def add_ge1_block3a_ss316_130120_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 14.25)'
    zoom_val = 'plot [4.25:14.5] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 8 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.404, 4.869, 5.512, 5.880,
                            6.270, 6.707, 7.223, 7.763, 8.211, 8.912,
                            9.325, 9.830, 10.267, 10.600, 11.059, 11.496,
                            11.852, 12.334, 12.701, 12.954, 13.379, 13.666,
                            13.896, 14.160]
    list_of_bckgrd_pts_y_p = [0.779]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    # [111] > [400] (6 peaks)


    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_130120_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.240, hw_peaks_p, 5.240, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.045, hw_peaks_p, 6.045, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.550, hw_peaks_p, 8.550, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.024, hw_peaks_p, 10.024, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.478, hw_peaks_p, 10.478, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.100, hw_peaks_p, 12.100, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.188, hw_peaks_p, 13.188, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.535, hw_peaks_p, 13.535, hw_peaks_p))
    file_out.write('guess %_27 = Polynomial6\n')

# block3a_ss316_140--130
def add_ge1_block3a_ss316_140130_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 14.25)'
    zoom_val = 'plot [4.25:14.5] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 8 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.401, 4.869, 5.512, 5.880,
                            6.270, 6.707, 7.223, 7.763, 8.211, 8.912,
                            9.325, 9.830, 10.267, 10.600, 11.059, 11.496,
                            11.852, 12.334, 12.701, 12.954, 13.379, 13.666,
                            13.896, 14.160]
    list_of_bckgrd_pts_y_p = [0.77]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    # [111] > [400] (6 peaks)


    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_140130_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.240, hw_peaks_p, 5.240, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.05, hw_peaks_p, 6.05, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.550, hw_peaks_p, 8.550, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.028, hw_peaks_p, 10.028, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.478, hw_peaks_p, 10.478, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.100, hw_peaks_p, 12.100, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.187, hw_peaks_p, 13.187, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.54, hw_peaks_p, 13.54, hw_peaks_p))
    file_out.write('guess %_27 = Polynomial6\n')


# block3a_ss316_140--130 -------- voigt
def add_ge1_block3a_ss316_140130_poly_voigt_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 14.25)'
    zoom_val = 'plot [4.25:14.5] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 8 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.401, 4.869, 5.512, 5.880,
                            6.270, 6.707, 7.223, 7.763, 8.211, 8.912,
                            9.325, 9.830, 10.267, 10.600, 11.059, 11.496,
                            11.852, 12.334, 12.701, 12.954, 13.379, 13.666,
                            13.896, 14.160]
    list_of_bckgrd_pts_y_p = [0.77]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '1, 1, 1, 1, 1, 1, 1, 1'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_140130_poly_voigt_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(5.240, hw_peaks_p, 5.240, hw_peaks_p))
    file_out.write('guess %_6 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(6.05, hw_peaks_p, 6.05, hw_peaks_p))
    file_out.write('guess %_9 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(8.550, hw_peaks_p, 8.550, hw_peaks_p))
    file_out.write('guess %_12 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(10.028, hw_peaks_p, 10.028, hw_peaks_p))
    file_out.write('guess %_15 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(10.478, hw_peaks_p, 10.478, hw_peaks_p))
    file_out.write('guess %_18 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(12.100, hw_peaks_p, 12.100, hw_peaks_p))
    file_out.write('guess %_21 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(13.187, hw_peaks_p, 13.187, hw_peaks_p))
    file_out.write('guess %_24 = SplitPseudoVoigt [({} - {}) : ({} + {})]\n'.format(13.54, hw_peaks_p, 13.54, hw_peaks_p))
    file_out.write('guess %_27 = Polynomial6\n')


# block3a_ss316_150--140
def add_ge1_block3a_ss316_150140_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 14.25)'
    zoom_val = 'plot [4.25:14.5] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 8 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.401, 4.869, 5.512, 5.880,
                            6.270, 6.707, 7.223, 7.763, 8.211, 8.912,
                            9.325, 9.830, 10.267, 10.600, 11.059, 11.496,
                            11.852, 12.334, 12.701, 12.954, 13.379, 13.666,
                            13.896, 14.160]
    list_of_bckgrd_pts_y_p = [0.76]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    # [111] > [400] (6 peaks)


    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_150140_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.240, hw_peaks_p, 5.240, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.05, hw_peaks_p, 6.05, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.550, hw_peaks_p, 8.550, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.03, hw_peaks_p, 10.03, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.478, hw_peaks_p, 10.478, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.100, hw_peaks_p, 12.100, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.189, hw_peaks_p, 13.189, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.52, hw_peaks_p, 13.52, hw_peaks_p))
    file_out.write('guess %_27 = Polynomial6\n')

# block3a_ss316_160--150
def add_ge1_block3a_ss316_160150_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 14.25)'
    zoom_val = 'plot [4.25:14.5] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 8 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.401, 4.869, 5.512, 5.880,
                            6.270, 6.707, 7.223, 7.763, 8.211, 8.912,
                            9.325, 9.830, 10.267, 10.600, 11.059, 11.496,
                            11.852, 12.334, 12.701, 12.954, 13.379, 13.666,
                            13.896, 14.160]
    list_of_bckgrd_pts_y_p = [0.75]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    # [111] > [400] (6 peaks)


    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_160150_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.240, hw_peaks_p, 5.240, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.043, hw_peaks_p, 6.043, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.550, hw_peaks_p, 8.550, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.03, hw_peaks_p, 10.03, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.478, hw_peaks_p, 10.478, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.100, hw_peaks_p, 12.100, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.189, hw_peaks_p, 13.189, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.52, hw_peaks_p, 13.52, hw_peaks_p))
    file_out.write('guess %_27 = Polynomial6\n')

# block3a_ss316_170--160
def add_ge1_block3a_ss316_170160_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 14.00)'
    zoom_val = 'plot [4.25:14.25] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 8 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.401, 4.869, 5.512, 5.880,
                            6.270, 6.707, 7.223, 7.763, 8.211, 8.912,
                            9.325, 9.830, 10.267, 10.600, 11.059, 11.496,
                            11.852, 12.334, 12.701, 12.954, 13.379, 13.666,
                            13.896, 14.160]
    list_of_bckgrd_pts_y_p = [0.77]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    # [111] > [400] (6 peaks)


    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_170160_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.240, hw_peaks_p, 5.240, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.05, hw_peaks_p, 6.05, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.550, hw_peaks_p, 8.550, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.03, hw_peaks_p, 10.03, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.478, hw_peaks_p, 10.478, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.110, hw_peaks_p, 12.110, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.189, hw_peaks_p, 13.189, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.53, hw_peaks_p, 13.53, hw_peaks_p))
    file_out.write('guess %_27 = Polynomial6\n')


# block3a_ss316_180--170
def add_ge1_block3a_ss316_180170_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 13.50)'
    zoom_val = 'plot [4.25:13.75] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 7 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.401, 4.869, 5.512, 5.880, 6.270, 6.707, 7.223, 7.763, 8.211, 8.912,
                            9.325, 9.830, 10.267, 10.600, 11.059, 11.496, 11.852, 12.334, 12.701, 12.954, 13.379]
    list_of_bckgrd_pts_y_p = [0.52]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_block3a_ss316_180170_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.240, hw_peaks_p, 5.240, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.05, hw_peaks_p, 6.05, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.550, hw_peaks_p, 8.550, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.04, hw_peaks_p, 10.04, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.478, hw_peaks_p, 10.478, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.105, hw_peaks_p, 12.105, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.20, hw_peaks_p, 13.20, hw_peaks_p))
    file_out.write('guess %_24 = Polynomial6\n')
# ###########################################################################################

# LANL_STEEL_DATA_JAN_2022_bank1_instrumental
def add_k_CMWP_116306_bank1_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 2.83 and x < 14.42)'
    zoom_val = 'plot [2.69:14.58] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 15 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [2.757, 2.964, 3.417, 3.852, 4.286, 4.664, 4.928, 5.438, 5.834, 6.363,
                            6.741, 7.080, 7.571, 7.798, 8.289, 8.704, 9.195, 9.346, 9.780, 10.139,
                            10.611, 11.102, 11.366, 11.857, 12.273, 12.518, 12.915, 13.330, 13.500,
                            13.953, 14.406]
    list_of_bckgrd_pts_y_p = [3.51]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_k_CMWP_116306_bank1_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3.176, hw_peaks_p, 3.176, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.200, hw_peaks_p, 5.200, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.107, hw_peaks_p, 6.107, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.355, hw_peaks_p, 7.355, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.017, hw_peaks_p, 8.017, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.019, hw_peaks_p, 9.019, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.567, hw_peaks_p, 9.567, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.399, hw_peaks_p, 10.399, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.872, hw_peaks_p, 10.872, hw_peaks_p))
    file_out.write('guess %_30 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.666, hw_peaks_p, 11.666, hw_peaks_p))
    file_out.write('guess %_33 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.063, hw_peaks_p, 12.063, hw_peaks_p))
    file_out.write('guess %_36 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.762, hw_peaks_p, 12.762, hw_peaks_p))
    file_out.write('guess %_39 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.159, hw_peaks_p, 13.159, hw_peaks_p))
    file_out.write('guess %_42 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.783, hw_peaks_p, 13.783, hw_peaks_p))
    file_out.write('guess %_45 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.162, hw_peaks_p, 14.162, hw_peaks_p))
    file_out.write('guess %_48 = Polynomial6\n')
# ###########################################################################################

# LANL_STEEL_DATA_JAN_2022_bank3_instrumental
def add_k_CMWP_116306_bank3_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.5 and x < 14.42)'
    zoom_val = 'plot [4.34:14.58] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 14 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.286, 4.664, 4.928, 5.438, 5.834, 6.363,
                            6.741, 7.080, 7.571, 7.798, 8.289, 8.704, 9.195, 9.346, 9.780, 10.139,
                            10.611, 11.102, 11.366, 11.857, 12.273, 12.518, 12.915, 13.330, 13.500,
                            13.953, 14.406]
    list_of_bckgrd_pts_y_p = [3.13]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_k_CMWP_116306_bank3_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.200, hw_peaks_p, 5.200, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.107, hw_peaks_p, 6.107, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.355, hw_peaks_p, 7.355, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.017, hw_peaks_p, 8.017, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.019, hw_peaks_p, 9.019, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.567, hw_peaks_p, 9.567, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.399, hw_peaks_p, 10.399, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.872, hw_peaks_p, 10.872, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.641, hw_peaks_p, 11.641, hw_peaks_p))
    file_out.write('guess %_30 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.063, hw_peaks_p, 12.063, hw_peaks_p))
    file_out.write('guess %_33 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.762, hw_peaks_p, 12.762, hw_peaks_p))
    file_out.write('guess %_36 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.159, hw_peaks_p, 13.159, hw_peaks_p))
    file_out.write('guess %_39 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.783, hw_peaks_p, 13.783, hw_peaks_p))
    file_out.write('guess %_42 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.123, hw_peaks_p, 14.123, hw_peaks_p))
    file_out.write('guess %_45 = Polynomial6\n')
# ###########################################################################################

# LANL_STEEL_DATA_JAN_2022_bank3_H1_H2
def add_k_CMWP_H1_H2_bank3_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 3.4 and x < 14.75)'
    zoom_val = 'plot [3.33:14.93] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 13 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.32, 3.671, 4.108, 4.527, 5.069, 5.296,
                            5.785, 6.013, 6.397, 6.590, 6.992, 7.481, 8.198, 8.757, 9.928, 10.749,
                            11.361, 11.763, 12.655, 13.127, 13.861, 14.105, 14.682]
    list_of_bckgrd_pts_y_p = [4.88]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_k_CMWP_H1_H2_bank3_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3.916, hw_peaks_p, 3.916, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(4.796, hw_peaks_p, 4.796, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.524, hw_peaks_p, 5.524, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.180, hw_peaks_p, 6.180, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.773, hw_peaks_p, 6.773, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.815, hw_peaks_p, 7.815, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.162, hw_peaks_p, 9.162, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.575, hw_peaks_p, 9.575, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.066, hw_peaks_p, 11.066, hw_peaks_p))
    file_out.write('guess %_30 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.036, hw_peaks_p, 12.036, hw_peaks_p))
    file_out.write('guess %_33 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.368, hw_peaks_p, 12.368, hw_peaks_p))
    file_out.write('guess %_36 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.536, hw_peaks_p, 13.536, hw_peaks_p))
    file_out.write('guess %_39 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.363, hw_peaks_p, 14.363, hw_peaks_p))
    file_out.write('guess %_42 = Polynomial6\n')
# ###########################################################################################

# LANL_CHESS-may-2022
def add_000130_CeO2_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 2.85 and x < 11.00)'
    zoom_val = 'plot [2.60:11.25] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 13 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [2.853, 3.273, 3.426, 3.808, 4.300, 4.664, 4.865, 5.438, 5.770, 6.075, 6.363,
                            6.649, 7.080, 7.387, 7.655, 7.922, 8.289, 8.636, 9.056, 9.514, 9.780, 9.986,
                            10.253, 10.457, 10.686, 10.865, 10.979]
    list_of_bckgrd_pts_y_p = [480000]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_000130_CeO2_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3.108, hw_peaks_p, 3.108, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3.579, hw_peaks_p, 3.579, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.069, hw_peaks_p, 5.069, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.935, hw_peaks_p, 5.935, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.203, hw_peaks_p, 6.203, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.158, hw_peaks_p, 7.158, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.808, hw_peaks_p, 7.808, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.999, hw_peaks_p, 7.999, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.763, hw_peaks_p, 8.763, hw_peaks_p))
    file_out.write('guess %_30 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.298, hw_peaks_p, 9.298, hw_peaks_p))
    file_out.write('guess %_33 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.126, hw_peaks_p, 10.126, hw_peaks_p))
    file_out.write('guess %_36 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.584, hw_peaks_p, 10.584, hw_peaks_p))
    file_out.write('guess %_39 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.750, hw_peaks_p, 10.750, hw_peaks_p))
    file_out.write('guess %_42 = Polynomial6\n')


def add_CHESS_Ti64_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 3.0 and x < 11.144)'
    zoom_val = 'plot [2.75:11.394] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 16 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.05, 5.393, 6.239, 6.435, 7.125, 7.216, 8.740, 9.157, 9.235, 9.678, 9.860, 11.124]
    list_of_bckgrd_pts_y_p = [19000]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_CHESS_Ti64_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3.947, hw_peaks_p, 3.947, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(4.285, hw_peaks_p, 4.285, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(4.494, hw_peaks_p, 4.494, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.822, hw_peaks_p, 5.822, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.838, hw_peaks_p, 6.838, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.542, hw_peaks_p, 7.542, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.880, hw_peaks_p, 7.880, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.076, hw_peaks_p, 8.076, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.180, hw_peaks_p, 8.180, hw_peaks_p))
    file_out.write('guess %_30 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.571, hw_peaks_p, 8.571, hw_peaks_p))
    file_out.write('guess %_33 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.975, hw_peaks_p, 8.975, hw_peaks_p))
    file_out.write('guess %_36 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.430, hw_peaks_p, 9.430, hw_peaks_p))
    file_out.write('guess %_39 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.186, hw_peaks_p, 10.186, hw_peaks_p))
    file_out.write('guess %_42 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.446, hw_peaks_p, 10.446, hw_peaks_p))
    file_out.write('guess %_45 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.668, hw_peaks_p, 10.668, hw_peaks_p))
    file_out.write('guess %_48 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.967, hw_peaks_p, 10.967, hw_peaks_p))
    file_out.write('guess %_51 = Polynomial6\n')
# ###########################################################################################


# LANL-alpha-fe-si-instrumental
def add_LANL_si_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 2.85 and x < 14.97)'
    zoom_val = 'plot [2.60:15.22] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 26 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [2.853, 2.965, 3.305, 4.401, 4.475, 4.777, 5.08, 5.382, 5.929, 6.269, 6.779,
                            7.138, 7.251, 7.500, 7.855, 8.328, 8.422, 8.667, 8.875, 9.158, 9.404, 9.668,
                            10.027, 10.273, 10.518, 10.612, 11.198, 11.500, 11.764, 11.897, 12.293, 12.633,
                            13.011, 13.332, 13.577, 14.276, 14.427, 14.950]
    list_of_bckgrd_pts_y_p = [1.995]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_LANL_si_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3.196, hw_peaks_p, 3.196, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(4.274, hw_peaks_p, 4.274, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(4.935, hw_peaks_p, 4.935, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.200, hw_peaks_p, 5.200, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.108, hw_peaks_p, 6.108, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.978, hw_peaks_p, 6.978, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.375, hw_peaks_p, 7.375, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.018, hw_peaks_p, 8.018, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.188, hw_peaks_p, 8.188, hw_peaks_p))
    file_out.write('guess %_30 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.566, hw_peaks_p, 8.566, hw_peaks_p))
    file_out.write('guess %_33 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.020, hw_peaks_p, 9.020, hw_peaks_p))
    file_out.write('guess %_36 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.568, hw_peaks_p, 9.568, hw_peaks_p))
    file_out.write('guess %_39 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.871, hw_peaks_p, 9.871, hw_peaks_p))
    file_out.write('guess %_42 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.438, hw_peaks_p, 10.438, hw_peaks_p))
    file_out.write('guess %_45 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.760, hw_peaks_p, 10.760, hw_peaks_p))
    file_out.write('guess %_48 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.892, hw_peaks_p, 10.892, hw_peaks_p))
    file_out.write('guess %_51 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.043, hw_peaks_p, 11.043, hw_peaks_p))
    file_out.write('guess %_54 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.648, hw_peaks_p, 11.648, hw_peaks_p))
    file_out.write('guess %_57 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.083, hw_peaks_p, 12.083, hw_peaks_p))
    file_out.write('guess %_60 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.821, hw_peaks_p, 12.821, hw_peaks_p))
    file_out.write('guess %_63 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.161, hw_peaks_p, 13.161, hw_peaks_p))
    file_out.write('guess %_66 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.785, hw_peaks_p, 13.785, hw_peaks_p))
    file_out.write('guess %_69 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.974, hw_peaks_p, 13.974, hw_peaks_p))
    file_out.write('guess %_72 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.144, hw_peaks_p, 14.144, hw_peaks_p))
    file_out.write('guess %_75 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.617, hw_peaks_p, 14.617, hw_peaks_p))
    file_out.write('guess %_78 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.825, hw_peaks_p, 14.825, hw_peaks_p))
    file_out.write('guess %_81 = Polynomial6\n')
# ###########################################################################################

# LANL-CuFe-multilayer-foils
def add_LANL_CuFe_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 6.00 and x < 14.40)'
    zoom_val = 'plot [5.75:14.65] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 11 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [6.269, 6.779, 7.178, 7.500, 8.000, 8.328, 8.779, 8.977, 9.372, 10.027, 10.273, 10.518,
                            10.812, 11.279, 11.500, 11.764, 12.215, 12.633, 12.916, 13.204, 13.348, 13.690, 13.816,
                            14.180, 14.399]
    list_of_bckgrd_pts_y_p = [0.200]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_LANL_CuFe_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.97, hw_peaks_p, 6.97, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.80, hw_peaks_p, 7.80, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.54, hw_peaks_p, 8.54, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.18, hw_peaks_p, 9.18, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.03, hw_peaks_p, 11.03, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.95, hw_peaks_p, 11.95, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.15, hw_peaks_p, 12.15, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.38, hw_peaks_p, 12.38, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.04, hw_peaks_p, 13.04, hw_peaks_p))
    file_out.write('guess %_30 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.56, hw_peaks_p, 13.56, hw_peaks_p))
    file_out.write('guess %_33 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.95, hw_peaks_p, 13.95, hw_peaks_p))
    file_out.write('guess %_36 = Polynomial6\n')
# ###########################################################################################

# LANL-Ti555
def add_LANL_Ti555_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 3.00 and x < 17.25)'
    zoom_val = 'plot [2.75:17.50] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 9 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.164, 3.921, 4.496, 5.000, 6.403, 7.415, 8.427, 8.790, 9.237, 10.164, 10.516, 10.931,
                            11.453, 11.997, 12.924, 13.520, 13.882, 14.511, 15.161, 15.619, 16.109, 16.514, 17.068]
    list_of_bckgrd_pts_y_p = [4000]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_LANL_Ti555_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.58, hw_peaks_p, 5.58, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.89, hw_peaks_p, 7.89, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.66, hw_peaks_p, 9.66, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.16, hw_peaks_p, 11.16, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.50, hw_peaks_p, 12.50, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.69, hw_peaks_p, 13.69, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.80, hw_peaks_p, 14.80, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(15.84, hw_peaks_p, 15.84, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(16.80, hw_peaks_p, 16.80, hw_peaks_p))
    file_out.write('guess %_30 = Polynomial6\n')
# ###########################################################################################

# LANL-Ti555-instrumental-LaB6
def add_LANL_Ti555_LaB6_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 2.60 and x < 17.1)'
    zoom_val = 'plot [2.35:17.35] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 26 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [2.650, 2.830, 3.260, 4.140, 4.570, 5.170, 5.540, 5.980, 6.370, 6.710, 7.080, 7.380, 7.700,
                            8.500, 8.850, 9.100, 9.380, 9.610, 9.910, 10.040, 10.340, 10.500, 10.780, 10.990, 11.240,
                            11.350, 11.680, 12.160, 12.410, 12.570, 12.800, 12.940, 13.170, 13.310, 13.540, 13.630,
                            13.880, 14.000, 14.200, 14.340, 14.590, 14.960, 15.170, 15.310, 15.510, 15.610, 15.790,
                            15.900, 16.160, 16.480, 16.710, 16.780, 17.010]
    list_of_bckgrd_pts_y_p = [1430]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_LANL_Ti555_LaB6_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3.069, hw_peaks_p, 3.069, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(4.342, hw_peaks_p, 4.342, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.320, hw_peaks_p, 5.320, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.144, hw_peaks_p, 6.144, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6.871, hw_peaks_p, 6.871, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.528, hw_peaks_p, 7.528, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(8.695, hw_peaks_p, 8.695, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.233, hw_peaks_p, 9.233, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.724, hw_peaks_p, 9.724, hw_peaks_p))
    file_out.write('guess %_30 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.200, hw_peaks_p, 10.200, hw_peaks_p))
    file_out.write('guess %_33 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(10.655, hw_peaks_p, 10.655, hw_peaks_p))
    file_out.write('guess %_36 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.091, hw_peaks_p, 11.091, hw_peaks_p))
    file_out.write('guess %_39 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.510, hw_peaks_p, 11.510, hw_peaks_p))
    file_out.write('guess %_42 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.310, hw_peaks_p, 12.310, hw_peaks_p))
    file_out.write('guess %_45 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.690, hw_peaks_p, 12.690, hw_peaks_p))
    file_out.write('guess %_48 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.060, hw_peaks_p, 13.060, hw_peaks_p))
    file_out.write('guess %_51 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.419, hw_peaks_p, 13.419, hw_peaks_p))
    file_out.write('guess %_54 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.770, hw_peaks_p, 13.770, hw_peaks_p))
    file_out.write('guess %_57 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.112, hw_peaks_p, 14.112, hw_peaks_p))
    file_out.write('guess %_60 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(14.446, hw_peaks_p, 14.446, hw_peaks_p))
    file_out.write('guess %_63 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(15.092, hw_peaks_p, 15.092, hw_peaks_p))
    file_out.write('guess %_66 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(15.405, hw_peaks_p, 15.405, hw_peaks_p))
    file_out.write('guess %_69 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(15.712, hw_peaks_p, 15.712, hw_peaks_p))
    file_out.write('guess %_72 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(16.013, hw_peaks_p, 16.013, hw_peaks_p))
    file_out.write('guess %_75 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(16.600, hw_peaks_p, 16.600, hw_peaks_p))
    file_out.write('guess %_78 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(16.886, hw_peaks_p, 16.886, hw_peaks_p))
    file_out.write('guess %_81 = Polynomial6\n')
# ###########################################################################################


"""
    APS APRIL 2022 - HX EXPERIMENTS
"""


# APS_HX_LaB6
def add_APS_HX_LaB6_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.645 and x < 19.123)'
    zoom_val = 'plot [4.5:19.35] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 48 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.678, 4.747, 4.879, 5.243, 5.488, 5.8, 6.002, 6.211, 6.684, 6.905, 7.132, 7.275, 7.426,
                            7.528, 7.77, 7.851, 8.042, 8.262, 8.412, 8.57, 8.739, 8.911, 9.08, 9.553, 9.715, 9.979,
                            10.111, 10.328, 10.551, 10.68, 10.823, 10.94, 11.087, 11.208, 11.362, 11.703, 11.835,
                            11.945, 12.089, 12.191, 12.323, 12.433, 12.565, 12.859, 13.017, 13.127, 13.244, 13.534,
                            13.662, 13.754, 13.872, 13.967, 14.088, 14.169, 14.286, 14.381, 14.484, 14.58, 14.682,
                            14.77, 14.891, 15.152, 15.258, 15.335, 15.453, 15.53, 15.633, 15.728, 15.816, 15.908,
                            16.007, 16.087, 16.183, 16.26, 16.37, 16.608, 16.704, 16.781, 16.891, 16.946, 17.056,
                            17.129, 17.217, 17.302, 17.383, 17.46, 17.57, 17.636, 17.738, 17.959, 18.036, 18.12, 18.204,
                            18.263, 18.358, 18.439, 18.527, 18.736, 18.901, 19.008, 19.122]
    list_of_bckgrd_pts_y_p = [0.753]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV

    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_APS_HX_LaB6_poly_peaks(file_out):
    hw = 0.075  # peak half window
    file_out.write(f'guess %_3 = SplitPearson7 [({4.802} - {hw}) : ({4.802} + {hw})]\n')
    file_out.write(f'guess %_6 = SplitPearson7 [({5.378} - {hw}) : ({5.378} + {hw})]\n')
    file_out.write(f'guess %_9 = SplitPearson7 [({5.892} - {hw}) : ({5.892} + {hw})]\n')
    file_out.write(f'guess %_12 = SplitPearson7 [({6.802} - {hw}) : ({6.802} + {hw})]\n')
    file_out.write(f'guess %_15 = SplitPearson7 [({7.213} - {hw}) : ({7.213} + {hw})]\n')
    file_out.write(f'guess %_18 = SplitPearson7 [({7.591} - {hw}) : ({7.591} + {hw})]\n')
    file_out.write(f'guess %_21 = SplitPearson7 [({8.335} - {hw}) : ({8.335} + {hw})]\n')
    file_out.write(f'guess %_24 = SplitPearson7 [({8.677} - {hw}) : ({8.677} + {hw})]\n')
    file_out.write(f'guess %_27 = SplitPearson7 [({8.996} - {hw}) : ({8.996} + {hw})]\n')
    file_out.write(f'guess %_30 = SplitPearson7 [({9.619} - {hw}) : ({9.619} + {hw})]\n')
    file_out.write(f'guess %_33 = SplitPearson7 [({9.917} - {hw}) : ({9.917} + {hw})]\n')
    file_out.write(f'guess %_36 = SplitPearson7 [({10.203} - {hw}) : ({10.203} + {hw})]\n')
    file_out.write(f'guess %_39 = SplitPearson7 [({10.482} - {hw}) : ({10.482} + {hw})]\n')
    file_out.write(f'guess %_42 = SplitPearson7 [({10.757} - {hw}) : ({10.757} + {hw})]\n')
    file_out.write(f'guess %_45 = SplitPearson7 [({11.025} - {hw}) : ({11.025} + {hw})]\n')
    file_out.write(f'guess %_48 = SplitPearson7 [({11.278} - {hw}) : ({11.278} + {hw})]\n')
    file_out.write(f'guess %_51 = SplitPearson7 [({11.780} - {hw}) : ({11.780} + {hw})]\n')
    file_out.write(f'guess %_54 = SplitPearson7 [({12.019} - {hw}) : ({12.019} + {hw})]\n')
    file_out.write(f'guess %_57 = SplitPearson7 [({12.257} - {hw}) : ({12.257} + {hw})]\n')
    file_out.write(f'guess %_60 = SplitPearson7 [({12.496} - {hw}) : ({12.496} + {hw})]\n')
    file_out.write(f'guess %_63 = SplitPearson7 [({12.954} - {hw}) : ({12.954} + {hw})]\n')
    file_out.write(f'guess %_66 = SplitPearson7 [({13.178} - {hw}) : ({13.178} + {hw})]\n')
    file_out.write(f'guess %_69 = SplitPearson7 [({13.600} - {hw}) : ({13.600} + {hw})]\n')
    file_out.write(f'guess %_72 = SplitPearson7 [({13.813} - {hw}) : ({13.813} + {hw})]\n')
    file_out.write(f'guess %_75 = SplitPearson7 [({14.029} - {hw}) : ({14.029} + {hw})]\n')
    file_out.write(f'guess %_78 = SplitPearson7 [({14.224} - {hw}) : ({14.224} + {hw})]\n')
    file_out.write(f'guess %_81 = SplitPearson7 [({14.429} - {hw}) : ({14.429} + {hw})]\n')
    file_out.write(f'guess %_84 = SplitPearson7 [({14.631} - {hw}) : ({14.631} + {hw})]\n')
    file_out.write(f'guess %_87 = SplitPearson7 [({14.818} - {hw}) : ({14.818} + {hw})]\n')
    file_out.write(f'guess %_90 = SplitPearson7 [({15.214} - {hw}) : ({15.214} + {hw})]\n')
    file_out.write(f'guess %_93 = SplitPearson7 [({15.405} - {hw}) : ({15.405} + {hw})]\n')
    file_out.write(f'guess %_96 = SplitPearson7 [({15.592} - {hw}) : ({15.592} + {hw})]\n')
    file_out.write(f'guess %_99 = SplitPearson7 [({15.776} - {hw}) : ({15.776} + {hw})]\n')
    file_out.write(f'guess %_102 = SplitPearson7 [({15.948} - {hw}) : ({15.948} + {hw})]\n')
    file_out.write(f'guess %_105 = SplitPearson7 [({16.139} - {hw}) : ({16.139} + {hw})]\n')
    file_out.write(f'guess %_108 = SplitPearson7 [({16.311} - {hw}) : ({16.311} + {hw})]\n')
    file_out.write(f'guess %_111 = SplitPearson7 [({16.843} - {hw}) : ({16.843} + {hw})]\n')
    file_out.write(f'guess %_114 = SplitPearson7 [({17.008} - {hw}) : ({17.008} + {hw})]\n')
    file_out.write(f'guess %_117 = SplitPearson7 [({17.177} - {hw}) : ({17.177} + {hw})]\n')
    file_out.write(f'guess %_120 = SplitPearson7 [({17.350} - {hw}) : ({17.350} + {hw})]\n')
    file_out.write(f'guess %_123 = SplitPearson7 [({17.511} - {hw}) : ({17.511} + {hw})]\n')
    file_out.write(f'guess %_126 = SplitPearson7 [({17.676} - {hw}) : ({17.676} + {hw})]\n')
    file_out.write(f'guess %_129 = SplitPearson7 [({17.992} - {hw}) : ({17.992} + {hw})]\n')
    file_out.write(f'guess %_132 = SplitPearson7 [({18.164} - {hw}) : ({18.164} + {hw})]\n')
    file_out.write(f'guess %_135 = SplitPearson7 [({18.314} - {hw}) : ({18.314} + {hw})]\n')
    file_out.write(f'guess %_138 = SplitPearson7 [({18.476} - {hw}) : ({18.476} + {hw})]\n')
    file_out.write(f'guess %_141 = SplitPearson7 [({18.784} - {hw}) : ({18.784} + {hw})]\n')
    file_out.write(f'guess %_144 = SplitPearson7 [({18.945} - {hw}) : ({18.945} + {hw})]\n')
    file_out.write('guess %_147 = Polynomial6\n')
# ###########################################################################################

# ########################################### APS 316L TRIANGLES EXPERIMENT 2022 ####################################
# lr_dt_hu_1_4permm2
def add_ge1_ss316_hu_triangle_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 3.000 and x < 14.000)'
    zoom_val = 'plot [2.95:14.05] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 9 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.086, 3.677, 4.119, 4.888, 5.109, 5.300, 5.945, 6.642, 7.426, 8.141, 8.838, 9.937,
                            10.791, 11.366, 11.802, 12.726, 13.266, 13.877]
    list_of_bckgrd_pts_y_p = [390]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    # [111] > [400] (6 peaks)


    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_ss316_hu_triangle_poly_peaks(file_out):
    hw_peaks_p = 0.100
    file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(4.819, hw_peaks_p, 4.819, hw_peaks_p))
    file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.550, hw_peaks_p, 5.550, hw_peaks_p))
    file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.873, hw_peaks_p, 7.873, hw_peaks_p))
    file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.202, hw_peaks_p, 9.202, hw_peaks_p))
    file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.637, hw_peaks_p, 9.637, hw_peaks_p))
    file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.111, hw_peaks_p, 11.111, hw_peaks_p))
    file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.125, hw_peaks_p, 12.125, hw_peaks_p))
    file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.441, hw_peaks_p, 12.441, hw_peaks_p))
    file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.626, hw_peaks_p, 13.626, hw_peaks_p))
    file_out.write('guess %_30 = Polynomial6\n')


# lr_dt_hd_1_4permm2
def add_ge1_ss316_hd_triangle_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 3.000 and x < 14.000)'
    zoom_val = 'plot [2.95:14.05] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 9 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [3.086, 3.677, 4.119, 4.222, 4.450, 4.590, 5.042, 5.320, 5.842, 5.945, 6.642, 7.426, 8.141, 8.838, 9.937,
                            10.791, 11.366, 11.802, 12.726, 13.266, 13.877]
    list_of_bckgrd_pts_y_p = [390]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    # background_val = '%bg0 = Spline(2.553,2000, 2.847,1920, 4.083,1650, 4.67,1500, 4.964,1520, 5.693,1470, 5.947,1420, 6.838,1300, 7.264,1270, 7.871,1270, 8.733,1270, 8.945,1270, 9.543,1270, 10.151,1220, 10.434,1200, 10.931,1300, 11.518,1250, 11.751,1270, 12.197,1220, 12.744,1220, 12.927,1220, 13.312,1270, 13.828,1300, 13.95,1250, 14.375,1350, 14.73,1250, 15.024,1220, 15.267,1250, 15.388,1250, 15.783,1250, 15.935,1270, 16.229,1300)'

    # [111] > [400] (6 peaks)


    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge1_ss316_hd_triangle_poly_peaks(f):
    peaks_list_p = [4.798, 5.563, 7.858, 9.232, 9.649, 11.127, 12.118, 12.431]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))


# Ce0_0007_10degcake_ge1
def add_ge1_ss316_2022_CeO_10deg_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 2.700 and x < 13.650)'
    zoom_val = 'plot [2.65:13.70] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 20 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [2.843, 3.297, 3.419, 3.820, 4.797, 5.286, 5.739, 6.384, 6.994, 7.361, 7.622, 8.215,
                            8.616, 8.983, 9.157, 9.523, 9.977, 10.308, 10.483, 10.919, 11.215, 11.460, 11.634, 12.053,
                            12.332, 12.541, 12.681, 13.047, 13.274, 13.530, 13.620]

    list_of_bckgrd_pts_y_p = [940]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


# old style - rewrote below
# def add_ge1_ss316_2022_CeO_10deg_peaks(file_out):
#     hw_peaks_p = 0.100
#     file_out.write('guess %_3 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(4.819, hw_peaks_p, 4.819, hw_peaks_p))
#     file_out.write('guess %_6 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(5.550, hw_peaks_p, 5.550, hw_peaks_p))
#     file_out.write('guess %_9 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(7.873, hw_peaks_p, 7.873, hw_peaks_p))
#     file_out.write('guess %_12 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.202, hw_peaks_p, 9.202, hw_peaks_p))
#     file_out.write('guess %_15 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9.637, hw_peaks_p, 9.637, hw_peaks_p))
#     file_out.write('guess %_18 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(11.111, hw_peaks_p, 11.111, hw_peaks_p))
#     file_out.write('guess %_21 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.125, hw_peaks_p, 12.125, hw_peaks_p))
#     file_out.write('guess %_24 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12.441, hw_peaks_p, 12.441, hw_peaks_p))
#     file_out.write('guess %_27 = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(13.626, hw_peaks_p, 13.626, hw_peaks_p))
#     file_out.write('guess %_30 = Polynomial6\n')


# new-er way
# def add_ge1_ss316_2022_CeO_10deg_peaks(f):
#     hw_peaks_p = 0.100
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(3, 3.105, hw_peaks_p, 3.105, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(6, 3.576, hw_peaks_p, 3.576, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(9, 5.076, hw_peaks_p, 5.076, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(12, 5.948, hw_peaks_p, 5.948, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(15, 6.227, hw_peaks_p, 6.227, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(18, 7.169, hw_peaks_p, 7.169, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(21, 7.832, hw_peaks_p, 7.832, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(24, 8.023, hw_peaks_p, 8.023, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(27, 8.791, hw_peaks_p, 8.791, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(30, 9.332, hw_peaks_p, 9.332, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(33, 10.151, hw_peaks_p, 10.151, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(36, 10.605, hw_peaks_p, 10.605, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(39, 10.779, hw_peaks_p, 10.779, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(42, 11.355, hw_peaks_p, 11.355, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(45, 11.774, hw_peaks_p, 11.774, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(48, 11.913, hw_peaks_p, 11.913, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(51, 12.436, hw_peaks_p, 12.436, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(54, 12.838, hw_peaks_p, 12.838, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(57, 12.960, hw_peaks_p, 12.960, hw_peaks_p))
#     f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'.format(60, 13.448, hw_peaks_p, 13.448, hw_peaks_p))
#     f.write('guess %_{} = Polynomial6\n'.format(63))


# newest way
def add_ge1_ss316_2022_CeO_10deg_peaks(f):
    peaks_list_p = [3.105, 3.576, 5.076, 5.948, 6.227, 7.169, 7.832, 8.023, 8.791, 9.332, 10.151, 10.605, 10.779,
                    11.355, 11.774, 11.913, 12.436, 12.838, 12.960, 13.448]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))


# APS-HX-april-2023
def add_hx_april_2023_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.350 and x < 17.500)'
    zoom_val = 'plot [4.300:17.550] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 12 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.400, 5.064, 5.263, 5.844, 7.500, 8.066, 8.872, 9.362, 9.441, 9.785, 10.803, 11.252,
                            11.768, 12.588, 13.289, 13.804, 14.188, 14.611, 16.158, 16.938, 17.4]

    list_of_bckgrd_pts_y_p = [0.129]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_hx_april_2023_peaks(f):
    peaks_list_p = [4.800, 5.527, 7.841, 9.216, 9.613, 11.067, 12.085, 12.376, 13.580, 14.426, 16.409, 16.647]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))


# Ce0_0007_10degcake_ge2_aps2022_triangles
def add_ge2_ss316_2022_CeO_10deg_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 2.700 and x < 13.650)'
    zoom_val = 'plot [2.65:13.70] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 19 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [2.843, 3.355, 3.512, 3.820, 5.000, 5.477, 5.739, 5.963, 6.259, 6.311, 6.537, 7.215,
                            7.545, 7.900, 8.157, 8.415, 8.884, 9.197, 9.483, 9.753, 10.310, 10.605, 10.814, 11.214,
                            11.544, 11.822, 12.014, 12.396, 12.674, 12.918, 13.074, 13.474, 13.647]

    list_of_bckgrd_pts_y_p = [860]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge2_ss316_2022_CeO_10deg_peaks(f):
    peaks_list_p = [3.199, 3.686, 5.233, 6.137, 6.381, 7.389, 8.050, 8.276, 9.058, 9.597, 10.466, 10.918, 11.092,
                    11.701, 12.135, 12.257, 12.813, 13.196, 13.335]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))


# Ce0_0007_10degcake_ge2_aps2022_triangles
def add_ge3_ss316_2022_CeO_10deg_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 2.700 and x < 13.600)'
    zoom_val = 'plot [2.65:13.65] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 19 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [2.843, 3.355, 3.512, 3.820, 5.000, 5.477, 5.739, 5.963, 6.259, 6.311, 6.537, 7.215,
                            7.545, 7.900, 8.157, 8.415, 8.884, 9.197, 9.483, 9.753, 10.310, 10.605, 10.814, 11.214,
                            11.544, 11.822, 12.014, 12.396, 12.674, 12.918, 13.074, 13.474, 13.647]

    list_of_bckgrd_pts_y_p = [860]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_ge3_ss316_2022_CeO_10deg_peaks(f):
    peaks_list_p = [3.199, 3.686, 5.216, 6.12, 6.381, 7.32, 8.050, 8.241, 9.041, 9.597, 10.449, 10.918, 11.092,
                    11.701, 12.101, 12.257, 12.813, 13.196, 13.335]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))


# LANL_STEEL_DATA_JAN_2023 - Si instrumenttal
def add_LANL_STEEL_2023_Si_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4 and x < 14.600)'
    zoom_val = 'plot [3.95:14.65] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 14 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.005, 5.000, 5.493, 5.910, 6.345, 7.266, 7.579, 7.927, 8.274, 8.9, 9.265, 9.491, 9.839, 10.343,
                            10.656, 10.829, 11.160, 11.577, 11.89, 12.046, 12.307, 12.759, 13.000, 13.124, 13.437, 13.698,
                            14.045, 14.150, 14.445, 14.595]

    list_of_bckgrd_pts_y_p = [1.19]  # have to put a guess for the first point's height, fityk won't accept a calculated first value
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_LANL_STEEL_2023_Si_peaks(f):
    peaks_list_p = [5.267, 6.171, 7.440, 8.100, 9.109, 9.665, 10.534, 11.021, 11.768, 12.203, 12.898, 13.298, 13.924, 14.306]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window - HAVE TO PUT DIFFERENTLY FOR SplitPseudoVoigt
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))


# APS-HX-april-2023 >>>>>>>>>>>>>>>>>>>>>>> 14-apr-2023/dt_hu_1/K-converted >>>>>>>>> this is an SS316L sample
def add_hx_april_2023_dt_hu_1_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.500 and x < 13.000)'
    zoom_val = 'plot [4.495:13.005] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 8 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.510, 4.590, 5.042, 5.320, 5.842, 5.945, 6.642, 7.426, 8.141,
                            8.838, 9.352, 9.500, 9.937,
                            10.791, 11.366, 11.802, 12.726, 12.990]

    list_of_bckgrd_pts_y_p = [0.320]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_hx_april_2023_dt_hu_1_peaks(f):
    peaks_list_p = [4.813, 5.553, 7.867, 9.216, 9.626, 11.120, 12.118, 12.431]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))


# lab6 scan for the same dataset
def add_hx_april_2023_lab6_1_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.500 and x < 13.25)'
    zoom_val = 'plot [4.495:13.255] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 23 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.553, 4.715, 4.877, 5.239, 5.464, 5.788, 6.000, 6.674, 6.873, 7.110, 7.285, 7.497, 7.659,
                            7.859, 8.046, 8.233, 8.395, 8.570, 8.732, 8.907, 9.069, 9.493, 9.668, 9.792, 9.980, 10.117,
                            10.254, 10.379, 10.541, 10.666, 10.803, 10.928, 11.065, 11.202, 11.339, 11.676, 11.826,
                            11.926, 12.050, 12.163, 12.325, 12.412, 12.537, 12.849, 12.998, 13.073, 13.240]

    list_of_bckgrd_pts_y_p = [1.4]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_hx_april_2023_lab6_1_peaks(f):
    peaks_list_p = [4.799, 5.367, 5.872, 6.781, 7.198, 7.589, 7.956, 8.309, 8.650, 8.979, 9.597, 9.900, 10.178, 10.469,
                    10.734, 10.999, 11.264, 11.757, 12.009, 12.249, 12.476, 12.931, 13.146]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))


# lab6 scan for APS-HX-2022
def add_hx_april_2022_lab6_2_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.500 and x < 13.25)'
    zoom_val = 'plot [4.495:13.255] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 23 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.553, 4.715, 4.877, 5.239, 5.464, 5.788, 6.000, 6.674, 6.873, 7.110, 7.285, 7.497, 7.659,
                            7.859, 8.046, 8.233, 8.395, 8.570, 8.732, 8.907, 9.069, 9.493, 9.668, 9.792, 9.980, 10.117,
                            10.254, 10.379, 10.541, 10.666, 10.803, 10.928, 11.065, 11.202, 11.339, 11.676, 11.826,
                            11.926, 12.050, 12.163, 12.325, 12.412, 12.537, 12.849, 12.998, 13.073, 13.240]

    list_of_bckgrd_pts_y_p = [1.4]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))

    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_hx_april_2022_lab6_2_peaks(f):
    peaks_list_p = [4.799, 5.367, 5.872, 6.781, 7.198, 7.589, 7.956, 8.309, 8.650, 8.979, 9.597, 9.900, 10.178, 10.469,
                    10.734, 10.999, 11.264, 11.757, 12.009, 12.249, 12.476, 12.931, 13.146]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))


# Cu test data neutron 2024 - for paper
def add_cu_test_data_neutron_poly_info():
    # SET ACTIVE RANGE
    active_range_val = 'A = (x > 4.000 and x < 15.000)'
    zoom_val = 'plot [3.995:15.005] []'
    # SET NUMBER OF PEAKS TO EVALUATE
    include_polynomial6 = True
    num_peaks = 10 + 1  # + 1 if include_polynomial6 = True, + 0 if include_polynomial6 = False
    # SET BACKGROUND
    list_of_bckgrd_pts_p = [4.005, 4.269, 4.574, 5.023, 5.310, 5.740, 6.727, 7.552, 8.090, 8.897, 9.794, 10.835, 11.283,
                            11.821, 12.628, 13.256, 13.776, 14.063, 14.691, 14.995]

    list_of_bckgrd_pts_y_p = [0.166]
    half_window_p = 0.025
    divs_p = 4
    background_val = bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p)))
    # SET PEAK TYPES
    peak_types_p = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0'  # 0 = SP7, 1 = SPV
    return active_range_val, zoom_val, background_val, num_peaks, include_polynomial6, peak_types_p


def add_cu_test_data_neutron_peaks(f):
    peaks_list_p = [4.772, 5.543, 7.821, 9.166, 9.597, 11.050, 12.054, 12.359, 13.543, 14.368]
    hw_peaks_p = [0.100] * len(peaks_list_p)  # list of windows of identical size

    # position, center, left window, center, right window
    for pos, peak in enumerate(peaks_list_p):
        f.write('guess %_{} = SplitPearson7 [({} - {}) : ({} + {})]\n'
                .format(3 * pos + 3, peak, hw_peaks_p[pos], peak, hw_peaks_p[pos]))
    f.write('guess %_{} = Polynomial6\n'.format(3 * len(peaks_list_p) + 3))
