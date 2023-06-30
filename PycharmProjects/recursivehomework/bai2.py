#quicksort recursive
def quicksort(arr) :
    if len(arr) == 1 :
        return arr
    else :
        b = int(len(arr)/2)
        pivot = arr[b]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]
        return quicksort(left) + middle + quicksort(right)
arr = []
n = int(input("Enter the length of array : "))
for i in range(1,n+1) :
    a =int(input("Enter the element : "))
    arr.append(a)
quicksort(arr)