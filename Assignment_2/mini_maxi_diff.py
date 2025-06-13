class Solution(object):
    def minimizeMax(self, nums, p):
        nums.sort()
        n = len(nums)

        def can_form_pairs(x):
            count = 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= x:
                    count += 1
                    i += 2  # skip next, as both indices are now used
                else:
                    i += 1
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer


nums = [10, 1, 2, 7, 1, 3]
p = 2
num = [4, 2, 1, 2]
p1 = 1

sol = Solution()
print(sol.minimizeMax(nums, p))   # Output: 1
print(sol.minimizeMax(num, p1))   # Output depends on input
