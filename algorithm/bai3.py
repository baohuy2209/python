"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""


class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def bt(i,sum,comb):
            if sum == target:
                result.append(comb.copy())
                return

            if i == len(candidates) or sum > target:
                return

            comb.append(candidates[i])
            bt(i,sum+candidates[i],comb)
            comb.pop()
            bt(i+1,sum,comb)

        result = []
        bt(0,0,[])
        return result


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
    print(sol.combinationSum(lst,tar))
