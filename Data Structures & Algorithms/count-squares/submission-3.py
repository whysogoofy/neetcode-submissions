class CountSquares:

    def __init__(self):
        # Maps x -> Counter(y -> count)
        # This lets us easily find all points sharing the same x-coordinate
        self.pts_map = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pts_map[x][y] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total_squares = 0
        
        # If the x-coordinate doesn't exist, no squares can be formed
        if x1 not in self.pts_map:
            return 0
            
        # Iterate over all points that share the same x-coordinate (vertical line)
        for y2, count_p2 in self.pts_map[x1].items():
            # Skip the query point itself (side length cannot be 0)
            if y2 == y1:
                continue
                
            side = abs(y1 - y2)
            
            # Case 1: Square to the right (x3 = x1 + side)
            x3_right = x1 + side
            if x3_right in self.pts_map:
                total_squares += count_p2 * self.pts_map[x3_right][y1] * self.pts_map[x3_right][y2]
                
            # Case 2: Square to the left (x3 = x1 - side)
            x3_left = x1 - side
            if x3_left in self.pts_map:
                total_squares += count_p2 * self.pts_map[x3_left][y1] * self.pts_map[x3_left][y2]
                
        return total_squares