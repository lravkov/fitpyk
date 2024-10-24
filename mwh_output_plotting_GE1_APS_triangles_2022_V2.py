import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd


def get_row_b3(pnl, fwhml, startnum, endnum):
    pnl_raw = [i for i in pnl if (startnum <= i <= endnum)]
    # print(pnl_raw)

    fwhml_raw = [fwhml[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]

    logged_missing_positions = []

    # check first value
    if pnl_raw[0] == startnum:
        pass
    else:
        pnl_raw.insert(0, startnum)
        fwhml_raw.insert(0, np.NaN)
        logged_missing_positions.append(0)

    # check all values but the last one
    test_value = startnum
    for i in range(int(endnum - startnum)):
        # print(i)
        # print(pnl_raw)
        try:
            if pnl_raw[i] == test_value:
                pass
            else:
                pnl_raw.insert(i, test_value)
                fwhml_raw.insert(i, np.NaN)
                logged_missing_positions.append(i)
        except IndexError:
            pnl_raw.append(endnum)
            fwhml_raw.append(np.NaN)
            logged_missing_positions.append(int(endnum - startnum))  # int(endnum - startnum)
        test_value += 1

    # check the final value
    try:
        pnl_raw[int(endnum - startnum)]
    except IndexError:
        pnl_raw.append(endnum)
        fwhml_raw.append(np.NaN)
        logged_missing_positions.append(int(endnum - startnum))

    # fix the last patterns if the repeat near the end fail
    rlmp = logged_missing_positions[::-1]
    print(rlmp)

    if len(rlmp) > 1 and rlmp[0] == rlmp[1]:
        temp_pattern = np.NaN
        temp_pos = 0
        poss = []
        for pos, pattern in enumerate(rlmp):
            if pattern != temp_pattern:
                temp_pattern = pattern
                # print(f'{pattern}, {pos}')
                poss.append(pos)
                # for i in range(temp_pos, pos):
                #     if i == temp_pos:
                #         print(rlmp[i])
        # print(poss)

        rpnl_raw = pnl_raw[::-1]
        for i in range(0, poss[1]):
            # print(int(endnum - startnum - i))
            rlmp[i] = int(endnum - startnum - i)
            rpnl_raw[i] = rpnl_raw[i] - i
        # print(rlmp)
        # print(rpnl_raw)
        logged_missing_positions = rlmp[::-1]
        pnl_raw = rpnl_raw[::-1]

    return pnl_raw, fwhml_raw, logged_missing_positions


if __name__ == "__main__":
    # ------------------------------------------- MAIN INPUTS --------------------------------------------------------
    inputfile = 'GE2_APS316Ltriangles_2022_mwh_output_edited.txt'

    startpattern = 1558  # 43 for hypotenuse up triangles
    numrows = 27
    numcols = 56
    prefix = 'Hypotenuse Down 1'
    suffix = 'GE2'

    plottingthis = 'rho'  # csds, rho, q

    writeflag = False
    filelocation = 'D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hd_1_4permm2/'

    # also might have to mess with the z_length and x, y meshgrids

    # ----------------------------------------- END MAIN INPUTS ------------------------------------------------------

    df = pd.read_csv(inputfile)
    patterns = df.iloc[:, 0]
    infos = df.iloc[:, 1]
    results = df.iloc[:, 2]

    # print(results)

    # separate results into the 3 sections [grainSize, rho, q]
    gss = []
    rhos = []
    qs = []
    for result in results:
        # remove the square brackets from raw results
        result = result[2:]
        result = result[:-1]

        # split results and append the float of each result to the corresponding list
        three_results = result.split(' ')
        gss.append(float(three_results[0]))
        rhos.append(float(three_results[1]))
        qs.append(float(three_results[2]))
        # print(three_results)
    # print(gss)
    # print(rhos)
    # print(qs)

    # find all the indices of patterns that repeat, so we can average the results
    patternas = []
    gsas = []
    rhoas = []
    qas = []

    temp_pattern = np.NaN
    temp_pos = 0
    for pos, pattern in enumerate(patterns):
        if pattern != temp_pattern:
            temp_pattern = pattern
            # print(f'{pattern}, {pos}')

            # averaging occurs in here
            temp_gs = []
            temp_rho = []
            temp_q = []
            for i in range(temp_pos, pos):
                if i == temp_pos:
                    # print(patterns[i])
                    patternas.append(patterns[i])
                # print(i)
                temp_gs.append(gss[i])
                temp_rho.append(rhos[i])
                temp_q.append(qs[i])
            # print(temp_gs)
            # print(temp_rho)
            # print(temp_q)
            gsas.append(np.nanmean(temp_gs))
            rhoas.append(np.nanmean(temp_rho))
            qas.append(np.nanmean(temp_q))

            temp_pos = pos
    # print(patternas)
    # print(len(patternas))
    gsas = gsas[1:]
    # print(gsas)
    # print(len(gsas))
    rhoas = rhoas[1:]
    # print(rhoas)
    # print(len(rhoas))
    qas = qas[1:]
    # print(qas)
    # print(len(qas))

    # MISSING THE LAST SET OF PATTERNS SO DO IT IN REVERSE AND THEN ADD THE FIRST RESULT TO THE END OF THE PREVIOUS SET
    # OF RESULTS
    rpatterns = patterns.values.tolist()[::-1]  # have to do this cause it's a pd.df
    rgss = gss[::-1]
    rrhos = rhos[::-1]
    rqs = qs[::-1]

    patternas2 = []
    gsas2 = []
    rhoas2 = []
    qas2 = []

    temp_pattern = np.NaN
    temp_pos = 0
    for pos, pattern in enumerate(rpatterns):
        if pattern != temp_pattern:
            temp_pattern = pattern
            # print(f'{pattern}, {pos}')

            # averaging occurs in here
            temp_gs = []
            temp_rho = []
            temp_q = []
            for i in range(temp_pos, pos):
                if i == temp_pos:
                    # print(rpatterns[i])
                    patternas2.append(rpatterns[i])
                # print(i)
                temp_gs.append(rgss[i])
                temp_rho.append(rrhos[i])
                temp_q.append(rqs[i])
            # print(temp_gs)
            # print(temp_rho)
            # print(temp_q)
            gsas2.append(np.nanmean(temp_gs))
            rhoas2.append(np.nanmean(temp_rho))
            qas2.append(np.nanmean(temp_q))

            temp_pos = pos
    # print(patternas2)
    # print(len(patternas2))
    gsas2 = gsas2[1:]
    # print(gsas2)
    # print(len(gsas2))
    rhoas2 = rhoas2[1:]
    # print(rhoas2)
    # print(len(rhoas2))
    qas2 = qas2[1:]
    # print(qas2)
    # print(len(qas2))
    # APPEND THE FIRST ITEM OF the ___2 LIST TO THE END OF ___ LIST TO MAKE IT WHOLE
    patternas.append(patternas2[0])
    gsas.append(gsas2[0])
    rhoas.append(rhoas2[0])
    qas.append(qas2[0])

    print(patternas)
    print(gsas)
    print(rhoas)
    print(qas)

    # choose which things to plot and create array
    z_p = []
    if plottingthis == 'csds':
        tempdata = gsas
    elif plottingthis == 'rho':
        tempdata = rhoas
    else:
        tempdata = qas

    for row in range(numrows):
        print(f'row: {row}')
        newpattern = float(startpattern + (numcols * row))
        endpattern = float(newpattern + numcols - 1)
        print(newpattern)
        print(endpattern)
        f_pnl_p, a_fwhml_p, missing_p = get_row_b3(patternas, tempdata, newpattern, endpattern)  # rhoas, gsas, qas
        z_p.append(a_fwhml_p)
    # end short module

    # generate z values
    z = z_p

    z_length = len(z)
    print(f'z_length: {z_length}')

    # generate 2 2d grids for the x & y bounds
    # y, x = np.meshgrid(np.linspace(13.4, 10.4 - 0.5, 6 + 1), np.linspace(-14.1, 13.8 + 0.5, 56 + 1))
    y, x = np.meshgrid(np.linspace(13.4, 13.4 - (0.5 * z_length) - 0.5, z_length + 1),
                       np.linspace(-14.1, 13.8 + 0.5, 56 + 1))

    print('----- z ----')
    print(z)
    newz = []
    for row in z:
        newrow = []
        for val in row:
            newrow.append(np.nanmean(val))
        newz.append(newrow)
    print(newz)

    # using newz instead of z
    z = np.array(newz).T.tolist()

    # write to file
    if writeflag:
        # old way to write to file
        # with open(r'D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hd_1_4permm2/GE4_mwhoutput_gs.txt', 'w') as f:

        # new way to write to file
        # filelocation = 'D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hd_1_4permm2/'
        if plottingthis == 'csds':
            with open(f'{filelocation}{suffix}_mwhoutput_gs.txt', 'w') as f:
                for item in z:
                    # write each item on a new line
                    f.write("%s\n" % item)
        elif plottingthis == 'rho':
            with open(f'{filelocation}{suffix}_mwhoutput_rho.txt', 'w') as f:
                for item in z:
                    # write each item on a new line
                    f.write("%s\n" % item)
        else:
            with open(f'{filelocation}{suffix}_mwhoutput_q.txt', 'w') as f:
                for item in z:
                    # write each item on a new line
                    f.write("%s\n" % item)

    # old way to generate min and max values
    # z_min, z_max = 0, 1000  # gsas
    # z_min, z_max = 1e12, 1e15  # rhoas
    # z_min, z_max = 1.71, 2.46  # qas

    # new way to generate min and max values
    if plottingthis == 'csds':
        z_min, z_max = 0, 1000  # gsas
    elif plottingthis == 'rho':
        z_min, z_max = 1e12, 1e15  # rhoas
    else:
        z_min, z_max = 1.71, 2.46  # qas

    # print(max(max(z)))
    #######################################################################################

    ############################################## 2D HEATMAP #####################################
    fig, ax = plt.subplots()

    c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)

    # old way to generate titles of plot
    # ax.set_title(f'Hypotenuse Up 1 - Dislocation Density [m^-2] vs. Location [mm] - GE4')
    # ax.set_title(f'{prefix} - Coherent Scattering Domain Size [nm] vs. Location [mm] - {suffix}')
    # ax.set_title(f'Hypotenuse Up 1 - Edge/Screw Character vs. Location [mm] - GE1')

    # new way to generate titles of plot
    if plottingthis == 'csds':
        ax.set_title(f'{prefix} - Coherent Scattering Domain Size [nm] vs. Location [mm] - {suffix}')
    elif plottingthis == 'rho':
        ax.set_title(f'{prefix} - Dislocation Density [m^-2] vs. Location [mm] - {suffix}')
    else:
        ax.set_title(f'{prefix} - Edge/Screw Character vs. Location [mm] - {suffix}')

    # set the limits of the plot to the limits of the data
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    fig.colorbar(c, ax=ax)

    plt.gca().invert_yaxis()
    plt.show()
    interactive(True)
    ###############################################################################################