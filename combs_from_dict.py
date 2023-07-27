from typing import List, Dict

def split_dict(purpose : List[int],
               data : Dict[any, int],
               err : int = 0) -> List[int, Dict[any, int]]:
    ''' return all possible combinations as list of dicts where key is purposeID, value is part of data dict'''
    k_data, v_data = zip(*data.items())
    comms = [[] for d in range(len(v_data)+1)]
    comms[0] = [[0 for i in range(len(purpose))]]
    anss = [[] for d in range(len(v_data)+1)]
    anss[0] = [[[] for i in range(len(purpose))]]
    for d in range(1, len(v_data)+1):
        for p in range(len(purpose)):
            for var in range(len(purpose)):
                if p == var:
                    for prev in range(len(comms[d-1])):
                        presum = v_data[d-1] + comms[d-1][prev][p]
                        if purpose[p] - presum == 0 \
                            or (purpose[p] - presum >= min(v_data[d:], default=0) + err \
                                and presum <= purpose[p]):
                                anss[d].append([anss[d-1][prev][i] + ([d-1] if p == i else [])
                                                for i in range(len(purpose))])
                                comms[d].append([presum if p == i else comms[d-1][prev][i]
                                                 for i in range(len(purpose))])
    result = []
    ''' check if final result fits in err limit and we used all data '''
    for ans in range(len(anss[-1])):
        if sum([1 for i in anss[-1][ans] for ii in i]) == len(data) \
            and all([purpose[i] - err <= comms[-1][ans][i] <= purpose[i] + err
                     for i in range(len(comms[-1][ans]))]):
            ans_return = {i : {k_data[ii] : v_data[ii]
                                        for ii in anss[-1][ans][i]}
                          for i in range(len(anss[-1][ans]))}
            result.append(ans_return)
    return result

#example
mysums = [1000, 1000, 1000]
mycosts = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g'], [100, 200, 300, 900, 950, 500, 50]))
res = split_dict(mysums, mycosts)