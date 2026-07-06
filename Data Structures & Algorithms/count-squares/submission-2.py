class CountSquares:

    def __init__(self):
        self.x_map = defaultdict(list)
        self.y_map = defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        self.x_map[point[0]].append(point)
        self.y_map[point[1]].append(point)

    def count(self, point: List[int]) -> int:
        # print("daant", self.x_map, self.y_map)
        count = 0
        x_points, y_points = defaultdict(list), defaultdict(list)

        for x in self.x_map:
            if x == point[0]:
                for x_point in self.x_map[x]:
                    x_points[abs(x_point[1] - point[1])].append(x_point)
        
        for y in self.y_map:
            if y == point[1]:
                for y_point in self.y_map[y]:
                    y_points[abs(y_point[0] - point[0])].append(y_point)
        # print("len_maps", x_points, y_points)
        for x_len in x_points:
            for y_point in y_points[x_len]:
                for final_point in self.x_map[y_point[0]]:
                    # same_point_skipped = False
                    for x_point in x_points[x_len]:
                        # if  and not same_point_skipped:
                        #     same_point_skipped = True
                        #     continue
                        if final_point[1] == x_point[1] and final_point != x_point:
                            # print("count+", x_len, final_point)
                            count += 1
        
        return count
                        


        
