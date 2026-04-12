class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction = {"L":(-1,0),"R":(1,0),"U":(0,1),"D":(0,-1)}
        current_x,current_y = 0,0
        for move in moves:
            direction_x,direction_y = direction[move]
            current_x,current_y = current_x+direction_x, current_y+direction_y

        if current_x==0 and current_y==0:
            return True
        return False

        