class Solution12:
    def isValid(self, s: str) -> bool:
        stack = []
        # mapping from closing to open parenthesis
        closeToOpenParenthesis = {")":"(", "}":"{" ,"[":"]"}
        # loop through each char in given str
        for c in s:

            if c in s :
            # if stack is not empty
            # & stack top is a closing bracket then pop
                if stack and stack[-1] == closeToOpenParenthesis[c]:
                    stack.pop()
            # closing bracket did not match so retuen false
                else:
                    return False
        # if it is a opening bracket append in stack 
            else:
                stack.append(c)
        # if stack is empty then all matched and poped otherwise unmatched so false
        return True if not stack else False
    
