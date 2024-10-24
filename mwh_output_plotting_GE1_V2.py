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
    # print(rlmp)

    if rlmp[0] == rlmp[1]:
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
    df = pd.read_csv('GE1_mwh_output.txt')
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

    # get the rows to plot
    print('----------')
    f_pnl_155184, a_rhoal_155184, missing_155184 = get_row_b3(patternas, gsas, 155.0, 184.0)
    print(missing_155184)
    print(f_pnl_155184)
    print(a_rhoal_155184)
    print('----------')

    print('----------')
    f_pnl_185214, a_rhoal_185214, missing_185214 = get_row_b3(patternas, gsas, 185.0, 214.0)
    print(missing_185214)
    print(f_pnl_185214)
    print(a_rhoal_185214)
    print('----------')

    print('----------')
    f_pnl_215244, a_rhoal_215244, missing_215244 = get_row_b3(patternas, gsas, 215.0, 244.0)
    print(missing_215244)
    print(f_pnl_215244)
    print(a_rhoal_215244)
    print('----------')

    print('----------')
    f_pnl_245274, a_rhoal_245274, missing_245274 = get_row_b3(patternas, gsas, 245.0, 274.0)
    print(missing_245274)
    print(f_pnl_245274)
    print(a_rhoal_245274)
    print('----------')

    print('----------')
    f_pnl_275304, a_rhoal_275304, missing_275304 = get_row_b3(patternas, gsas, 275.0, 304.0)
    print(missing_275304)
    print(f_pnl_275304)
    print(a_rhoal_275304)
    print('----------')

    print('----------')
    f_pnl_305334, a_rhoal_305334, missing_305334 = get_row_b3(patternas, gsas, 305.0, 334.0)
    print(missing_305334)
    print(f_pnl_305334)
    print(a_rhoal_305334)
    print('----------')

    print('----------')
    f_pnl_335364, a_rhoal_335364, missing_335364 = get_row_b3(patternas, gsas, 335.0, 364.0)
    print(missing_335364)
    print(f_pnl_335364)
    print(a_rhoal_335364)
    print('----------')

    print('----------')
    f_pnl_365394, a_rhoal_365394, missing_365394 = get_row_b3(patternas, gsas, 365.0, 394.0)
    print(missing_365394)
    print(f_pnl_365394)
    print(a_rhoal_365394)
    print('----------')

    print('----------')
    f_pnl_395424, a_rhoal_395424, missing_395424 = get_row_b3(patternas, gsas, 395.0, 424.0)
    print(missing_395424)
    print(f_pnl_395424)
    print(a_rhoal_395424)
    print('----------')

    print('----------')
    f_pnl_425454, a_rhoal_425454, missing_425454 = get_row_b3(patternas, gsas, 425.0, 454.0)
    print(missing_425454)
    print(f_pnl_425454)
    print(a_rhoal_425454)
    print('----------')

    print('----------')
    f_pnl_455484, a_rhoal_455484, missing_455484 = get_row_b3(patternas, gsas, 455.0, 484.0)
    print(missing_455484)
    print(f_pnl_455484)
    print(a_rhoal_455484)
    print('----------')

    print('----------')
    f_pnl_485514, a_rhoal_485514, missing_485514 = get_row_b3(patternas, gsas, 485.0, 514.0)
    print(missing_485514)
    print(f_pnl_485514)
    print(a_rhoal_485514)
    print('----------')

    print('----------')
    f_pnl_515544, a_rhoal_515544, missing_515544 = get_row_b3(patternas, gsas, 515.0, 544.0)
    print(missing_515544)
    print(f_pnl_515544)
    print(a_rhoal_515544)
    print('----------')

    print('----------')
    f_pnl_545574, a_rhoal_545574, missing_545574 = get_row_b3(patternas, gsas, 545.0, 574.0)
    print(missing_545574)
    print(f_pnl_545574)
    print(a_rhoal_545574)
    print('----------')

    print('----------')
    f_pnl_575604, a_rhoal_575604, missing_575604 = get_row_b3(patternas, gsas, 575.0, 604.0)
    print(missing_575604)
    print(f_pnl_575604)
    print(a_rhoal_575604)
    print('----------')

    print('----------')
    f_pnl_605634, a_rhoal_605634, missing_605634 = get_row_b3(patternas, gsas, 605.0, 634.0)
    print(missing_605634)
    print(f_pnl_605634)
    print(a_rhoal_605634)
    print('----------')

    print('----------')
    f_pnl_635664, a_rhoal_635664, missing_635664 = get_row_b3(patternas, gsas, 635.0, 664.0)
    print(missing_635664)
    print(f_pnl_635664)
    print(a_rhoal_635664)
    print('----------')

    # this one is a test
    print('----------')
    f_pnl_test, a_rhoal_test, missing_test = get_row_b3(patternas, gsas, 635.0, 664.0)
    print(missing_test)
    print(f_pnl_test)
    print(a_rhoal_test)
    print('----------')

    # plot averaged results vs. corresponding pattern number
    # generate 2 2d grids for the x & y bounds
    y, x = np.meshgrid(np.linspace(-18.688, -2.688, 17), np.linspace(141.13, 170.13, 30))

    # generate z values
    z = [a_rhoal_155184, a_rhoal_185214, a_rhoal_215244, a_rhoal_245274, a_rhoal_275304, a_rhoal_305334, a_rhoal_335364,
         a_rhoal_365394, a_rhoal_395424, a_rhoal_425454, a_rhoal_455484, a_rhoal_485514, a_rhoal_515544, a_rhoal_545574,
         a_rhoal_575604, a_rhoal_605634, a_rhoal_635664]

    z = np.array(z).T.tolist()

    # write to file
    with open(r'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE1_mwhoutput_gs.txt', 'w') as f:
        for item in z:
            # write each item on a new line
            f.write("%s\n" % item)

    # generate min and max values
    z_min, z_max = 0, 1000

    # print(max(max(z)))
    #######################################################################################

    ############################################## 2D HEATMAP #####################################
    fig, ax = plt.subplots()

    c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)
    ax.set_title('csds vs. Location - GE1')
    # set the limits of the plot to the limits of the data
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    fig.colorbar(c, ax=ax)

    plt.gca().invert_yaxis()
    plt.show()
    interactive(True)
    ###############################################################################################