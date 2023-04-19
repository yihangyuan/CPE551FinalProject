

class Grid():

    """
    This class is response for generate and print a grid, 
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







class Algorithm_Tic():
    pass



class Tic_Tac_Toe():

    def __init__ (self, num_of_player):
        self.num_of_player = num_of_player
        self.info = [[0 for col in range(3)] for row in range(3)] # the matrix that store the information of grid
        self.grid = Grid()


    def is_valid_move(self, row, col):
         
         if 0 <= row < 3 and 0 <= col < 3 and self.info[row][col] == 0:
            return True
         
         return False
    
    

    def play_with_human(self):
        current_player = "X"

        while True:
            self.grid.draw_grid()
            print(f"Player {current_player}, make your move:")
            try:
                row, col = map(int, input("Enter row and column (comma separated, e.g 0,1): ").split(','))

                if current_player == "X":
                    val = -1
                else:
                    val = 1

                if self.is_valid_move(row, col):
                    self.grid[row][col] = val
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as comma separated integers.")




    def play_with_AI_(self):
        pass








def play():
    grid = create_grid()
    current_player = "X"

    while True:
        draw_grid(grid)
        print(f"Player {current_player}, make your move:")
        try:
            row, col = map(int, input("Enter row and column (comma separated): ").split(','))
            if update_grid(grid, row, col, current_player):
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as comma separated integers.")







    