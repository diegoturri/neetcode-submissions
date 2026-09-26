class Solution:
    def isValid(self, s: str) -> bool:
        # if I remove every block inside an open parenthesis, the remaining closing parenthesis must be the same type

        # I take note of all the open ones until the first close one, then if it's the same type as the last open one, I remove it ad repeat the process, if it a different type the function return false, if the open one finishes the function returns true

        # I check the caracters until I find a close one and check the last character before that if it's the right kind

        stack = []
        h_map = {"}":"{", "]":"[", ")":"("}

        for value in s:
            if not stack and value in h_map:
                return False

            if value in h_map:
                if stack[-1] == h_map[value]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(value)
                
        return True if not stack else False