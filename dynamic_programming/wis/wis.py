def wis(weighted_list):
    wis_list = weighted_list.copy()
    wis_list.insert(0, 0)
    for i in range(2, len(wis_list)):
        wis_list[i] = max(wis_list[i - 1], wis_list[i - 2] + weighted_list[i - 1])
    return wis_list
