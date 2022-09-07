def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
    @lru_cache
    def recurMemo(s: str, word_dict: Set[str], start: int):
        if start == len(s):
            return True
        
        for end in range(start + 1, len(s) + 1):
            # so here both possibilities cat and cats for str catsanddog
            if s[start:end] in word_dict and recurMemo(s, word_dict, end):
                return True
            
        return False
    
    # set lookup is constant
    return recurMemo(s, frozenset(wordDict), 0)
    
    
    # basically we may have to make choice, between splitting the string using cat or cats for example
    # for catsanddog
    
    # dp = {3: ["pen"], 5: ["apple"]}
#         dp = {}
#         for word in wordDict:
#             l = len(word)
#             if l in dp:
#                 dp[l].append(word)
#             else:
#                 dp[l] = [word]
            
    
#         while len(s) > 0:
#             # if len(s) not in dp:
#             #     return False
#             for end in dp:
#                 for word in dp[end]:
#                     substr = s[0:end]
#                     if substr == word:
#                         s = s[end:]
#                         if s == "":
#                             return True
                
    
    
    