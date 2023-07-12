from tree import Node

class KnightPathFinder:
    def __init__(self, pos) -> None:
        self._root = Node(pos)
        self._considered_positions = set([(pos)])

    def get_valid_moves(self, pos):
        x = pos[0]
        y = pos[1]
        
        possible_moves = set()
        i = 0
        while i < 2:
            if i == 0:
                new_xs = [x+2, x-2]
                new_ys = [y+1, y-1]
            else:
                new_xs = [x+1, x-1]
                new_ys = [y+2, y-2]
            new_xs = tuple(filter(lambda x: x >= 0 and x<8, new_xs))
            new_ys = tuple(filter(lambda y: y >= 0 and y<8, new_ys))
            print(new_xs)
            print(new_ys)
            for j in range(len(new_xs)):
                for k in range(len(new_ys)):
                    possible_moves.add((new_xs[j], new_ys[k]))

            i += 1
        return possible_moves


knight = KnightPathFinder((0,0))
print(knight.get_valid_moves((5,4)))