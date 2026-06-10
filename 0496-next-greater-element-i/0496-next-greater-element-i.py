class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    t=nums1[i]
                    for k in range(j+1,len(nums2)):
                        if nums2[k]>nums2[j]:
                            t=max(t,nums2[k])
                            break
                    if t==nums1[i]:
                        ans.append(-1)
                    else:
                        ans.append(t)
        return ans

        