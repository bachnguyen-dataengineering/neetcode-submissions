class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        str_dict = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            else:
                if not stack or stack[-1] != str_dict[bracket]:
                    return False
                stack.pop()
        return len(stack) == 0