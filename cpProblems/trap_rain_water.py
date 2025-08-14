from typing import List


class Solution7:
    def trapRainWaterUsingTwoPointer(self, height: List[int]) -> int:

        if not height: return 0
        l,r =0,len(height)-1
        leftMax,rightMax = height[l],height[r]
        res=0

        while l<r:
            if leftMax < rightMax :
                l+=1
                leftMax = max(leftMax,height[l])
                res +=leftMax - height[l]#above line already ensure leftmax is larger

            else:
                r-=1
                rightMax = max(rightMax , height[r])
                res +=rightMax-height[r]

        return res


        