"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def search_insert(nums, target):
        l, h = 0, len(nums) - 1 # 0, 3
        while l <= h: # True
            m = (l + h) // 2 # 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m - 1
            else:
                l = m + 1 # 2
        return l


if __name__ == "__main__":
    sol = Solution
    print(sol.search_insert(nums=[1, 3, 5, 6], target=0))
