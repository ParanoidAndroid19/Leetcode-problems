# https://leetcode.com/problems/sliding-window-maximum/

# Approach 1: using heap
# Time Complexity: O(N log N), because in worst case when nums elements are in
# increasing order, the heap may contain N elements. This is much better than the
# brute force complexity O(NK).
# Space Complexity: O(N), heap size could go up to N elements
def maxSlidingWindow(self, nums, k):
    n = len(nums)
    # base cases
    if n * k == 0:
        return []
    if k == 1:
        return nums
    
    maxHeap = []
    ans = []

    # inserting the first k eles in maxHeap
    for i in range(k):
        heappush(maxHeap, (-nums[i], i))

    ans.append(-maxHeap[0][0])

    for i in range(k, n):
        heappush(maxHeap, (-nums[i], i))

        top = maxHeap[0]

        # if index out of current window
        while top[1] < (i-k+1):
            heappop(maxHeap)
            top = maxHeap[0]

        ans.append(-maxHeap[0][0])

    return ans


# Approach 2: using deque
# Steps:
# 1. From start of deque, pop elements which lie outside of 
#    current window.
# 2. Maintain descending order, pop elements from right side
#    if they are less then current element 
# 3. Append current element.
# 4. If i >= k - 1, then push the first element from deque (largest)
#    to the answer array.

# Time Complexity: O(N)
# Space Complexity: O(N)
def maxSlidingWindow(nums, k):
    n = len(nums)
    # base cases
    if n * k == 0:
        return []
    if k == 1:
        return nums
    
    q = deque()
    q.append((nums[0], 0))
    
    ans = []
    
    for i in range(1, n):
        # step 1
        top = q[0]
        # if index out of current window, keep popping from start
        # getting rid of max elements out of the current window
        while top[1] < (i-k+1):
            q.popleft()
            top = q[0]
        
        # step 2
        last = q[-1]
        while len(q) > 0 and last[0] <= nums[i]:
            # keep popping elements from end which are less than current ele
            # directly popping elements because we only care about the 
            # max element in window
            q.pop()
            if len(q) > 0:
                last = q[-1]
        
        # step 3
        q.append((nums[i], i))
        
        # step 4
        # if window is complete, get the max element of current window
        if i >= k - 1:
            ans.append(q[0][0])
            
    
    return ans
        
        
    
print(maxSlidingWindow([7,2,4], 2))