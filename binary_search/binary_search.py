from bubble_sort import bubble_sort
import random

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



def run():
    
    my_list = [random.randint(1, 100) for i in range(31)]

    my_list = bubble_sort(my_list)
    
    print(my_list)
    objective = int(input("What element do you want to find?: "))
    result = binary_search(my_list, objective)
    print(f"result found, objective: {objective}" if result != -1 else "result not found"  )


if __name__ == '__main__':
    run()