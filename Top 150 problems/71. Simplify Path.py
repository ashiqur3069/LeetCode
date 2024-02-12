class Solution(object):
    def simplifyPath(self, path):
        stack = [] 
        path = path.split("/")
        for curr in path:
            if not curr or curr == ".": 
                continue
            elif curr == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(curr)
        return "/" + "/".join(stack)
