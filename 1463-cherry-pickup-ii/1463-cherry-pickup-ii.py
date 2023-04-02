from itertools import product
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def calc_next_move(robot_coord, move_code):
            direction = moves_to_direction_map[move_code]
            i, k = robot_coord
            x, y = direction
            return (i+x, k+y)
        
        def gen_next_move(robot1, robot2):
            for move_code1, move_code2 in possible_moves:
                robot1_nxt = calc_next_move(robot1, move_code1)
                robot2_nxt = calc_next_move(robot2, move_code2)
                yield (robot1_nxt, robot2_nxt)
        
        def get_grid_value(coord):
            i, k = coord
            return grid[i][k]
        
        @lru_cache(maxsize=None)
        def dfs(robot1, robot2):
            if (robot1[0] == robot2[0] == m) or (robot1[1] in (-1, n)) or (robot2[1] in (-1, n)):
                return 0
            
            max_result = max(dfs(robot1_nxt, robot2_nxt) for robot1_nxt, robot2_nxt in gen_next_move(robot1, robot2))
            if robot1 == robot2:
                result = max_result + get_grid_value(robot1)
            else:
                result = max_result + get_grid_value(robot1) + get_grid_value(robot2)
                
            return result
            
        m, n = len(grid), len(grid[0])
        possible_moves = tuple((x, y) for x, y in product(range(3), repeat=2))
        moves_to_direction_map = {0: (1, -1), 1: (1, 0), 2: (1, 1)}
        cache = {}
        
        robot1_start = (0, 0)
        robot2_start = (0, n-1)
        
        return dfs(robot1_start, robot2_start)