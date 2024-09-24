class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ranges = []
        _min = _max =  nums[0]
        count = nums[0]
        for num in nums:
            print(num, count)
            if num == count:
                count+=1
                _max = num
            else:
                if _min ==_max:
                    ranges.append(str(_min))
                else:
                    ranges.append(str(_min)+"->"+str(_max))
                _min = num
                _max = num
                count = num+1
        
        if _min ==_max:
            ranges.append(str(_min))
        else:
            ranges.append(str(_min)+"->"+str(_max))

        return ranges
            
            

    def summaryRanges(self, nums: List[int]) -> List[str]:

        ans = []
        i = 0
        while(i<len(nums)):
            start = i
            while(i< len(nums)-1 and nums[i]+1 ==nums[i+1]):
                i+=1

            if start == i:
                ans.append(str(nums[start]))
            else:
                print(str(nums[start])+"->"+str(nums[i]))
                ans.append(str(nums[start])+"->"+str(nums[i]))

            i+=1

        return ans
