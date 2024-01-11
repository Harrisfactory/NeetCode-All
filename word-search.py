class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        word = list(word)

        for row in range(len(board)):
            for col in range(len(board[row])):
                found: bool = self.dfs(board, row, col, [], word, 0, [])
                if found:
                    return True
        return False

    def dfs(self, board, row, col, b, word, word_ctr, positions_used):
        #check all bounds and fails
            #if the row column pair has been used already
            #if board position does not equal current char were looking for
            #if cur row is lower than boards length
            #if cur row is above the board
            #if cur col is the right of the board
            #if cur col is to the left of the board

        #need to account for words we already hit
        if [row,col] in positions_used or row > len(board) - 1 or row < 0 or col > len(board[row]) - 1 or col < 0 or board[row][col] != word[word_ctr]:
            return False
        #add candidate
        if board[row][col] == word[word_ctr] and [row,col] not in positions_used:
            b.append(board[row][col])
            positions_used.append([row,col])
        
        #win condition
        if b == word:
            return True
        
        #move to next char
        word_ctr+=1

        if self.dfs(board, row - 1, col, b, word, word_ctr, positions_used):
            return True
        if self.dfs(board, row + 1, col, b, word, word_ctr, positions_used):
            return True
        if self.dfs(board, row, col - 1, b, word, word_ctr, positions_used):
            return True
        if self.dfs(board, row, col + 1, b, word, word_ctr, positions_used):
            return True
        
        #remove candidate
        b.pop()
        positions_used.pop()

        return False
         
