import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # panels = [1, 1, 1, 1, 1, 1, 1,
    #           3, 3, 3, 3, 3,
    #           4, 4, 4, 4, 4, 4, 4, 4]
    # pns = [319, 320, 320, 323, 323, 323, 325,
    #        314, 316, 318, 321, 321,
    #        345, 350, 374, 376, 381, 381, 383, 386]
    # infos = [170160, 140130, 180170, 140130, 150140, 180170, 150140,
    #          180170, 130120, 160150, 150140, 160150,
    #          140130, 170160, 150140, 130120, 140130, 150140, 150140, 160150]
    # cmwprhos = [1.63312, 0.544979, 0.652153, 1.60745, 1.66298, 1.07165, 1.25892,
    #             0.855958, 2.31208, 0.873691, 1.92204, 1.30897,
    #             0.750480, 2.80368, 1.686130, 0.67654, 3.28365, 0.633994, 1.62627, 0.563901]
    # mwhrhos = [7.84238606, 3.25695934, 2.68709130, 6.56398464, 7.38319251, 6.19360516, 4.94079689,
    #            4.35949340, 6.14449499, 8.56759807, 7.82913337, 9.54155865,
    #            2.12013717, 9.20337490, 4.45944607, 1.19577653, 3.84223751, 7.69665205, 3.83422997, 1.57563616]

    panels = [1, 1, 1, 1, 1, 1, 1,
              3, 3, 3, 3, 3,
              ]
    pns = [319, 320, 320, 323, 323, 323, 325,
           314, 316, 318, 321, 321,
           ]
    infos = [170160, 140130, 180170, 140130, 150140, 180170, 150140,
             180170, 130120, 160150, 150140, 160150,
             ]
    cmwprhos = [1.63312, 0.544979, 0.652153, 1.60745, 1.66298, 1.07165, 1.25892,
                0.855958, 2.31208, 0.873691, 1.92204, 1.30897,
                ]
    mwhrhos = [7.84238606, 3.25695934, 2.68709130, 6.56398464, 7.38319251, 6.19360516, 4.94079689,
               4.35949340, 6.14449499, 8.56759807, 7.82913337, 9.54155865,
               ]

    # compute raw ratios
    rhoratios = [(cmwprho / mwhrhos[pos]) for pos, cmwprho in enumerate(cmwprhos)]
    print(rhoratios)
    print(np.nanmean(rhoratios))
    print(np.nanstd(rhoratios))

    # compute ratios averaging at each pattern number first
    uniquepatterns = []
    acmwprhos = []
    amwhrhos = []

    oldpattern = np.NaN
    oldpos = 0
    for pos, pattern in enumerate(pns):

        tempcmwprhos = []
        tempmwhrhos = []

        if pattern != oldpattern or pos == (len(pns) - 1):

            uniquepatterns.append(pattern)
            # print(pattern)

            for i in range(oldpos, pos):
                tempcmwprhos.append(cmwprhos[i])
                tempmwhrhos.append(mwhrhos[i])

            if pos == (len(pns) - 1):
                tempcmwprhos.append(cmwprhos[pos])
                tempmwhrhos.append(mwhrhos[pos])

            oldpattern = pattern
            oldpos = pos

            if pos > 0:
                acmwprhos.append(np.nanmean(tempcmwprhos))
                amwhrhos.append(np.nanmean(tempmwhrhos))

            if pattern == 386:
                acmwprhos.append(cmwprhos[pos])
                amwhrhos.append(mwhrhos[pos])

    # cull the last point cause it's extra
    # uniquepatterns = uniquepatterns[:-1]

    print(uniquepatterns)
    print(acmwprhos)
    print(amwhrhos)

    arhoratios = [(acmwprho / amwhrhos[pos]) for pos, acmwprho in enumerate(acmwprhos)]

    # removing the 2 outliers
    arhoratios[5] = np.NaN
    arhoratios[6] = np.NaN

    print(arhoratios)
    print(np.nanmean(arhoratios))
    print(np.nanstd(arhoratios))
