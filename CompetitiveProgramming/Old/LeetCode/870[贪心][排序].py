class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        a=sorted([(v,idx) for idx,v in enumerate(nums2)])
        ans=[0 for _ in range(len(a))]
        jump=[]
        p=jump_p=0
        for idx in range(len(a)):
            v,i=a[idx]
            while p<len(a) and nums1[p]<=v:
                jump.append(p)
                p+=1
            if p<len(a): 
                ans[i]=nums1[p]
                p+=1
            else: 
                ans[i]=nums1[jump[jump_p]]
                jump_p+=1
        return ans