from typing import List, Generator

def split_list(purpose : List[int],
               data : List[int], err : int = 0,
               hist : int = 0)-> Generator:
    ''' return possible combination as list of dicts where key is purposeVALUE, value is part of data list'''
    if len(data) <= 0:
        return
    if len(data) == 1:
        for i in range(len(purpose)):
            yield [{data[-1]: [data[-1]]} if i==ii and (
                   data[-1] <= purpose[ii] + err and
                   (hist != 0 or (hist == 0 and data[-1] >= purpose[ii]-err))
                   ) else {0: []} for ii in range(len(purpose))]
    else:
        if hist == 0:
            data = sorted(data, reverse=True)[:]
        for prev in split_list(purpose, data[:-1], err, hist + 1):
            for pur in range(len(purpose)):
                prev_pur = list(prev[pur].items())[0]
                if prev_pur[0] + data[-1] > purpose[pur] + err or (
                        hist == 0 and prev_pur[0] + data[-1] < purpose[pur] - err):
                    continue
                yield [{prev_pur[0] + data[-1] : prev_pur[1] + [data[-1]]} if i == pur else prev[i] for i in range(len(prev))]

#example
mysums = [22412,30760,24903,20449]
mycosts_list = [2180,2886,2180,3982,3052,872,872,527,10900,1244,414,1639,3052,305,1308,3270,3270,3270,1308,327,436,73,109,73,225,206,182,182,872,127,436,436,436,1744,44,436,690,1744,109,1526,1744,164,76,109,3270,3270,7848,255,1003,1308,27,993,436,1526,2616,160,872,8720,273,249,311,73,436,1590,1635,1635,719,44,218]
gen_res = split_list(mysums, mycosts_list, 0)
res = next(gen_res)