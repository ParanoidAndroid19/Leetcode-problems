def isValid(s):
    stack = []
    d = {"]":"[", "}":"{", ")":"("}

    for b in s:
        # bracket is open
        if b in d.values():
            stack.append(b)

        # bracket is close
        elif b in d.keys():
            # here since I'm first checking if stack is empty, won't get error
            # while stack.pop()
            # close bracket with no corresponding open in stack then false
            if stack == [] or d[b] != stack.pop():
                return False
        else:
            return False

    # true if stack is empty
    return stack == []


print(isValid("()[]{}"))