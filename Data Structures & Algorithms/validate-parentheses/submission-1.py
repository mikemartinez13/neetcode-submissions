class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        cor_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                ret = stack.pop()
                if cor_dict[ret] != char:
                    return False

        if not stack:
            return True
        return False
