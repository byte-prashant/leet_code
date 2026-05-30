class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        total = len(mat)* len(mat[0])
        top = (0,0)
        ans = []
        flip = True
        while total>0:

            ele = top
            temp = []
            while ele[1]>=0 and ele[0]<len(mat):
                temp.append(mat[ele[0]][ele[1]])
                total-=1
                ele= (ele[0]+1,ele[1]-1)
            
            if flip:
                temp = temp[::-1]
            ans.extend(temp)

            new_top = (top[0],top[1]+1)
            if new_top[1]>=len(mat[0]):
                new_top = (top[0]+1,top[1])
            top = new_top
            flip= not flip
        return ans





        