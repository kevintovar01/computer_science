import random

def sequence_search(my_list, objective):

    for i in my_list:
        if i == objective:
            return i
    return -1


def run():
    
    my_list = [random.randint(1, 100) for i in range(31)]

    print(my_list)
    objective = int(input("What element do you want to find?: "))
    result = sequence_search(my_list, objective)
    print(f"result found, objective: {objective}" if result != -1 else "result not found"  )


if __name__ == '__main__':
    run()