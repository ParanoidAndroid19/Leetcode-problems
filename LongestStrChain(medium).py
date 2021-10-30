# https://leetcode.com/problems/longest-string-chain/

# Approach 1: bottom up splution

def longestStrChain(words):

    # order words according to the word length
    words = sorted(words, key=lambda x: len(x))

    # global max
    longest = 1

    # where the key is word and value is the length of chain that ends at word
    # eg: {b: 1, ab: 2}
    dp = {}

    for word in words:
        # local max
        presentLen = 1

        # for deleting ith char of word to check if the chain length
        # of it's predecessor word (since the difference b/w current
        # and predecessor word is just one char)
        for i in range(0, len(word)):
            # removing the ith char
            pre = word[:i] + word[i+1:]

            # how long the chain is for predecessor word (current word 
            # with ith char missing)
            prevLen = dp.get(pre, 0)

            # include or exclude the predecessor word, depending on it's 
            # chain length
            # prevLen+1, because prevLen is for predecessor word
            # and +1 for the current word
            presentLen = max(presentLen, prevLen+1)

        # recording the calculated presentLen for current word
        dp[word] = presentLen

        # global max
        longest = max(longest, presentLen)

    return longest


