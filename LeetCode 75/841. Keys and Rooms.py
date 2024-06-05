class Solution(object):
    def canVisitAllRooms(self, rooms):
        q = deque()
        visited = set()
        q.append(0)

        while q:
            for i in range(len(q)):
                roomNum = q.popleft()

                if roomNum not in visited:
                    foundKey = rooms[roomNum]

                    for key in foundKey:
                        q.append(key)
                    visited.add(roomNum)
        return len(visited) == len(rooms) 
