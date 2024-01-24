class Solution:
    def isvalid(self,board,x,y,visited):
        return (x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and (x,y) not in visited)
    
    def explore(self,board, x, y, word,visited):
        moves = [(0,1),(0,-1),(1,0),(1,-1)]

        if (len(word) == 0):
            return True
        for m in moves: 
            if(self.isvalid(board, x+m[0], y+m[1] ,visited) and board[x+m[0]][y+m[1]] == word[0]):
                visited.add((x+m[0], y+m[1]))
                if (self.explore(board,x+m[0], y+m[1], word[1:],visited)):
                    return (True)
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for x in range(len(board)):
            for y in range(len(board[0])):
                if (board[x][y] == word[0]):
                    visited = set()
                    if (self.explore(board,x,y,word[1:],visited)):
                        return (True)
        return (False)