class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        if ruleKey=="type":
            index=0
        if ruleKey=="color":
            index=1
        if ruleKey=="name":
            index=2
        s=0
        for i in items:
            if i[index]==ruleValue:
                s+=1
        return s


items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"]]
ruleKey="type"
ruleValue="phone"
first=Solution()
print(first.countMatches(items,ruleKey,ruleValue))