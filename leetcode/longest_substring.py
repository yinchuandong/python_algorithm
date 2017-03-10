class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        max_count = 0
        start = 0
        for i in range(len(s)):
            if s[i] in table and start <= table[s[i]]:
                start = table[s[i]] + 1
            tmp_count = i - start + 1
            if tmp_count > max_count:
                max_count = tmp_count
            table[s[i]] = i
        return max_count

if __name__ == '__main__':
    cls = Solution()
    # print cls.lengthOfLongestSubstring('abcabcbb')
    # print cls.lengthOfLongestSubstring('bbbbb')
    # print cls.lengthOfLongestSubstring('pwwkew')
    # print cls.lengthOfLongestSubstring('dvdf')
    print cls.lengthOfLongestSubstring('abba')
