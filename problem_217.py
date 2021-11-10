"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def contains_duplicates(nums):
        num_dict = {}
        for n in nums:
            if n not in num_dict.keys():
                num_dict[n] = 1
            else:
                return True
        return False


if __name__ == "__main__":
    sol = Solution
    print(sol.contains_duplicates([1,2,3,4]))
