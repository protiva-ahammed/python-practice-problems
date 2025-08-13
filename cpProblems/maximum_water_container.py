from typing import List


class Solution6:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1 , len(heights)):
                res = max(res, min(heights[i],heights[j])*(j-i))
        return res
    

    def maxAreaTwoPointer(self, heights: List[int]) -> int:
        res = 0
        l , r = 0,len(heights) - 1
        while l < r :
            res = max(res, min(heights[l],heights[r])*(r-l))
            if heights[l] < heights[r]:
                l += 1
            else :
                r -=1
        return res