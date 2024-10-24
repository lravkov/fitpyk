import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # panels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #           2, 2, 2, 2,
    #           3, 3, 3, 3,
    #           4, 4, 4, 4
    #           ]
    #
    # # maybe remove GE1: 370, 742
    # pns = [129, 158, 226, 370, 619, 742, 964, 1129, 1411, 1468, 1469,
    #        105, 564, 703, 1247,
    #        138, 365, 905, 1034,
    #        367, 649, 727, 801
    #        ]
    # infos = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #          2, 2, 2, 2,
    #          3, 3, 3, 3,
    #          4, 4, 4, 4
    #          ]
    # cmwprhos = [0.98696, 0.62884, 0.96395, 0.40517, 1.0887, 0.99947, 1.0772, 1.2547, 6.1293, 5.4774, 0.6698,
    #             4.4729, 1.2194, 1.0158, 0.38352,
    #             9.437, 3.2344, 1.9422, 4.7943,
    #             2.5056, 5.3734, 9.311, 1.6832
    #             ]
    # mwhrhos = [7.56266172, 5.58733356, 4.09964536, 3.61753302, 3.7039804, 3.73897131, 4.7100334, 5.42036201, 11.3231203, 11.7107267, 8.46144925,
    #            9.42802738, 4.88231516, 3.78092056, 3.98190874,
    #            6.91173539, 4.56297163, 2.73105925, 7.78669368,
    #            4.23625963, 9.49221472, 19.8700113, 3.74995879
    #            ]

    # GE3 and GE4 PANELS DISAGREE WITH 1 and 2
    panels = [
              4, 4, 4, 4
              ]

    # maybe remove GE1: 370, 742
    pns = [
           367, 649, 727, 801
           ]
    infos = [
             4, 4, 4, 4
             ]
    cmwprhos = [
                2.5056, 5.3734, 9.311, 1.6832
                ]
    mwhrhos = [
               4.23625963, 9.49221472, 19.8700113, 3.74995879
               ]

    # compute raw ratios
    rhoratios = [(cmwprho / mwhrhos[pos]) for pos, cmwprho in enumerate(cmwprhos)]

    # use these if you are using panels 1 and 2
    # rhoratios[8] = np.NaN
    # rhoratios[9] = np.NaN
    # rhoratios[12] = np.NaN

    # don't use these normally
    # rhoratios[0] = np.NaN
    # rhoratios[19] = np.NaN
    # rhoratios[20] = np.NaN
    # rhoratios[21] = np.NaN
    # rhoratios[22] = np.NaN

    print(rhoratios)
    print(np.nanmean(rhoratios))
    print(np.nanstd(rhoratios))

    # GE1: 0.18786259916593495 +- 0.07446106049006462  # 9 points
    # GE2: 0.27229119169805840 +- 0.13448670716070620  # 4 points

    # GE3: 0.67856438572633680 +- 0.04445892177637750  # 3 points
    # GE4: 0.51875099961812280 +- 0.06109093912026764  # 4 points

    # compute ratios averaging at each pattern number first
    # uniquepatterns = []
    # acmwprhos = []
    # amwhrhos = []
    #
    # oldpattern = np.NaN
    # oldpos = 0
    # for pos, pattern in enumerate(pns):
    #
    #     tempcmwprhos = []
    #     tempmwhrhos = []
    #
    #     if pattern != oldpattern or pos == (len(pns) - 1):
    #
    #         uniquepatterns.append(pattern)
    #         # print(pattern)
    #
    #         for i in range(oldpos, pos):
    #             tempcmwprhos.append(cmwprhos[i])
    #             tempmwhrhos.append(mwhrhos[i])
    #
    #         if pos == (len(pns) - 1):
    #             tempcmwprhos.append(cmwprhos[pos])
    #             tempmwhrhos.append(mwhrhos[pos])
    #
    #         oldpattern = pattern
    #         oldpos = pos
    #
    #         if pos > 0:
    #             acmwprhos.append(np.nanmean(tempcmwprhos))
    #             amwhrhos.append(np.nanmean(tempmwhrhos))
    #
    #         if pattern == 386:
    #             acmwprhos.append(cmwprhos[pos])
    #             amwhrhos.append(mwhrhos[pos])
    #
    # # cull the last point cause it's extra
    # # uniquepatterns = uniquepatterns[:-1]
    #
    # print(uniquepatterns)
    # print(acmwprhos)
    # print(amwhrhos)
    #
    # arhoratios = [(acmwprho / amwhrhos[pos]) for pos, acmwprho in enumerate(acmwprhos)]
    #
    # # removing the 2 outliers
    # # arhoratios[5] = np.NaN
    # # arhoratios[15] = np.NaN
    # # arhoratios[16] = np.NaN
    # # arhoratios[17] = np.NaN
    #
    # print(arhoratios)
    # print(np.nanmean(arhoratios))
    # print(np.nanstd(arhoratios))
