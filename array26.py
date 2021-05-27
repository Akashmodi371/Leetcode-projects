class Solution:
    def removeDuplicates(self, nums):
        # answer=[]
        # new=sorted(nums)
            i=0
            length=1
            for j in range(1,len(nums)):
                if nums[j] != nums[i]:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
                    length += 1
            return length


nums = [0,0,1,1,1,2,2,3,3,4]
first=Solution()
print(first.removeDuplicates(nums))