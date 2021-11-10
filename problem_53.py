"""Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[
i]] for each 0 <= i < nums.length and return it. A zero-based permutation nums is an array of distinct integers from
0 to nums.length - 1 (inclusive). """


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def max_sub_array(nums):
        max_sum = nums[0]
        current_sum = 0
        for n in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += n
            max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == "__main__":
    sol = Solution
    print(sol.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
