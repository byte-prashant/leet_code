class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # def dfs(x,y, inital_colour, new_colour):


        #     if x>=0 and x< len(image) and y>=0 and y<len(image[0]) and image[x][y]== inital_colour:

        #         image[x][y] = new_colour


        #         dfs(x+1,y,inital_colour, new_colour)
        #         dfs(x-1,y,inital_colour, new_colour)
        #         dfs(x,y+1,inital_colour, new_colour)
        #         dfs(x,y-1,inital_colour, new_colour)

        # x,y = sr,sc
        # if sr>=0 and sr< len(image) and sc>=0 and sc<len(image[0]) and image[x][y]!= color  :
        #     initial_colour = image[x][y]
        #     #image[x][y]= color
        #     dfs(x,y,initial_colour, color)

        # return image



        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        src_color = image[sr][sc]

        queue = [(sr,sc)]
        visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        while queue:
            
            x, y = queue.pop()

            image[x][y] = color
            visited[x][y] = True
            for dx, dy in directions:
                new_x,new_y = x+dx,y+dy
                if  new_x>=0 and new_x<len(image) and new_y>=0 and new_y<len(image[0]) and not visited[new_x][new_y] and image[new_x][new_y] == src_color:
                    queue.append((new_x,new_y))

        return image





        