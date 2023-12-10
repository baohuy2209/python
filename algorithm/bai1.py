"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
def concatenatearray(nums1, nums2):
    list = []
    for i in nums1:
        list.append(i)
    for i in nums2:
        list.append(i)
    return list


def selectionsort(nums1, nums2):
    lst = concatenatearray(nums1, nums2)
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
    return lst


def inputarray(n):
    li = []
    for i in range(n):
        n = int(input("Element : "))
        li.append(n)
    return li


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array = selectionsort(nums1, nums2)
        if len(array) % 2 == 0:
            median = (array[int(len(array) / 2 - 1)] + array[int(len(array) / 2)]) / 2
        else:
            median = array[int(len(array) / 2)]
        return median

if __name__ == "__main__" :
    sol = Solution()
    print("Enter the two array : ")
    print(" + The first array : ")
    length1 = int(input("   + Length : "))
    lst1 = inputarray(length1)
    print(" + The second array : ")
    length2 = int(input("   + Length : "))
    lst2 = inputarray(length2)
    print("Median of the two sorted arrays : ", sol.findMedianSortedArrays(lst1, lst2))
