class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n,m=len(nums1),len(nums2)
        i,j=0,0
        r=[]
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                r.append(nums1[i])
                i+=1
            else:
                r.append(nums2[j])
                j+=1
        while i<n:
            r.append(nums1[i])
            i+=1
        while j<m:
            r.append(nums2[j])
            j+=1
        mid=len(r)//2
        if len(r)%2!=0:
            return r[mid]
        else:
            return (float(r[mid]+r[mid-1])/2)