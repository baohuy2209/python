# Give a string s , return the longest palindrome substring in s

class Solution:

    def longestpalindrome(self, s:str) -> str:
        def palindrome(l,r):
            while (l > 0) and (r < len(s)) and s[l]==s[r]:
                l = l - 1
                r = r + 1
            return s[l+1:r]
        res = " "
        for i in range(len(s)):
            pal = palindrome(i,i)
            if len(pal) > len(res):
                res = pal
            pal = palindrome(i,i+1)
            if len(pal) > len(res):
                res = pal
        return res


if __name__ == "__main__" :
    s = input("Enter string :")
    sol = Solution()
    print(sol.longestpalindrome(s))
