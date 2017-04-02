class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == 0 and len2 == 0:
            return 0.0

        i = j = 0
        arr = []
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        if i < len1:
            arr.extend(nums1[i:])
        else:
            arr.extend(nums2[j:])

        print arr
        size = len(arr)
        if len(arr) % 2 == 0:
            return (arr[size / 2] + arr[size / 2 - 1]) / 2.0
        else:
            return arr[size / 2]


if __name__ == '__main__':
    s = Solution()
    # nums1 = [1, 2]
    # nums2 = [3]
    nums1 = []
    nums2 = []
    r = s.findMedianSortedArrays(nums1, nums2)
    print r
