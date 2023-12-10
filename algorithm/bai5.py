"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = 0
        while x > 0:
            d = x%10
            s = s*10 + d
            x = x/10
        if x == s:
            return True
        return False


if __name__ == "__main__":
    x = int(input("Enter the number : "))
    sol = Solution()

    if sol.isPalindrome(x):
        print("X is a palindrome.")
    else:
        print("X is not palindrome.")