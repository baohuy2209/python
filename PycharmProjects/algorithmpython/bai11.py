"""Give an array of integers nums and an integer target ,
 return indices of the two numbers such that they add up to target"""


class Solution:
    def twosum(self, arr : list[int], target: int) -> list[list[int]]:
        res = []
        li = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j] == target:
                    li = [i,j]
                    res.append(li)

        return res


if __name__ == "__main__":
    sol = Solution()

    n = int(input("Enter the length of list : "))
    arr = []
    print("Enter the array : ")
    for i in range(n):
        x = int(input("Element : "))
        arr.append(x)

    target = int(input("Enter the target : "))

    print("Result : ",sol.twosum(arr, target))
