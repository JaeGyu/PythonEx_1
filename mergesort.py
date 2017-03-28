import random as rnd 

def merge(list1, list2):
    resultList = []
    while list1 and list2:
        if list1[0] <= list2[0]:
            resultList.append(list1.pop(0))
        else:
            resultList.append(list2.pop(0))
    
    while list1:
        resultList.append(list1.pop(0))
    
    while list2:
        resultList.append(list2.pop(0))

    return resultList

def merge_sort(list):
    if len(list) > 1:
        mid = int(len(list)/2)
        list1 = list[:mid]
        list2 = list[mid:]
        list1 = merge_sort(list1)
        list2 = merge_sort(list2)
        list = merge(list1,list2)
    return list

def main():

    list = rnd.sample(range(10), 10)
    print("Before sort : ", list)
    list = merge_sort(list)
    print("After  sort : ", list)

if __name__ == "__main__":
    main()

