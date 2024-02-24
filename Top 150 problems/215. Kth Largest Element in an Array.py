class Solution(object):
                                               # Using quickselct but one learge testcase dont work
   '''
    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p > k: return quickSelect(l,p-1)
            elif p < k: return quickSelect(p+1,r)
            else: return nums[p]
        return quickSelect(0,len(nums)-1)

  '''
  #                                                         using heap
    import heapq
    def findKthLargest(self, nums, k):
        pq = []
    
        for i in range(len(nums)):
            heapq.heappush(pq, -1 * nums[i])
    
        l = k - 1
        while l > 0:
            heapq.heappop(pq)
            l = l - 1
    
        return -1 * pq[0]
