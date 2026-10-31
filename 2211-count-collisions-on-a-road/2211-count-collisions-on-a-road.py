class Solution:
    def countCollisions(self, directions: str) -> int:

        

        stack= [directions[0]]
        collisions = 0

        def is_collision(prev,direction):
            if (direction==prev) or (prev=="S" and direction=="R")  or (prev=="L" and direction =="R") or (prev=="L" and direction =="S"):
                prev = direction
                return False
            return True

        for index in range(1,len(directions)):

            direction = directions[index]
            
            new_direction = direction
            is_collided = False
            while stack and  is_collision(stack[-1],new_direction):
                prev = stack.pop()

                if "S" in (prev,new_direction ):
                    collisions+=1
                else:
                    collisions+=2
                new_direction = "S"
                is_collided = True

            

            if is_collided:
                stack.clear()
                stack.append("S")
            else:
                stack.append(new_direction)




        return collisions


            


               

                    

            
        