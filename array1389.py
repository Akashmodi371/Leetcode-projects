class Solution:
    def createTargetArray(self, nums,index):
        target=[]
        for i in range(len(index)):
            target[index[i]:index[i]] = [nums[i]]
        return target

num = [0,1,2,3,4]
index = [0,1,2,2,1]
first=Solution()
print(first.createTargetArray(num,index))