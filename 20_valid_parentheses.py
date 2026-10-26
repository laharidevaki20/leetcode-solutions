class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(0,len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (s[i] == ")" and top != "(") or \
                   (s[i] == "]" and top != "[") or \
                   (s[i] == "}" and top != "{"):
                    return False
        return len(stack) == 0