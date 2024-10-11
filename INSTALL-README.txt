WINDOWS 10 INSTALLATION INSTRUCTIONS:

install fityk-1.3.1-setup.exe in any location of choice, leave the name as "Fityk".

ensure that you have python 3.7 or python 3.8 installed (may work on other versions, not tested).

you will need to be able to edit/run python scripts, so grab your IDE of choice, I use PyCharm. Create a project/add a folder to your path that "fitpyk-2023-dec" can live in.

extract "fitpyk-2023-dec" to this same location of choice. I use 7Zip.

open up start menu, type "fit" or "fityk", check which one makes the "Fityk" program show up, not the "Fityk CLI" program. Record what this string is.

when you find which string is better, open up "fitpyk_fityk_controller_V2.py" inside your IDE, find the function "type_fityk_string", and change the value of the keyboard_p.type('fityk') string to be either 'fit' or 'fityk' as needed.

now open up "_script_47939.fit", on the first line, edit the path to match the path in your installation.

open up fityk, go to file > execute script. navigate to the "_script_47939.fit" file and execute it, you should see a poorly fit file. This ensures that fityk is primed to execute scripts from the correct folder.

open up "fitpyk_user_interface_APS_triangles_2023.py", change the base_path to the place that fitpyk-2023-dec is installed in, eg: "P:/PyCharmProjectsP/botting/venv/fitpyk-2023-dec/", including the fitpyk-2023-dec folder itself. This is the base path of the scripts.

change the storage_dir_name to '_results_2/'