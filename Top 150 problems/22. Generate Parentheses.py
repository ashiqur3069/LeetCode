class Solution(object):
    def generateParenthesis(self, n):
        '''
        stack = []
        result = []

        def backtrack(openN,closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return result
        '''

        result = []

        def dfs(left, right, path):
            if left == 0 and right == 0:
                result.append(path)
            if left > 0:
                dfs(left-1, right, path + "(")
            if right > 0 and right > left:
                dfs(left, right-1, path + ")")
        
        dfs(n, n, "")
        return result
