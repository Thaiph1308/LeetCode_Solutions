n=3

def isValid(s):
    '''
    O(n) way
    '''
    stack = []
    left =("{[(")
    right =("}])")
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

def generateParenthesis(self, n: int) -> List[str]:
    