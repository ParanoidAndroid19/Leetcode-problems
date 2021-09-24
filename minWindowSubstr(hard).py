# https://leetcode.com/problems/minimum-window-substring/

def minWindow(s, match):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    p1 = 0
    p2 = len(match)
    # initial value of output string will be s, as it cannot be more than s length
    op = s
    # because the min length of the substr cannot be any less than the match str
    sub = s[p1:p2]

    flag = 0

    # dict to keep a count of chars in match string
    m = {}

    # to take care of duplicates
    for char in match:
        m[char] = m.get(char, 0) + 1

    # dict to keep a count of chars in substr
    sd = {}

    for char in sub:
        sd[char] = sd.get(char, 0) + 1

    # going till the end of s
    while p2 <= len(s):
        sub = s[p1:p2]

        # this means substr has equal or more chars than match string (including duplicates)
        # so we record this substr (if it's less than output string)
        # and try to shrink the substr further (since we want the smallest substr)
        # flag to keep a track if any substr ever satisfied the condition, if not then output str will be ""
        if helper(m, sd) == True:
            flag = 1

            if len(sub) < len(op):
                op = sub

            # shrink window, adjust the substr dict char count accordingly
            # shrinking involves moving p1 forward, so reducing the count of char at p1
            sd[s[p1]] = sd.get(s[p1], 0) - 1
            p1 = p1 + 1

        else:
            # substr has less chars than necessary, 
            # it does not have all chars (including dups) present in match str
            # making sure p2 is not exceeding range, since using it as index in s
            if p2 < len(s):
                sd[s[p2]] = sd.get(s[p2], 0) + 1
            # expanding the substr to include more chars
            # expanding involves moving p2 forward, so increasing the count of char at p2
            p2 = p2 + 1


    # flag to keep a track if any substr ever satisfied the condition, if not then output str will be ""
    if flag == 0:
        return ""

    return op


def helper(m, sd):
    # calculating for every substr (sd dict)
    for char in m:
        # eg: if match str has dd then s should have at least 2 d's
        if m[char] > sd.get(char, 0):
            # substr has less chars than necessary, expand
            return False

    return True
