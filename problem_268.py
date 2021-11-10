"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def missing_number_method1(self):
        """
        Approach: find sum of all the numbers in the array as well as sum of n elements.
         Difference between these two will give the missing number
        :param nums:
        :return:
        """
        num_elements = len(self.nums)
        sum_n_numbers = (num_elements + 1) * num_elements / 2
        sum_nums = sum(self.nums)
        return int(sum_n_numbers - sum_nums)

    @property
    def missing_number_method2(self):
        """
        This method uses XORs. The idea is simple x^x = 0 so 0^x = x so if we perform xor on nums array and [0, n]
        missing value will be returned
        :return:
        """
        result = 0
        for num in range(0, len(self.nums)+1):
            result ^= num

        for num in self.nums:
            result ^= num
        return result


if __name__ == "__main__":
    sol = Solution([3, 0, 1])
    print(sol.missing_number_method1())
    print(sol.missing_number_method2)
