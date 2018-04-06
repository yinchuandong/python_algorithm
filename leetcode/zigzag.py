class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s

        lines = ["" for _ in range(numRows)]

        row = 0
        direction = -1
        for i in range(len(s)):
            lines[row] += s[i]
            if row == 0 or row == numRows - 1:
                direction *= -1
            row += direction

        return "".join(lines)


if __name__ == '__main__':
    sol = Solution()
    print sol.convert("PAYPALISHIRING", 3)
    print sol.convert("PAYPALISHIRING", 1)
