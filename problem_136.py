"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space."""


class Solution:
    def __init__(self, nums):
        self.nums = nums

    @property
    def single_number(self):
        """
        Approach: use xor method .. take each element one by one and use xor
        :param nums:
        :return:
        """
        result = 0
        for num in self.nums:
            result ^= num

        return result


if __name__ == "__main__":
    sol = Solution([4,1,2,1,2])
    print(sol.single_number)
