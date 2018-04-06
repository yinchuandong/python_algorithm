class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0

        max_count = 0
        count = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    count[i] = 2 + (count[i - 2] if i - 2 >= 0 else 0)
                    max_count = count[i] if count[i] > max_count else max_count
                else:
                    if i - count[i - 1] - 1 >= 0 and s[i - count[i - 1] - 1] == "(":
                        count[i] = count[i - 1] + 2 + (count[i - count[i - 1] - 2] if i - count[i - 1] - 2 >= 0 else 0)
                        max_count = count[i] if count[i] > max_count else max_count
        return max_count


if __name__ == '__main__':
    sol = Solution()
    print sol.longestValidParentheses("(()())")
    print sol.longestValidParentheses(")))()")
    print sol.longestValidParentheses("()(())()")
