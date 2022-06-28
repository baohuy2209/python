class Solution:
    def twosum(self, candidate: list[int], target: int) -> list[int] :
        list = []
        for i in range(len(candidate)-1):
            for j in range(i+1,len(candidate)):
                if candidate[i]+candidate[j] == target:
                    list.append([i, j])

        return list


if __name__ == "__main__":
    target = int(input("Enter the target number :"))
    n = int(input("Enter length of list : "))
    li = []
    for i in range(n):
        x = int(input("Element :"))
        li.append(x)
    sol = Solution()
    print(sol.twosum(li, target))
