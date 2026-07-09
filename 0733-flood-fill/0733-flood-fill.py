class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(x,y, inital_colour, new_colour):


            if x>=0 and x< len(image) and y>=0 and y<len(image[0]) and image[x][y]== inital_colour:

                image[x][y] = new_colour


                dfs(x+1,y,inital_colour, new_colour)
                dfs(x-1,y,inital_colour, new_colour)
                dfs(x,y+1,inital_colour, new_colour)
                dfs(x,y-1,inital_colour, new_colour)

        x,y = sr,sc
        if sr>=0 and sr< len(image) and sc>=0 and sc<len(image[0]) and image[x][y]!= color  :
            initial_colour = image[x][y]
            #image[x][y]= color
            dfs(x,y,initial_colour, color)

        return image


        