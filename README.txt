###############################################################################

to install:
- required non standard python packages: numpy, pandas, pynput, psutil, matplotlib
- need fityk 1.3.1

- optional packages for logo display: pillow, tk
- the logo is included so the user knows the program is running and can easily be removed
don't want the logo:
- comment out lines 3, 22, 23 in fitpyk.py
- comment out lines 21, 75, 76 in fitpyk_dev.py

###############################################################################

if you need to stop fitting:

- end your program while fityk is open and fitting, then close fityk. this will be the easiest way

common bugs and fixes:

- if fityk cannot run because windows is not opening it in the start menu, change the string in line 24 of fitpyk_fityk_controller_V2.py to match a string that shows fityk in your start menu
- if fityk cannot run your script because the script does not exist, uncomment line 84 in fitpyk_fityk_controller_V2.py
- if fityk cannot run because of timing issues, you can change the values of lines 8 and 9 in fitpyk_engine_V10.py

program crashes during a run:

- delete the most recent XXX-YYY filenumber section of the run that is incomplete, and rerun your user interface script from the XXX pattern number

fitPyk cannot detect that fityk is finished:

- change the threshold value from the default of 20, in line 149 of fitpyk_process_monitor_V6.py

###############################################################################

in MuranskyCode:

###############################################################################

in fitpyk-2024-jun:
run one of the convert_tth_to_k_ .py scripts
	dat
	dat_multi
	fxye
	fyxe_multi
	xye
	xye_multi

run patterns (fitpyk_user_interface_Cu_test_data_neutron_2024_v3.py)

run instrumentals (fitpyk_user_interface_Cu_test_data_neutron_2024_inst_V1.py)  # IF YOU HAVE INSTRUMENTALS DO THIS STEP

run instrumentals_from_results_316L_APS_triangles_2022.py  # IF YOU HAVE INSTRUMENTALS DO THIS STEP
	check for outliers
	get polynomial factors > put back into script
	put peak positions
	get output instrumental fwhms > put into background_subtractor_gaussian_

run fitpyk_result_compiler_V3.py
    make sure line 34 has the same letter in the check as your drive, e.g. "C" for C: drive base_path

run wh_plotting_from_results_Cu_test_data_neutron_2024_V1.py
	make sure startpattern, numrows, numcols are the correct numbers, as well as the meshgrid
	you will have to edit values in these line ranges: basic info: [375 - 390], pattern/mesh numbers: [667-669], meshgrid dimensions: [689-690], min/max vals for plotting: 712, plot title: 766

	run this over and over again, increasing from 2% up to the highest value (10%) you need for each peak
	make sure you set the print_to_file_flag when you get a good picture
	manually stitch all of the outputs together (...-allpeaks.txt file)
	save all the files back into your results folder and delete them from your fitpyk base path
	you should record your peak window file names and error values used in a log file, as you will use these later (windows for fitting and err for publications).

run background_subtractor_gaussian_Cu_test_data_2024.py
	make sure you have the right peak windows
	make sure you have the right instrumental widths, with correct polynomial [CONSIDER UPDATING POLYNOMIAL AUTOMATICALLY]
	update the info name on line 146
	make sure you change the output file name in both places to the new name you need

    if you want to get the delta centre values, run background_subtractor_gaussian_Cu_test_data_2024_V2.py
        produce a _del_cen.txt version of the normal "_to_mwh_optimize.txt"


run mwh_optimize_V8_Cu_test_data_2024.py
	make sure you change the input and output file names to the correct ones
	************ ADD THE SCRIPTS FROM THE VIRTUAL MACHINE TO HERE TO CALC ChOO and q **************************

run mwh_output_plotting_GE1_APS_triangles_2022_V3.py
	make sure you choose the correct start and end to each row for the plotting process
	set the write to file portion of the code on or off depending if you need for panel combiner

run GE_mwh_panel_combiner_SS316L_APS_triangles_2022_V2.py
	(YOU CAN USE V5 WHICH HAS MASKING/AVERAGING CAPABILITIES)
	make sure to use the right meshgrid

in cmwp-instrumental-script folder:
	in NEW_p7_split-p7:
create a instrumental.sh for your dataset
    WHEN YOU MAKE THE INSTRUMENTAL.SH MAKE SURE YOU USE THE RIGHT PEAK WIDTH AND NUMBER OF POINTS TO HAVE MUCH GREATER THAN 10 OVER THE FWHM
    for each peak run instrumentals_from_results_316L_APS_triangles_2022.py with different parameters needed (LHWHM, RHWHM, LS, RS)
    construct an instrumental peak for each point in your dataset
        use a polynomial for LHWHM and RHWHM and a mean for Lshape and Rshape (unless there's a clear trend)

run your new instrumental.sh
    send each of the number files over to your linux machine

on linux machine:

transfer some files to your CMWP data location
store the number files in an instrumental folder
go in the instrumental folder on linux and run 'dos2unix *'

back on the windows machine:

run mwh-to-cmwp-conversion_APS_triangles_2022.py
    put in the values that are obtained from CMWP and your mwh_optimize_V8_ss316l_triangles_2022.py
