import random

#this algorithm compare one elemen to it's second and swap if necessary

def bubble_sort(mylist):
    len_list = len(mylist)

    for i in range(len_list):
        for j in range(len_list-i-1): #this decrements the list, for don't repeat iterations to future
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

    return mylist 


def run():
    mylist = [random.randint(1, 100) for i in range(10)]
    print(mylist)

    list_sorted = bubble_sort(mylist) 
    print(list_sorted)


if __name__ == '__main__':
    run()