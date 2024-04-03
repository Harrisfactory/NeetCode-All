class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pascals_triangle = []
        #initialize the triangle
        for i in range(numRows):
            #initialize empty row of correct length
            t_row = [0] * (i + 1)
            t_row[0] = 1
            t_row[len(t_row) - 1] = 1
            pascals_triangle.append(t_row)
        
        #starting on the first full row with elements that need changing
        for i in range(2, len(pascals_triangle)):
            for j in range(len(pascals_triangle[i])):
                #compute from two above if true
                if pascals_triangle[i][j] == 0:
                    pascals_triangle[i][j] = pascals_triangle[i-1][j] + pascals_triangle[i-1][j-1]

        return pascals_triangle