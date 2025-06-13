class Solution(object):
    def canMakeEqual(self, nums, k):
        n = len(nums)
        flips = 0
        arr = nums[:]
        for i in range(n-1):
            if arr[i] != arr[0]:

                arr[i] *= -1
                arr[i+1] *= -1
                flips += 1

        if all(x == arr[0] for x in arr):
            return flips <= k
        else:
            return False


nums1 = [1, -1, 1, -1, 1]
nums2 = [-1, -1, -1, 1, 1, 1]
k1 = 3
k2 = 5
s = Solution()
print(s.canMakeEqual(nums1, k1))
print(s.canMakeEqual(nums2, k2))
