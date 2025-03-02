class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        arr = []
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l][0] == nums2[r][0]:
                arr.append([nums1[l][0], (nums1[l][1] + nums2[r][1])])
                l += 1
                r += 1
            elif nums1[l][0] < nums2[r][0]:
                arr.append(nums1[l])
                l += 1
            elif nums1[l][0] > nums2[r][0]:
                arr.append(nums2[r])
                r += 1
            # print(arr)
        
        while l < len(nums1):
            arr.append(nums1[l])
            l += 1
        while r < len(nums2):
            arr.append(nums2[r])
            r += 1
        return arr