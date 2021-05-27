class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        count=0
        i=0
        j=0
        k=0
        while i<len(arr)-2:
            j=i+1
            while j<len(arr)-1:
                k=j+1
                while k<len(arr):
                    if (abs(arr[i] - arr[j])<= a) and (abs(arr[j] - arr[k])<= b) and (abs(arr[i] - arr[k])<= c):
                        count=count+1
                    k=k+1
                j=j+1
            i=i+1
        return count

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
first=Solution()
print(first.countGoodTriplets(arr,a,b,c))
