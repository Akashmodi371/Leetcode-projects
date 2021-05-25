class Solution:
    def decompressRLElist(self, nums):
        answer=[]
        for i in range (0,len(nums),2):
            for _ in range(nums[i]):
                answer.append(nums[i+1])
        return answer

num=[1,1,2,3]
first=Solution()
print(first.decompressRLElist(num))
