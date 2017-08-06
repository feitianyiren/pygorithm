# Author: OMKAR PATHAK
# Contributors: Mohamed Kiouaz
# Created On: 31st July 2017

# Best O(n); Average O(n*(n-1)/4); Worst O(n^2)

# Bubble Sorting algorithm
def sort(List):
    for i in range(len(List)):
        stop = True
        for j in range(len(List) - 1, i, -1):
            if List[j] < List[j - 1]:
                stop = False
                List[j], List[j - 1] = List[j - 1], List[j]
        if(stop == True):
            return List
    return List

# time complexities
def time_complexities():
    return '''Best case O(n); Average case O(n * (n - 1) / 4); Worst case O(n ^ 2)'''

# easily retrieve the source code of the sort function
def get_code():
    import inspect
    return inspect.getsource(sort)
