class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # set up our two pointers
        # basically have a area variable where
        # we do max(area, currentArea)
        #while we move our two pointers through the array
        left = 0
        right = len(heights) - 1
        max_area = -1

        while left < right:
            # set up height & width for area
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            max_area = max(area, max_area)

            # moving pointers
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return max_area
        


        