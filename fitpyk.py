from fitpyk_engine_V10 import *  # V7 last stable
import config
from fitpyk_display_logo_V1 import *  # can uncomment if you don't want logo displayed

# Known bugs:
# BUG 1:
# If "failed to run recursively", then the file run is not removed and fityk stays open -> should restart the call from
# current location instead of stepping forwards by 1
# BUG 2:
# if both the second last and last files fail, code errors out
# BUG 3:
# no simple method to call fitpyk on a single file, e.g. minimum number of patterns is 2
# BUG 4:
# if cleanup fails, cleanup should be called a second time to clear the files in the main directory so program can keep
# running

def fitpyk(base_path, data_directory, storage_directory_name, filename_prefix, filename_spacer,
                          filename_suffix, data_type, z_fill, first_file, number_of_spectra,
                          max_fitpyk_iterations, results_filename, info, peaks):

    # display fitPyk logo
    image_path = "fitPyk.jpeg"
    fitpyk_display_image(image_path)

    # rest of code
    os.system('color')

    config.returnpackage = [first_file, number_of_spectra]

    print('\033[34m' + 'fitting start.' + '\033[0m')

    while len(config.returnpackage) == 2 and config.returnpackage[1] > 1:
        # print('fitting with polynomial background')
        # print(config.returnpackage)
        # print(f'fitting patterns {config.returnpackage[0]} - {config.returnpackage[0] + config.returnpackage[1] - 1}.', end=' ')
        run_fitpyk_engine(base_path, data_directory, storage_directory_name, filename_prefix, filename_spacer,
                          filename_suffix, data_type, z_fill, config.returnpackage[0], config.returnpackage[1],
                          max_fitpyk_iterations, results_filename, info, peaks)

        try:
            config.returnpackage[0] += 1
            config.returnpackage[1] -= 1

            print('\033[31m' + f'file {config.returnpackage[0] - 1} failed.' + '\033[0m')  # '\033[91m' <- light red

        except IndexError:
            # print('list index out of range')
            # print('fitting complete')
            pass
        # print(config.returnpackage)
        # print(len(config.returnpackage))

    # print(config.returnpackage)
    # print(len(config.returnpackage))
    # print('')
    # print('fitting complete.')

    # -------------- check to make sure the final result matches the final file number --------------
    # check for the last file number in K_results_2
    # print(config.finalspectrainfo)

    if len(config.finalspectrainfo) > 0:
        last_file_equal_max_file = fitpyk_check_last_spectra(config.finalspectrainfo[0], config.finalspectrainfo[1], (config.finalspectrainfo[1] + config.finalspectrainfo[2]), config.finalspectrainfo[3], config.finalspectrainfo[4])
        # print(last_file_equal_max_file)

        # does last file number == final file number, yes -> do nothing, no ->
        if last_file_equal_max_file == 'passed':
            pass
        else:
            # print('rename stuff and move stuff to failed folder (make failed folder if not exist)')
            # print('failed file is: {}'.format(last_file_equal_max_file + 1))
            # add file to failed file directory
            # does failed folder exist? if no, make failed folder. if yes -> fitpyk_failed_file_copier

            fixed_filename_prefix_p, script_name_p, fixed_script_name_p, pretext_filename_p, fixed_filename_p, bool_filename_p, storage_destination_p = fitpyk_file_backend(
                filename_prefix, results_filename, data_directory, storage_directory_name)
            directory_fail_p = storage_destination_p + 'failed/'
            if not os.path.exists(directory_fail_p):
                try:
                    os.makedirs(directory_fail_p)
                except:
                    print('could not create failed files directory.')
            fitpyk_failed_file_copier(base_path, data_directory, storage_directory_name, filename_prefix,
                                      filename_spacer, (last_file_equal_max_file + 1), z_fill, filename_suffix, data_type)

            # change name of folder that has K_results_2 from (x)-(y) to (x)-(y-1)
            # print(config.finalspectrainfo[5])
            original_final_storage_location = config.finalspectrainfo[5] + '{}'.format(config.finalspectrainfo[1]) + '-' + '{}'.format(config.finalspectrainfo[1] + config.finalspectrainfo[2] - 1) + '/'
            # print(original_final_storage_location)
            modified_final_storage_location = config.finalspectrainfo[5] + '{}'.format(config.finalspectrainfo[1]) + '-' + '{}'.format(config.finalspectrainfo[1] + config.finalspectrainfo[2] - 2) + '/'
            # print(modified_final_storage_location)
            os.rename(original_final_storage_location, modified_final_storage_location)
            # print('renamed final file directory.')
            print('\033[31m' + f'file {config.finalspectrainfo[1] + config.finalspectrainfo[2] - 1} failed.' + '\033[0m', end=' ')

    print('')
    print('\033[34m' + 'fitting complete.' + '\033[0m')

if __name__ == "__main__":
    pass
