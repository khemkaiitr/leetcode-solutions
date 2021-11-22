"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
"""


class Solution:
    def __init__(self, nums):
        self.nums = nums

    @property
    def missing_number_method1(self):
        """
        Approach: represent the numbers in set and then substract from 1-n set
        :param nums:
        :return:
        """
        num_set = set(self.nums)
        range_set = set(range(1, len(self.nums) + 1))
        return list(range_set - num_set)

    @property
    def missing_number_method2(self):
        """
        This method is based on negative indexing of all the numbers.
        :return:
        """
        result = []
        for n in self.nums:
            pos = abs(n) - 1
            if self.nums[pos] > 0:
                self.nums[pos] *= -1

        for ind in range(0, len(self.nums)):
            if self.nums[ind] > 0:
                result.append(ind + 1)
        return result


if __name__ == "__main__":
    sol = Solution([4, 3, 2, 7, 8, 2, 3, 1])
    print(sol.missing_number_method1)
    print(sol.missing_number_method2)
