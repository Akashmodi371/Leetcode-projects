class Solution:
    def smallerNumbersThanCurrent(self,nums):
        no=sorted(nums)
        answer=[]
        for i in nums:
            answer.append(no.index(i))
        return answer

num=[6,5,4,8]
first=Solution()
print(first.smallerNumbersThanCurrent(num))

