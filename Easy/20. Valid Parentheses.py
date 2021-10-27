s = "{[]}"
# def isValid(s):
#     '''
#     Smartest way
#     '''
#     while "[]" in s or "{}" in s or "()" in s:
#         s = s.replace('[]','').replace('()','').replace('{}','')
#         return not len(s)

def isValid(s):
    '''
    O(n) way
    '''
    stack = []
    left ="{[("
    right ="}])"
    for i in s:
        if i in left:
            stack.append(i)
        if i in right:
            if len(stack) == 0:
                return False
            if right.index(i) != left.index(stack.pop()):
                return False
        print(stack)
    return not stack

def isValid_2(s):
    '''
    Another way using Mapping technique
    '''
    stack = []
    mapping = {"(":")","{":"}","[":"]"}
    for char in s:
        if char in mapping:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if mapping[stack.pop()] != char:
                return False
    return True if len(stack) == 0 else False

def isValid_3(s):
    '''
    This is solution from Leetcode
    '''
        # Also makes adding more types of parenthesis easier
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in s:

        # If the character is an closing bracket
        if char in mapping:
            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack
print(isValid_3(s))