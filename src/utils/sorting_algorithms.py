'''
Created on Dec 12, 2015

@author: Adam
'''
def quick_sort(lista, *,key=lambda x: x, reverse=False, cmp=lambda x, y: x < y):
    '''
    Quicksort is a divide and conquer algorithm. 
    Quicksort first divides a large array into two smaller sub-arrays: 
        - the low elements and the high elements. 
    Quicksort can then recursively sort the sub-arrays.
    The steps are:
        1.Pick an element, called a pivot, from the array.
        2.Reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
        3.Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
    The base case of the recursion is arrays of size zero or one, which never need to be sorted.
    '''
    if lista != []:
        pivot = lista[0]
        left = quick_sort([x for x in lista[1:] if cmp(key(x), key(pivot))], key=key, reverse=reverse, cmp=cmp)
        right = quick_sort([x for x in lista[1:] if not cmp(key(x), key(pivot))], key=key, reverse=reverse, cmp=cmp)
        if reverse:
            left, right = right, left
        return left + [pivot] + right   
    else:
        return []
    
def gnome_sort(lista, *,key=lambda x: x, reverse=False, cmp=lambda x, y: x < y):
    '''
    Gnome Sort is based on the technique used by Dutch Garden Gnomes. 
    Here is how a garden gnome sorts a line of flower pots.
    Boundary conditions: if there is no previous pot, he steps forwards;
    if there is no pot next to him, he is done.
    Basically, he looks at the flower pot next to him and the previous one; 
    if they are in the right order he steps one pot forward,
    otherwise he swaps them and steps one pot backwards.
    '''
    pos = 0
    while True:
        if pos == 0:
            pos += 1
        if pos >= len(lista):
            break
        if not cmp(key(lista[pos]), key(lista[pos - 1])):
            pos += 1
        else:
            lista[pos - 1], lista[pos] = lista[pos], lista[pos - 1]
            pos -= 1
            
    if not reverse:
        return lista
    else:
        return lista[::-1]
