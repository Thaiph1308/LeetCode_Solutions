unsorted_list = [33,5,7,9,4,12,5,7,87,1,1,11,5,7,8,1]

def buble_sort(unsorted_list):
    length = len(unsorted_list)
    print(length)
    count = 0
    for i in range(length):
        for j in range(0,length-1):
            count = count + 1
            print(i,j,unsorted_list)
            if (unsorted_list[j] > unsorted_list[j+1]):
                #print("swap:" , unsorted_list[j], unsorted_list[j+1],sep="|")
                unsorted_list[j] , unsorted_list[j+1] = unsorted_list[j+1] , unsorted_list[j]
    #print(count)

#buble_sort(unsorted_list)

def selection_sort(unsorted_list):
    '''
    Divive the unsorted_list into 2 part:
    1. Sorted part
    2. Unsorted part
    Find min value in unsorted part and add it into sorted part
    '''
    length = len(unsorted_list)
    count = 0
    for i in range(length):
        min_index = i
        for j in range(i,length):
            count = count + 1
            print(i,j,unsorted_list)
            if (unsorted_list[j] < unsorted_list[min_index]):
                min_index = j
                #print(min_index,unsorted_list[j],unsorted_list[min_index],sep=" | ")
        unsorted_list[min_index] , unsorted_list[i] = unsorted_list[i] , unsorted_list[min_index]
        #print("swap:",min_index,i,sep=" ")
        #print(count)
    
#selection_sort(unsorted_list)

def insertion_sort():
    '''
    Same as Selection Sort, we have 2 parts:
    1. Sorted
    2. Unsorted
    '''
    pass

def heapify(nums, heap_size, root_index):  
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    #print(largest,left_child,right_child)
    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        #print(largest,left_child,right_child)
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        #print(largest,left_child,right_child)
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest (check right_child/left child), so max Heappify = 2 times
        heapify(nums, heap_size, largest)


def heap_sort(nums):  
    n = len(nums)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n//2, -1, -1):
        print(unsorted_list,i)
        heapify(nums, n, i)
    # Move the root of the max heap (largest number) to the end of the max_heap tree, then remove it (because it's sorted), make a new max_heap with res elements (move i from n-1 to 0 with step = -1)
    print("------------")
    for i in range(n - 1, 0, -1):
        print(unsorted_list,i)
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    print(unsorted_list)

#heap_sort(unsorted_list)

def merge_sort(unsorted_list):
    '''
    Divide and Conquer
    NEED EXTRA MEMORY  
    '''
    n = len(unsorted_list)
    mid_pivot = n//2
    left_list = unsorted_list[:mid_pivot]
    right_lift = unsorted_list[mid_pivot:]
    print(mid_pivot,left_list,right_lift,sep=" | ")

merge_sort(unsorted_list)