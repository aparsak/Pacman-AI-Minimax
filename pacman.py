import os
from os import system
from time import sleep
from random import randint


class Agent:
    def __init__(self, location):
        self.location = location

    def move_up(self):
        self.location[0] -= 1

    def move_down(self):
        self.location[0] += 1

    def move_left(self):
        self.location[1] -= 1

    def move_right(self):
        self.location[1] += 1

    def is_move_up_valid(self, map):
        if map[self.location[0] - 1][self.location[1]] != 0:
            return True
        else:
            return False

    def is_move_down_valid(self, map):
        if map[self.location[0] + 1][self.location[1]] != 0:
            return True
        else:
            return False

    def is_move_left_valid(self, map):
        if map[self.location[0]][self.location[1] - 1] != 0:
            return True
        else:
            return False

    def is_move_right_valid(self, map):
        if map[self.location[0]][self.location[1] + 1] != 0:
            return True
        else:
            return False

    def valid_moves(self, map):
        moves = []
        if self.is_move_up_valid(map):
            moves.append("up")
        if self.is_move_down_valid(map):
            moves.append("down")
        if self.is_move_left_valid(map):
            moves.append("left")
        if self.is_move_right_valid(map):
            moves.append("right")
        return moves

    def move(self, move):
        if move == "up":
            self.move_up()
        elif move == "down":
            self.move_down()
        elif move == "left":
            self.move_left()
        elif move == "right":
            self.move_right()

    def move_back(self, move):
        if move == "up":
            self.move_down()
        elif move == "down":
            self.move_up()
        elif move == "left":
            self.move_right()
        elif move == "right":
            self.move_left()


class Player(Agent):
    ...


class Ghost(Agent):
    ...

    def make_move(self, map):
        moves = self.valid_moves(map)
        move = moves[randint(0, len(moves) - 1)]
        self.move(move)


class Game:
    def __init__(self):
        self.map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.player = Player([9, 9])
        self.ghost1 = Ghost([7, 7])
        self.ghost2 = Ghost([5, 5])
        self.score = 0

    def print_map(self):
        for i in range(0, 11):
            for j in range(0, 20):
                if self.player.location == [i, j]:
                    print("P", end=" ")
                elif self.ghost1.location == [i, j]:
                    print("1", end=" ")
                elif self.ghost2.location == [i, j]:
                    print("2", end=" ")
                elif self.map[i][j] == 0:
                    print("#", end=" ")
                elif self.map[i][j] == 1:
                    print(".", end=" ")
                elif self.map[i][j] == 2:
                    print(" ", end=" ")
            print()

    def is_game_over(self):
        if all(row.count(1) == 0 for row in self.map):

            return True  
        if self.player.location == self.ghost1.location or self.player.location == self.ghost2.location:

            return True
        else:
            return False
        

    def move_player_up(self):
        if self.player.is_move_up_valid(self.map):
            self.player.move_up()
            if self.map[self.player.location[0]][self.player.location[1]] == 1:
                self.score += 10  # Add 10 to score for each point eaten
                self.map[self.player.location[0]][self.player.location[1]] = 2
                

    def move_player_down(self):
        if self.player.is_move_down_valid(self.map):
            self.player.move_down()
            if self.map[self.player.location[0]][self.player.location[1]] == 1:
                self.score += 10  # Add 10 to score for each point eaten
                self.map[self.player.location[0]][self.player.location[1]] = 2
               

    def move_player_left(self):
        if self.player.is_move_left_valid(self.map):
            self.player.move_left()
            if self.map[self.player.location[0]][self.player.location[1]] == 1:
                self.score += 10  # Add 10 to score for each point eaten
                self.map[self.player.location[0]][self.player.location[1]] = 2
               

    def move_player_right(self):
        if self.player.is_move_right_valid(self.map):
            self.player.move_right()
            if self.map[self.player.location[0]][self.player.location[1]] == 1:
                self.score += 10  # Add 10 to score for each point eaten
                self.map[self.player.location[0]][self.player.location[1]] = 2
               

    def move_player(self, depth, mode):
        movement = ""
        if mode == "minimax":
            movement = min_max(self, 0, "player_turn", depth, 0, -1000000000, +1000000000)
        if movement == "":
            raise Exception("Invalid movement")

        if movement == "up":
            self.move_player_up()
        elif movement == "down":
            self.move_player_down()
        elif movement == "left":
            self.move_player_left()
        elif movement == "right":
            self.move_player_right()

    def run_game(self, depth, mode):
        command = "clear"
        if os.name == "nt":
            command = "cls"
        itr = 0
        while not self.is_game_over():
            itr += 1
            print("Score: ", self.score - itr)
            self.print_map()
            sleep(0.05)
            self.move_player(depth, mode)
            if self.is_game_over():
                break
            self.ghost1.make_move(self.map)
            if self.is_game_over():
                break
            self.ghost2.make_move(self.map)
            sleep(0.05)
            system(command)
        os.system(command)
        print("Score: ", self.score - itr)
        self.print_map()

        return self.score, itr

    def test_run_game(self, depth, mode):
        itr = 0
        while not self.is_game_over():
            itr += 1
            self.move_player(depth, mode)
            if self.is_game_over():
                break
            self.ghost1.make_move(self.map)
            if self.is_game_over():
                break
            self.ghost2.make_move(self.map)
        return self.score, itr


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def shortest_path(map, p1):
    queue = [p1]
    visited = [p1]
    distance = {tuple(p1): 0}

    while len(queue) != 0:
        p = queue.pop(0)
        if map[p[0]][p[1]] == 1:
            return distance[tuple(p)]
        if map[p[0] - 1][p[1]] != 0 and [p[0] - 1, p[1]] not in visited:
            queue.append([p[0] - 1, p[1]])
            visited.append([p[0] - 1, p[1]])
            distance[tuple([p[0] - 1, p[1]])] = distance[tuple(p)] + 1
        if map[p[0] + 1][p[1]] != 0 and [p[0] + 1, p[1]] not in visited:
            queue.append([p[0] + 1, p[1]])
            visited.append([p[0] + 1, p[1]])
            distance[tuple([p[0] + 1, p[1]])] = distance[tuple(p)] + 1
        if map[p[0]][p[1] - 1] != 0 and [p[0], p[1] - 1] not in visited:
            queue.append([p[0], p[1] - 1])
            visited.append([p[0], p[1] - 1])
            distance[tuple([p[0], p[1] - 1])] = distance[tuple(p)] + 1
        if map[p[0]][p[1] + 1] != 0 and [p[0], p[1] + 1] not in visited:
            queue.append([p[0], p[1] + 1])
            visited.append([p[0], p[1] + 1])
            distance[tuple([p[0], p[1] + 1])] = distance[tuple(p)] + 1
    return 0


