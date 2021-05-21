class solution:

    def shuffle(self,nums,n):
         answer=[]
         for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i+n])
         return answer


num=[1,2,3,4,5,6]
first=solution()
print(first.shuffle(num,3))
