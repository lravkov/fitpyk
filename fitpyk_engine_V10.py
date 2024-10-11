from fitpyk_dev import *
import config


def run_fitpyk_engine(base_path_p, data_directory_p, storage_directory_name_p, filename_prefix_p, filename_spacer_p, filename_suffix_p, data_type_p, z_fill_p, first_file_p, number_of_spectra_p, max_fitpyk_iterations_p, results_filename_p, add_generic_info_p, add_generic_peaks_p):
    # USES FITYK 1.3.1 :: available in google drive :: fitpyk_backup_mar17_2022
    # these delay values should work for most modern PCs
    initial_delay_p = 1
    delay_p = 0.1

    print(f'fitting files {config.returnpackage[0]} - {config.returnpackage[0] + config.returnpackage[1] - 1}.', end=' ')

    # filename pre work
    fixed_filename_prefix_p, script_name_p, fixed_script_name_p, pretext_filename_p, fixed_filename_p, bool_filename_p, storage_destination_p = fitpyk_file_backend(filename_prefix_p, results_filename_p, data_directory_p, storage_directory_name_p)

    # directory pre work
    directory_p = base_path_p + storage_destination_p + '{}'.format(first_file_p) + '-' + '{}'.format(first_file_p + number_of_spectra_p - 1) + '/'
    if not os.path.exists(directory_p):
        os.makedirs(directory_p)
    directory_copy_p = storage_destination_p + '{}'.format(first_file_p) + '-' + '{}'.format(first_file_p + number_of_spectra_p - 1) + '/'
    directory_fail_p = storage_destination_p + 'failed/'

    for i in range(max_fitpyk_iterations_p):

        if i == 0:  # SETUP - DO INITIAL FIT WITHOUT CONSTRAINTS
            # GENERATE INITIAL FITYK SCRIPT
            # might need to change: add_generic_info_p, add_generic_peaks_p to add_cu_neutron_poly_info, add_cu_neutron_poly_peaks
            include_poly6_p, num_peaks_p = generate_initial_fityk_script_poly(filename_prefix_p, results_filename_p, pretext_filename_p,
                                                                              add_generic_info_p, add_generic_peaks_p,
                                                                              first_file_p, number_of_spectra_p, data_directory_p, data_type_p,
                                                                              z_fill_p, filename_suffix_p, filename_spacer_p)

            # RUN FITYK WITH INITIAL FITYK SCRIPT
            run_and_monitor_fityk(script_name_p, delay_p, initial_delay_p)  # close after fityk completes fitting

            # used storage destination before
            try:
                script_pass = fitpyk_copy_file(script_name_p + '.fit', base_path_p, directory_copy_p, i)
            except:
                # print('location already exists')
                pass

            result_pass = fitpyk_copy_file(results_filename_p, base_path_p, directory_copy_p, i)
            if result_pass == 0:
                # print('no result file.')

                # RUN CLEANUP
                fitpyk_cleanup(results_filename_p, fixed_filename_p, bool_filename_p, pretext_filename_p, script_name_p, fixed_script_name_p)

                #  add file to failed file directory
                if not os.path.exists(directory_fail_p):
                    try:
                        os.makedirs(directory_fail_p)
                    except:
                        print('could not create failed files directory.')
                bad_spectra_p = config.returnpackage[0]
                fitpyk_failed_file_copier(base_path_p, data_directory_p, storage_directory_name_p, filename_prefix_p,
                                          filename_spacer_p,
                                          bad_spectra_p, z_fill_p, filename_suffix_p, data_type_p)

                #  remove directory of failed run
                # print('directory')
                mydir_p = base_path_p + directory_copy_p
                # print(base_path_p + directory_copy_p)

                try:
                    shutil.rmtree(mydir_p)
                except OSError as e_p:
                    print("Error: %s - %s." % (e_p.filename, e_p.strerror))

                # print('---------')

                break

        if i != 0:  # FILE CLEANUP THAT HAPPENS ONLY AFTER THE FIRST RUN OF MAIN ENGINE LOOP
            fixed_script_pass = fitpyk_copy_and_delete_file(fixed_script_name_p + '.fit', base_path_p, directory_copy_p, i)
            fixed_filename_pass = fitpyk_copy_and_delete_file(fixed_filename_p, base_path_p, directory_copy_p, i)
            bool_pass = fitpyk_copy_and_delete_file(bool_filename_p, base_path_p, directory_copy_p, i)
            if fixed_script_pass == 0 or fixed_filename_pass == 0 or bool_pass == 0:
                print('no file for [fixed_script], [fixed_filename], [bool]: ' + fixed_script_pass + ', ' + fixed_filename_pass + ', ' + bool_pass)

                # RUN CLEANUP
                fitpyk_cleanup(results_filename_p, fixed_filename_p, bool_filename_p, pretext_filename_p, script_name_p, fixed_script_name_p)

                #  add file to failed file directory
                if not os.path.exists(directory_fail_p):
                    try:
                        os.makedirs(directory_fail_p)
                    except:
                        print('could not create failed files directory.')
                bad_spectra_p = config.returnpackage[0]
                fitpyk_failed_file_copier(base_path_p, data_directory_p, storage_directory_name_p, filename_prefix_p,
                                          filename_spacer_p,
                                          bad_spectra_p, z_fill_p, filename_suffix_p, data_type_p)

                #  remove directory of failed run
                # print('directory')
                mydir_p = base_path_p + directory_copy_p
                # print(base_path_p + directory_copy_p)

                try:
                    shutil.rmtree(mydir_p)
                except OSError as e_p:
                    print("Error: %s - %s." % (e_p.filename, e_p.strerror))

                # print('---------')

                break

        # MAIN ENGINE LOOP
        try:
            # works for both SP7 and SPV
            identify_and_fix_values(results_filename_p, fixed_filename_p, bool_filename_p, first_file_p, number_of_spectra_p,
                                    pretext_filename_p, filename_prefix_p, include_poly6_p)
        except:
            # print('identify and fix failed on iter {}'.format(i))
            pass

        try:
            # take spectra that have  been fixed to realistic values and convert back into fityk scripting language
            parse(bool_filename_p, pretext_filename_p, fixed_filename_p, first_file_p, number_of_spectra_p, fixed_filename_prefix_p,
                  filename_prefix_p, results_filename_p, include_poly6_p, data_directory_p, data_type_p, z_fill_p, filename_suffix_p,
                  filename_spacer_p)
        except:
            # print('parse failed on iter {}'.format(i))
            pass

        # CHECK TO SEE THAT A FIXED SCRIPT EXISTS
        # print(fixed_script_name_p)

        if os.path.exists(base_path_p + fixed_script_name_p + '.fit'):
            # print('fixed script exists')  # if it does continue on
            pass
        else:
            # print('fixed script does not exist')  # if it does not then clean up and break code
            # RUN CLEANUP
            fitpyk_cleanup(results_filename_p, fixed_filename_p, bool_filename_p, pretext_filename_p, script_name_p, fixed_script_name_p)
            # print(first_file_p, number_of_spectra_p)
            return_list_p = [first_file_p, number_of_spectra_p]
            config.returnpackage = return_list_p
            # print(config.returnpackage)

            #  add file to failed file directory
            if not os.path.exists(directory_fail_p):
                try:
                    os.makedirs(directory_fail_p)
                except:
                    # print('could not create failed files directory.')
                    pass
            bad_spectra_p = config.returnpackage[0]
            fitpyk_failed_file_copier(base_path_p, data_directory_p, storage_directory_name_p, filename_prefix_p,
                                      filename_spacer_p,
                                      bad_spectra_p, z_fill_p, filename_suffix_p, data_type_p)

            #  remove directory of failed run
            # print('directory')
            mydir_p = base_path_p + directory_copy_p
            # print(base_path_p + directory_copy_p)

            try:
                shutil.rmtree(mydir_p)
            except OSError as e_p:
                print("Error: %s - %s." % (e_p.filename, e_p.strerror))

            # print('---------')

            break

        # RUN FITYK WITH THE NEW FIXED FITYK SCRIPT
        if i != (max_fitpyk_iterations_p - 1):  # runs every time but the last time
            run_and_monitor_fityk(fixed_script_name_p, delay_p, initial_delay_p)  # close after fityk completes fitting

        if i == (max_fitpyk_iterations_p - 1):  # runs the last time
            run_and_monitor_fityk(fixed_script_name_p, delay_p, initial_delay_p)  # close

            result_pass = fitpyk_copy_file(results_filename_p, base_path_p, directory_copy_p, i)

            # new stuff
            fitpyk_copy_pretext(base_path_p, pretext_filename_p, directory_copy_p)

            # check the results_filename_p script for the furthest number it got to, return that + 2, run engine
            # between that number and the end
            last_good_spectra_p = fitpyk_check_last_spectra(results_filename_p, first_file_p, first_file_p + number_of_spectra_p - 1,
                                                          num_peaks_p, include_poly6_p)

            if last_good_spectra_p == first_file_p + number_of_spectra_p - 1:
                # print('passed all')

                # RUN CLEANUP
                fitpyk_cleanup(results_filename_p, fixed_filename_p, bool_filename_p, pretext_filename_p, script_name_p, fixed_script_name_p)

            else:
                # print('did not pass all')
                try:
                    bad_spectra_p = last_good_spectra_p + 1
                except TypeError:
                    # print('finished')
                    pass
                else:
                    # print('bad spectra: {}'.format(bad_spectra_p))
                    # print(f'file {bad_spectra_p} failed.')

                    new_first_file_p = last_good_spectra_p + 2
                    # print('new first file: {}'.format(new_first_file_p))
                    new_number_of_spectra_p = first_file_p + number_of_spectra_p - last_good_spectra_p - 2
                    # print('new number of spectra: {}'.format(new_number_of_spectra_p))
                    # print(f'fitting patterns {new_first_file_p} - {new_first_file_p + new_number_of_spectra_p - 1}.', end=' ')
                    updated_directory_name_p = base_path_p + storage_destination_p + '{}'.format(first_file_p) + '-' + '{}'.format(
                        last_good_spectra_p) + '/'
                    os.rename(directory_p, updated_directory_name_p)

                    # put the bad spectra in the failed file folder
                    if not os.path.exists(directory_fail_p):
                        try:
                            os.makedirs(directory_fail_p)
                        except:
                            print('could not create failed files directory.')
                    fitpyk_failed_file_copier(base_path_p, data_directory_p, storage_directory_name_p, filename_prefix_p, filename_spacer_p,
                                              bad_spectra_p, z_fill_p, filename_suffix_p, data_type_p)

                # check if we are trying to fit outside of the list
                try:
                    temp_test_p = new_first_file_p
                except UnboundLocalError:
                    new_first_file_p = first_file_p
                    new_number_of_spectra_p = number_of_spectra_p + 1  # this causes the if to run, rather than the else

                if new_first_file_p + new_number_of_spectra_p - 1 > first_file_p + number_of_spectra_p - 1:
                    # run cleanup
                    fitpyk_cleanup(results_filename_p, fixed_filename_p, bool_filename_p, pretext_filename_p, script_name_p, fixed_script_name_p)
                    config.returnpackage = []

                    # APR-5-2022 edit to detect if final spectra is failed
                    temp_split_results_filename_p = results_filename_p.split('.')
                    final_results_filename_p = temp_split_results_filename_p[0] + '_' + str(max_fitpyk_iterations_p - 1) + '.' + temp_split_results_filename_p[1]
                    final_directory_name_p = base_path_p + storage_destination_p + '{}'.format(new_first_file_p) + '-' + '{}'.format(new_first_file_p + new_number_of_spectra_p - 2) + '/'
                    final_storage_without_numbers_p = base_path_p + storage_destination_p
                    final_results_p = final_directory_name_p + final_results_filename_p
                    config.finalspectrainfo = [final_results_p, new_first_file_p, new_number_of_spectra_p - 1, num_peaks_p,
                                               include_poly6_p, final_storage_without_numbers_p]

                    # print('done')
                else:
                    # run cleanup
                    fitpyk_cleanup(results_filename_p, fixed_filename_p, bool_filename_p, pretext_filename_p, script_name_p, fixed_script_name_p)

                    # rerun the same entire engine but only for new_first_file_p : end
                    # print('run it again')
                    # print('new first file: ' + str(new_first_file_p))
                    # print('new number of spectra: ' + str(new_number_of_spectra_p))
                    config.returnpackage = [new_first_file_p, new_number_of_spectra_p]  # MAR-17-2022 edit to fix errors

                    # APR-5-2022 edit to detect if final spectra is failed
                    temp_split_results_filename_p = results_filename_p.split('.')
                    final_results_filename_p = temp_split_results_filename_p[0] + '_' + str(max_fitpyk_iterations_p - 1) + '.' + temp_split_results_filename_p[1]
                    final_directory_name_p = base_path_p + storage_destination_p + '{}'.format(new_first_file_p) + '-' + '{}'.format(new_first_file_p + new_number_of_spectra_p - 1) + '/'
                    final_storage_without_numbers_p = base_path_p + storage_destination_p
                    final_results_p = final_directory_name_p + final_results_filename_p
                    config.finalspectrainfo = [final_results_p, new_first_file_p, new_number_of_spectra_p, num_peaks_p, include_poly6_p, final_storage_without_numbers_p]

                    try:
                        print('\033[31m' + f'file {bad_spectra_p} failed.' + '\033[0m')  # '\033[91m' <- light red
                        run_fitpyk_engine(base_path_p, data_directory_p, storage_directory_name_p, filename_prefix_p, filename_spacer_p, filename_suffix_p, data_type_p, z_fill_p, config.returnpackage[0], config.returnpackage[1], max_fitpyk_iterations_p, results_filename_p, add_generic_info_p, add_generic_peaks_p)
                    except:
                        print('\033[33m' + 'failed to run recursively.' + '\033[0m', end=' ')  # <- light yellow

                        # RUN CLEANUP
                        fitpyk_cleanup(results_filename_p, fixed_filename_p, bool_filename_p, pretext_filename_p,
                                       script_name_p, fixed_script_name_p)

                        # print(new_first_file_p, new_number_of_spectra_p)
