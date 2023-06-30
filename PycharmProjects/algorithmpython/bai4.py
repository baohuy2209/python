"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""


class Solution:
    def comb(self, c: list[int], t: int, i: int, l: list[int], ans: list[list[int]]):
        if t == 0:
            ans.append(list(l))
            return
        if t < 0:
            return
        for j in range(i, len(c)):
            if j > i and c[j] == c[j - 1]:
                continue
            l.append(c[j])
            self.comb(c, t - c[j], j + 1, l, ans)
            l.pop()

    def combinationSum2(self, c: list[int], t: int) -> list[list[int]]:
        c.sort()
        l = []
        ans = [[]]
        self.comb(c, t, 0, l, ans)
        return ans[1:]


if __name__ == "__main__":
    lst = []
    sol = Solution()
    length = int(input("Length : "))
    print("Enter the elements : ")
    for i in range(length):
        n = int(input("Element : "))
        lst.append(n)
    tar = int(input("Input target : "))
    print("Result : ")
    print(sol.combinationSum2(lst,tar))


