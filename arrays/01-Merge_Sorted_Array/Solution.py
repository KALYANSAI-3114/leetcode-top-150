class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None. Do not return anything, modify nums1 in-place instead.
        """
        # Step 1: Copy the first m elements of nums1
        temp = nums1[:m]
        
        # Step 2: Combine with nums2
        temp.extend(nums2)
        
        # Step 3: Sort the combined array
        temp.sort()
        
        # Step 4: Write back into nums1 in-place
        for i in range(m + n):
            nums1[i] = temp[i]
