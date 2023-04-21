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
    
    

    
    def bestMove(self, board, player):
        ## this function return the bestMove location
        move = None
        bestScore = float('-inf');
        for row in range(len(board)):
            for col in range(len(row)):
                if board[row][col] == 0:
                    board[row][col] = player
                    score =  self.minimax(row,col, isMaximizing=False)
                    board[row][col] = 0
                if score > bestScore:
                    bestScore = score
                    move = (row, col)
                    
        return move
    
    
    #     let scores = {
    #     X: 10,
    #     O: -10,
    #     tie: 0
    #     };
    
    def checkWinner(self, board):
        
        t = 3 * val
        
        checked_row = sum(self.grid[row])
        checked_col = sum([r[col] for r in self.grid ])
        checked_diag = sum([self.grid[i][i] for i in range(3)])
        checked_anti_diag = sum([self.grid[i][2-i] for i in range(3)])
        
        if checked_row == t or checked_col == t or checked_diag == t or checked_anti_diag == t:
            return True
        
        return False 
        
        pass
        
    def minimax(row,col,isMaximizing=True):
        # this function compute the minimax score for the given location
        
    



    
    

    

    # function minimax(board, depth, isMaximizing) {
    # let result = checkWinner();
    # if (result !== null) {
    #     return scores[result];
    # }

    # if (isMaximizing) {
    #     let bestScore = -Infinity;
    #     for (let i = 0; i < 3; i++) {
    #     for (let j = 0; j < 3; j++) {
    #         // Is the spot available?
    #         if (board[i][j] == '') {
    #         board[i][j] = ai;
    #         let score = minimax(board, depth + 1, false);
    #         board[i][j] = '';
    #         bestScore = max(score, bestScore);
    #         }
    #     }
    #     }
    #     return bestScore;
    # } else {
    #     let bestScore = Infinity;
    #     for (let i = 0; i < 3; i++) {
    #     for (let j = 0; j < 3; j++) {
    #         // Is the spot available?
    #         if (board[i][j] == '') {
    #         board[i][j] = human;
    #         let score = minimax(board, depth + 1, true);
    #         board[i][j] = '';
    #         bestScore = min(score, bestScore);
    #         }
    #     }
    #     }
    #     return bestScore;
    # }
    # }

    




class Tic_Tac_Toe():

    def __init__ (self, num_of_player):
        self.num_of_player = num_of_player
        self.memory = [[0 for col in range(3)] for row in range(3)] # the matrix that store the information of grid
        self.grid = Grid()
        self.AI = Algorithm_Minimax()


    def is_valid_move(self, row, col):
         
         if 0 <= row < 3 and 0 <= col < 3 and self.info[row][col] == 0:
            return True
         
         return False
    
    def win_check(self, row, col, val):
        
        t = 3 * val
        
        checked_row = sum(self.grid[row])
        checked_col = sum([r[col] for r in self.grid ])
        checked_diag = sum([self.grid[i][i] for i in range(3)])
        checked_anti_diag = sum([self.grid[i][2-i] for i in range(3)])
        
        if checked_row == t or checked_col == t or checked_diag == t or checked_anti_diag == t:
            return True
        
        return False      
        
    
    def board_check(self):
        for row in self.grid:
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
                    


                if self.is_valid_move(row, col):
                    
                    self.memory[row][col] = val # set the value to memory
                    self.grid.update_grid(row,col,val)
                    self.grid.draw_grid() # show grid for this move
                    
                    if self.win_check(row, col, val) is True: # win check
                        print(f"{current_player} won!")
                        break
                        
                    
                    if self.board_check() is True: # board check
                        print("draw!")
                        break
                    
                    current_player = "O" if current_player == "X" else "X" # run this if move is valid
                else:
                    print("Invalid move. Try again.")
                    
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as comma separated integers.")
                
                
                    
                    
                
                
                
            
            
            
    













    