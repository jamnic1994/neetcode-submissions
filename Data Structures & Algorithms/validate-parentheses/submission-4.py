class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ")":"(",
            "]":"[",
            "}":"{",
        }   

        stack = []

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False

                if stack.pop() != pairs[char]:
                    return False

        return not stack

