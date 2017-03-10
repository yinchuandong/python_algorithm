class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        table = {}
        for i in range(len(nums)):
            if (target - nums[i]) in table:
                return [table[target - nums[i]], i]
            else:
                table[nums[i]] = i
        return []

if __name__ == '__main__':
    cls = Solution()
    print cls.twoSum([2, 7, 11, 15], 9)