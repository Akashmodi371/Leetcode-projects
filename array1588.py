class Solution:
    def sumOddLengthSubarrays(self, arr):
        total = 0
        n = len(arr)

        for l in range(1, n + 1, 2):
            for i in range(0, n - l + 1):
                total += sum(arr[i:i + l])
        return total

arr = [1,4,2,5,3]
first=Solution()
print(first.sumOddLengthSubarrays(arr))