class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []
        
        for num in nums1:
            found = False
            for i in range(nums2.index(num), len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    found = True
                    break
            if not found:
                result.append(-1)
        
        return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

s = Solution()
print(s.nextGreaterElement(nums1, nums2))
