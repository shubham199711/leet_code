class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        allKeySet = set([0])
        q = [x for x in rooms[0]]
        seen = set([0])
        while len(q):
            curRoom = q.pop(0)
            allKeySet.add(curRoom)
            for item in rooms[curRoom]:
                if item not in seen:
                    seen.add(item)
                    q.append(item)
        return len(allKeySet) == len(rooms)
            
        