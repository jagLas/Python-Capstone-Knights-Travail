from tree import Node

class KnightPathFinder:
    def __init__(self, pos) -> None:
        self._root = Node(pos)
        self._considered_positions = set([(pos)])

    def get_valid_moves(self, pos):
        x = pos[0]
        y = pos[1]
        
        possible_moves = set()
        # loop twice, once for x by 2 and once for y by 2
        i = 0
        while i < 2:
            # generate x's and y's
            if i == 0:
                new_xs = [x+2, x-2]
                new_ys = [y+1, y-1]
            else:
                new_xs = [x+1, x-1]
                new_ys = [y+2, y-2]
            # filter x and y's that are out of bounds
            new_xs = tuple(filter(lambda x: x >= 0 and x<8, new_xs))
            new_ys = tuple(filter(lambda y: y >= 0 and y<8, new_ys))

            # create combinations of valid squares
            for j in range(len(new_xs)):
                for k in range(len(new_ys)):
                    possible_moves.add((new_xs[j], new_ys[k]))

            i += 1
        return possible_moves
    
    def new_move_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        return valid_moves.difference(self._considered_positions)
    
    def build_move_tree(self):
        queue = [self._root]
        while len(queue):
            current_node = queue.pop(0)
            
            new_moves = self.new_move_positions(current_node.value)
            for move in new_moves:
                current_node.add_child(Node(move))
                self._considered_positions.add(move)
            for child in current_node.children:
                queue.append(child)

# knight = KnightPathFinder((0,0))
# print(knight.get_valid_moves((5,4)))
# knight._considered_positions.add((7,5))
# print(knight.new_move_positions((5,4)))
# print(knight.new_move_positions((0,0)))


# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder._root.children)