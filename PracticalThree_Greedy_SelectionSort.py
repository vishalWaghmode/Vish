#Implement Greedy search algorithm for any of the following app:
#I. Selection Sort
def SelectionSort(array:list)->list:
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                array[i] , array[j] = array[j] , array[i]
    return array
print(SelectionSort([5,1,1,2,0,0]))        
