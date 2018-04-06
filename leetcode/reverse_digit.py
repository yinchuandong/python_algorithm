class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        x = abs(x)
        s = 0
        while x > 0:
            s = s * 10 + x % 10
            x = x / 10

        if s > 1 << 31:
            return 0

        if is_negative:
            s *= -1
        return s


if __name__ == '__main__':
    sol = Solution()
    # print sol.reverse(-321)
    # print sol.reverse(123)
    # print sol.reverse(0)
    print sol.reverse(1534236469)
