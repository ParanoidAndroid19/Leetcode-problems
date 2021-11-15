# https://leetcode.com/problems/top-k-frequent-words/

from heapq import *

class Freq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            # this step is important!
            # since we need word with lower aplha order first in FINAL RESULT
            # and this Final result will be achieved by reversing the temp result array
            # SO HERE, we return self.word>other.word instead of self.word<other.word 
            return self.word > other.word
        else:
            return self.freq < other.freq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        minHeap = []
        count = {}
        res = []
        
        for word in words:
            count[word] = count.get(word, 0) + 1
            
        for word in count:
            heappush(minHeap, Freq(word, count[word]))
            
            if len(minHeap) > k:
                heappop(minHeap)
                
        while len(minHeap) > 0:
            # so that every time the minimum freq word is appended first
            res.append(heappop(minHeap).word)
        
        # then we just reverse it
        return res[::-1]