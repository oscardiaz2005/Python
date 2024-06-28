def soter_list(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(list[j]) > len(list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
    return list




   