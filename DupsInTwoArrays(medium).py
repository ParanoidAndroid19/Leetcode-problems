# PRAMP: Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

# case 1: both arrays are of approx same length
def find_duplicates(arr1, arr2):
    # two pointers
    v = w = 0
    op = []
    
    while v < len(arr1) and w < len(arr2):
        # if duplicate
        if arr1[v] == arr2[w]:
            op.append(arr1[v])
            v = v + 1
            w = w + 1
          
        elif(arr1[v] < arr2[w]):
            v = v + 1
          
        else:
            w = w + 1
        
    return op


print(find_duplicates([1, 2, 3, 5, 6, 7, 12], [7, 8, 9, 10, 11, 12]))


# case 2: The second array is much greater than first array
def find_duplicates(arr1, arr2):
    # for the case when arr2 length is much bigger than arr1
    op = []
    
    for num in arr1:
        if binSearch(arr2, num):
            op.append(num)
            
    return op
    
    
def binSearch(arr, num):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low+high)//2
        
        if arr[mid] == num:
            return True
            
        elif arr[mid] < num:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return False


print(find_duplicates([6, 7, 12], [7, 8, 9, 10, 11, 12, 22]))

