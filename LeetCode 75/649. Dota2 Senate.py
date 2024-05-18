class Solution(object):
    def predictPartyVictory(self, senate):
        senate = list(senate)
        D, R = deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            dturn = D.popleft()
            rturn = R.popleft()

            if rturn < dturn:
                R.append(dturn+ len(senate))
            else:
                D.append(rturn + len(senate))
        return "Radiant" if R else "Dire"
        
