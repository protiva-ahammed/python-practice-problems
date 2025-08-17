from typing import List


class Solution8:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums)-1 

        while left <= right :
            mid = ((right - left )//2)+left
            if nums[mid] < target :
                left = mid + 1
            elif nums[mid] > target :
                right = mid - 1
            else :
                return mid

        return -1
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = r 

        while l<=r:
            mk = (l+r)//2
            totalTime=0
            for pile in piles:
                totalTime += math.ceil(pile / mk)

            if totalTime <= h:
                res = min(res,mk) 
                r = mk - 1
            else:
                l = mk + 1
        return res
         