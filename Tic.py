import random

class Grid():

    """
    This class is responsible for generate and print a grid, 
    receive info from the input matrix, generate output gride
    
    """
    
    def __init__(self, matrix = None):

        self.grid = [[' ' for space in range(3)] for row in range(3)]

        if matrix is not None:

            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    val = matrix[row][col]
                    self.update_grid(row,col,val)


    def update_grid(self, row, col, val):
        if val == -1:
            self.grid[row][col] = "X"
        if val == 1:
            self.grid[row][col] = "O"


    def draw_grid(self):
        print("    0   1   2") # index
        print("  " + " ---" * 3)
        for i, row in enumerate(self.grid):
            row_str = "{} |".format(i) + " {} | {} | {} |".format(*row)
            print(row_str)
            print("  " + " ---" * 3)





class Algorithm_Minimax():
    
    """
    This class is for Minimax algorithm, which takes board as input, 
    compute which grid have highest possiblility for win,
    return that grid location
    
    Algorithm learned from:
    https://www.youtube.com/watch?v=trKjYdBASyQ
    
    """

    def __init__(self):
        self.scores = {-1:-10, 0:0, 1:10} # create a dictionary for score, "X" win: -10, "O" win +10
    
    

    
    def bestMove(self, board, player):
        ## this function return the bestMove location
        move = None
        bestScore = float('inf') if player == -1 else float('-inf')

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 0:
                    board[row][col] = player
                    score = self.minimax(board, row, col)
                    board[row][col] = 0
                    
                    if player == -1:
                        if score < bestScore:
                            bestScore = score
                            move = (row, col)
                    else:
                        if score > bestScore:
                            bestScore = score
                            move = (row, col)

                    
        return move
    
     
    def checkWinner(self, board, row, col):
        
        val = board[row][col]
        t = 3 * val 
        
        checked_row = sum(board[row])
        checked_col = sum([r[col] for r in board ])
        checked_diag = sum([board[i][i] for i in range(3)])
        checked_anti_diag = sum([board[i][2-i] for i in range(3)])
        
        if checked_row == t or checked_col == t or checked_diag == t or checked_anti_diag == t:
            return val # winner
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 0:
                    return None  # game go on      
        
        return 0  # Draw!

        
    def minimax(self, board, row, col):
        # this function compute the minimax score for the given location
        result = self.checkWinner(board,row,col)
        if result != None:
            return self.scores[board[row][col]]
        
        if board[row][col] == -1:

            bestScore = float('-inf')

            for r in range(len(board)):
                for c in range(len(board[r])):
                    if board[r][c] == 0:
                        board[r][c] = 1
                        score = self.minimax(board, r, c)
                        board[r][c] = 0
                        bestScore = max(score, bestScore)
        
            return bestScore


        else:

            bestScore = float('inf')

            for r in range(len(board)):
                for c in range(len(board[r])):
                    if board[r][c] == 0:
                        board[r][c] = -1
                        score = self.minimax(board, r, c)
                        board[r][c] = 0
                        bestScore = min(score, bestScore)
            
            return bestScore
        



class Tic_Tac_Toe():

    def __init__ (self, num_of_player):
        self.num_of_player = num_of_player
        self.memory = [[0 for col in range(3)] for row in range(3)] # the matrix that store the information of grid
        self.grid = Grid()
        self.AI = Algorithm_Minimax()
        self.play()


    def is_valid_move(self, row, col):
         
         if 0 <= row < 3 and 0 <= col < 3 and self.memory[row][col] == 0:
            return True
         
         return False
    
    def win_check(self, row, col, val):
        
        t = 3 * val
        
        checked_row = sum(self.memory[row])
        checked_col = sum([r[col] for r in self.memory ])
        checked_diag = sum([self.memory[i][i] for i in range(3)])
        checked_anti_diag = sum([self.memory[i][2-i] for i in range(3)])
        
        if checked_row == t or checked_col == t or checked_diag == t or checked_anti_diag == t:
            return True
        
        return False      
        
    
    def board_check(self):
        for row in self.memory:
            for col in row:
                if col ==0:
                    return False
        
        return True      
                
                
    def play(self):
        
        # playerX always go first
        
        playerX = "X"
        playerO = "O"
        
        AI_player = None
        
        if self.num_of_player == 1:
            
            AI_player = random.choice([playerX, playerO])
            
            if AI_player == playerX:
                print("AI go first")  # write something
            else:
                print("You go first") 
            
        current_player = playerX  # playerX always go first
        self.grid.draw_grid() # show grid for human player at begin
        
        
        while True:
            
            try:
                
                # get value
                if current_player == "X":
                    val = -1
                else:
                    val = 1
                
                # get row col for this turn
                if current_player == AI_player:
                    row, col = self.AI.bestMove(self.memory, val) 
                else:
                     
                    print(f"Player {current_player}, make your move:")
                    
                    next_move = input("Enter row and column separated by a comma or 'q' to quit: ")
                    
                    if next_move.lower() in ['q', 'quit']:
                        print("Game Over")
                        break
                    
                    row, col = map(int, next_move.split(','))
                    print(row,col)
                    


                if self.is_valid_move(row, col):
                    
                    self.memory[row][col] = val # set the value to memory
                    self.grid.update_grid(row,col,val)
                    self.grid.draw_grid() # show grid for this move
                    
                    if self.win_check(row, col, val) is True: # win check
                        print("player" f"{current_player} won!")
                        break
                        
                    
                    if self.board_check() is True: # board check
                        print("draw!")
                        break
                    
                    current_player = "O" if current_player == "X" else "X" # run this if move is valid
                else:
                    print("Invalid move. Try again.")
                    
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as comma separated integers.")
                
                
                    
                    
test = Tic_Tac_Toe(1)              
                
# test = Algorithm_Minimax ()

# board = [[-1,1,1],[0,1,0],[0,-1,-1]]

# result = test.bestMove([[-1,1,1],[0,1,0],[0,-1,-1]],-1)
# print(result)

            
            
            
    













    