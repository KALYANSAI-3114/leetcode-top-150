class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # Index for placing non-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