def nearest_point_manhattan_distance(map, position):
    res = 1000000000
    s = len(map)
    for i in range(s):
        for j in range(s):
            if map[i][j] == 1:
                res = min(res, manhattan_distance(position, [i, j]))
    return res


def e_utility(map, player, ghost1, ghost2, eaten_points, count_of_moves):
    ghost_distance = min(manhattan_distance(player.location, ghost1.location),
                         manhattan_distance(player.location, ghost2.location))
    point_distance = shortest_path(map, player.location)

    move_cost = -1
    point_score = 5 * (50 - point_distance)
    eaten_score = 50 * eaten_points
    
    ghost_score = ghost_distance

    if ghost_distance <= 1:
        return 10 * ghost_score + -100000

    return point_score + eaten_score + ghost_score - count_of_moves + (count_of_moves * move_cost)


def min_max(game, cur_depth, turn, target_depth, eaten_points, alpha, beta):
    if cur_depth == target_depth or game.is_game_over():
        return e_utility(game.map, game.player, game.ghost1, game.ghost2, eaten_points, count_of_moves=cur_depth)

    if turn == "player_turn":
        moves = game.player.valid_moves(game.map)
        max_eval = -1000000000
        move = ""
        for m in moves:
            flag = 0
            game.player.move(m)
            if game.map[game.player.location[0]][game.player.location[1]] == 1:
                game.score += 1
                eaten_points += 1
                game.map[game.player.location[0]][game.player.location[1]] = 2
                flag = 1

            new_val = min_max(game, cur_depth, "ghost1_turn", target_depth, eaten_points + flag, alpha, beta)

            if flag == 1:
                game.score -= 1
                eaten_points -= 1
                game.map[game.player.location[0]][game.player.location[1]] = 1
            game.player.move_back(m)
            if new_val > max_eval:
                max_eval = new_val
                move = m
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
        if cur_depth == 0:
            return move
        return max_eval

    if turn == "ghost1_turn":
        moves = game.ghost1.valid_moves(game.map)
        min_eval = +1000000000
        for m in moves:
            game.ghost1.move(m)
            new_val = min_max(game, cur_depth + 1, "ghost2_turn", target_depth, eaten_points, alpha, beta)
            game.ghost1.move_back(m)
            min_eval = min(min_eval, new_val)
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return min_eval

    if turn == "ghost2_turn":
        moves = game.ghost2.valid_moves(game.map)
        min_eval = +1000000000
        for m in moves:
            game.ghost2.move(m)
            new_val = min_max(game, cur_depth + 1, "player_turn", target_depth, eaten_points, alpha, beta)
            game.ghost2.move_back(m)
            min_eval = min(min_eval, new_val)
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return min_eval


if __name__ == "__main__":
    game = Game()
    depth = 2
    mode = "minimax"
    score, iterations = game.run_game(depth, mode)
    print("Game Over!")
    
    final_score = score - iterations
    #print("Final Score:", final_score)
    print("Total Iterations:", iterations)
