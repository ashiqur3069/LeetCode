class Solution:
    def largestSubmatrix(self, matrix):
        ones = [[] for _ in range(len(matrix))]
        for j in range(len(matrix[0])):
            dp = 0
            for i in range(len(matrix)):
                if matrix[i][j] == 0:
                    dp = 0
                else:
                    dp += 1
                ones[i].append(dp)
        ans = 0
        for i in range(len(ones)):
            ones[i].sort(reverse=True)
            row_ans = 0
            for j in range(len(ones[i])):
                row_ans = max(row_ans, ones[i][j] * (j + 1))
            ans = max(ans, row_ans)

        return ans
