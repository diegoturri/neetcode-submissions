class Solution:
    def isValid(self, s: str) -> bool:
        # if I remove every block inside an open parenthesis, the remaining closing parenthesis must be the same type

        # I take note of all the open ones until the first close one, then if it's the same type as the last open one, I remove it ad repeat the process, if it a different type the function return false, if the open one finishes the function returns true

        # I check the caracters until I find a close one and check the last character before that if it's the right kind

        stack = []
        
        for value in s:
            if len(stack) == 0:
                stack.append(value)
                continue
            if len(stack) == 1 and (s[0] == ")" or s[0] == "]" or s[0] == "}"): # Edge case
                return False

            if value == ")":
                if stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    return False
            elif value == "]":
                if stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False
            elif value == "}":
                if stack[-1] == "{":
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(value)
        
        if len(stack) == 0: # No characters left
            return True
        else:
            return False

            