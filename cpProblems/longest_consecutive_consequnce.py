from typing import List


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet =  set(nums)
        longest = 0

        for n in nums:
            #checking if the start of a sequence
            #if not then create a new sequence
            if(n-1) not in numSet:
                length=0
                while(n+length) in numSet:
                    length +=1
                longest=max(length,longest)

                
        return longest

        