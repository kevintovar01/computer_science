import random

#this algorithm compare one elemen to it's second and swap if necessary

def bubble_sort(mylist):
    aux_list = mylist.copy()
    len_list = len(mylist)

    for i in range(1):
        for j in range(len_list-i-1): #this decrements the list, for don't repeat iterations to future
            if aux_list[j] == None:
                aux_list[j] == 0
            elif aux_list[j+1] == None:
                aux_list[j+1] = 0

            if aux_list[j] > aux_list[j+1]:
                aux_list[j], aux_list[j+1] = aux_list[j+1], aux_list[j]

    return aux_list 