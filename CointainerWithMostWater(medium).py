# https://leetcode.com/problems/container-with-most-water/

# my sol
def maxArea(self, heights: List[int]) -> int:
    p1 = 0
    p2 = len(heights) - 1
    maxarea = 0

    while p1 < p2:
        # width
        w = p2 - p1
        # height
        h = min(heights[p1], heights[p2])

        ar = w*h
        maxarea = max(maxarea, ar)

        # doing this so that we retain the longest height
        # if p1's height is less then increment p1
        if heights[p1] < heights[p2]:
            p1 = p1 + 1
        # vice versa
        else:
            p2 = p2 - 1
    
        
    return maxarea



# Same logic better structured sol

def maxArea(self, heights: List[int]) -> int:
    area = 0

    left = 0
    right = len(heights) - 1
    
    max_width = len(heights) - 1
    
    # for every width
    for width in range(max_width, 0, -1):
        
        # left height is shorter
        if heights[left] < heights[right]:
            # max
            area = max(area, width*heights[left])
            # only incrementing left, thus maintaining right (longer) height
            left = left + 1
        
        # right height is shorter
        else:
            # max
            area = max(area, width*heights[right])
            # only decrementing right, thus maintaining left (longer) height
            right = right - 1
    
        
    return area