from fitpyk_engine_V10 import *  # V7 last stable
import config

# Known bugs:
# If the very last pattern fails it is not logged correctly in the file structure, and not added to failed files

def fitpyk(base_path, data_directory, storage_directory_name, filename_prefix, filename_spacer,
                          filename_suffix, data_type, z_fill, first_file, number_of_spectra,
                          max_fitpyk_iterations, results_filename, info, peaks):

    config.returnpackage = [first_file, number_of_spectra]

    while len(config.returnpackage) == 2 and config.returnpackage[1] > 1:
        print('fitting with polynomial background')
        print(config.returnpackage)
        run_fitpyk_engine(base_path, data_directory, storage_directory_name, filename_prefix, filename_spacer,
                          filename_suffix, data_type, z_fill, config.returnpackage[0], config.returnpackage[1],
                          max_fitpyk_iterations, results_filename, info, peaks)

        try:
            config.returnpackage[0] += 1
            config.returnpackage[1] -= 1
        except IndexError:
            print('list index out of range')
            print('fitting complete')
        print(config.returnpackage)
        print(len(config.returnpackage))

    print(config.returnpackage)
    print(len(config.returnpackage))


if __name__ == "__main__":
    pass
