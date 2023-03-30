import bisect
class SORTracker:

    def __init__(self):
        self.locations = []        
        self.rank = 0
        
    def add(self, name: str, score: int) -> None:
        bisect.insort(self.locations, (-1 * score, name))

    def get(self) -> str:
        output = self.locations[self.rank]
        self.rank += 1
        return output[1]
    