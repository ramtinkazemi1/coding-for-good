class Solution:
    def maxArea(self, height: List[int]) -> int:
        #height = [1,8,6,2,5,4,8,3,7]   ans = 49
        # two pointers

        left = 0
        right = len(height)-1
        max_area = 0
        # area = min(p2 , p1) *  (p2 - p1)
        # area formula =  max(area, ((min(height[right] , height[left])) *  (right - left))

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area