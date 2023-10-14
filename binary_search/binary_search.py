def binary_search(my_list, objective):

    left = 0
    right = len(my_list)-1

    while left <= right:

        medio = (left+right)//2
        if my_list[medio] == objective:
            return objective
        elif my_list[medio] < objective:
            left = medio+1
        else:
            right = medio-1
    
    return -1