"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


class Solution:
    def concatenate(self,lst1,lst2):
        li = []
        for i in lst1:
            for j in lst2:
                li.append(i+j)
        return li

    def letterCombinations(self, dig: str) -> list[str]:
        lict_let = {'1': [" "],
                    '2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}
        letter_combination_list = ['']
        for each_digit in digit:
            each_digit_list = lict_let[each_digit]
            letter_combination_list=self.concatenate(letter_combination_list,each_digit_list)
        if letter_combination_list == [" "]:
            letter_combination_list = []
        return letter_combination_list


if __name__ == "__main__":
    digit = input("Enter the chain of digit : ")
    sol = Solution()
    li = sol.letterCombinations(digit)
    print(li)