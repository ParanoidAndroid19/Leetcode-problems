from collections import deque

class HitCounter(object):

    def __init__(self):
        self.counter = deque()
        self.total = 0
        
    # Time complexity: O(1)
    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        # assume that calls are being made to the system in chronological order
        # so timestamp of the hit could be the same as last hit or a new timestamp
        # new timestamp 
        if len(self.counter) == 0 or self.counter[-1][0] != timestamp:
            self.counter.append([timestamp, 1])
        
        # add to existing timestamp
        else:
            self.counter[-1][1] = self.counter[-1][1] + 1
        
        # since at a time only 1 hit is recorded
        self.total = self.total + 1
        

    # Time complexity: O(N)
    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        while len(self.counter) != 0:
            # diff = 301 - 1 = 300
            diff = timestamp - self.counter[0][0]
            
            if diff >= 300:
                # removing the hit count of the oldest timestamp from total
                self.total = self.total - self.counter[0][1]
                # removing the oldest timestamp
                self.counter.popleft()
            else:
                break
                
        return self.total
