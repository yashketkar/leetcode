class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif stack and ((c == ')' and stack[-1] == '(') or (c == ']' and stack[-1] == '[') or (c == '}' and stack[-1] == '{')):
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
