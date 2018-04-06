class Solution(object):

    def isPanlindrome(self, s):
        lo = 0
        hi = len(s) - 1

        while lo <= hi and s[lo] == s[hi]:
            lo += 1
            hi -= 1

        if lo >= hi:
            return True
        else:
            return False

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        window = 1
        longest = ''
        while window <= size:
            i = 0
            while i <= size - window:
                sub = s[i:i + window]
                if len(sub) >= len(longest) and self.isPanlindrome(sub):
                    longest = sub
                    break
                i += 1
            window += 1

        return longest


if __name__ == '__main__':
    cls = Solution()
    print cls.longestPalindrome('')
    print cls.longestPalindrome('babad')
    print cls.longestPalindrome('cbbd')
