class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        output = []
        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                end = nums[i]
            else:
                if start == end:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(end))
                start = nums[i]
                end = nums[i]
        if start == end:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(end))

        return output

                


