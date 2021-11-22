"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    def __init__(self, num):
        self.num = num

    @property
    def climing_stairs(self):
        """
        Approach: Dynamic programming
        :param nums:
        :return:
        """
        first = 1  # f(1)
        second = 2  # f(2)

        if self.num == 1:
            return first
        elif self.num == 2:
            return second

        for n in range(3, self.num+1):  # n = 4 == f(2) + f(3)
            temp = second
            second = first + second  # f(3)
            first = temp  # f(2)

        return second


if __name__ == "__main__":
    sol = Solution(4)
    print(sol.climing_stairs)
