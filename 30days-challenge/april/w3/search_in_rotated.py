class Solution():
    def search(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[start]:
                if target >= nums[start] or target <= nums[mid]:
                    end = mid - 1
                    continue
            else:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                    continue

            if nums[end] < nums[mid]:
                if target >= nums[mid] or target <= nums[end]:
                    start = mid + 1
                    continue
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                    continue
            return -1

        return -1


class AlternativeSolution:
    def search(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
