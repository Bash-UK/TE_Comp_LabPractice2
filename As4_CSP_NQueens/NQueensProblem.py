class NQueensProblem:
    def NQueens(self,n) -> list[list[str]]:
        col = set()         # for verticle attacking
        posDiag =set()      # for positive diag (down-up)
        negDiag = set()     # for negative diag (up-down)
        res =[]
                 

        board = [["."]*n for i in range(n)]         # board init
        print(board)
         # Start search of solution in top-bottom and left-right approach from 0th row and increament subsequently
        def backtrack(r):
            
            if r==n:
                copyBoard = ["".join(row) for row in board] # if board successfully reaches nth row solution found 
                                                            # then join all rows for making it as single solution
                res.append(copyBoard)                       # append solution to list of possible solutions
                return
            for c in range(n):      # for loop for initial column for queen for each backtrack solution set
                if c in col or (r+c) in posDiag or (r-c) in negDiag: #check for conflicting column or diagonal indices already present in any of the 
                                                                    #attacked indices that are mention in any of the above set
                    continue
                

                # Place the queen if index non attacked position
                board[r][c] = "Q"
                print(f"Board at : {count}")
                print(board)

                # Add column to attacking set
                col.add(c)   
                print("col:")
                print(col)    
                
                # Add positive diagonal to attacking set
                posDiag.add(r+c)
                print("Pos Diag:")
                print(posDiag)

                # Add negative diag to attacking set
                negDiag.add(r-c)
                print("Neg Diag:")
                print(negDiag)
              
              # repeat for next row upto n-1
                backtrack(r+1)    # Go check for next row with 

            # if there is no possible unattacked position in next row 
            # then drop this incomplete solution 
            # And clear all sets of attacking position (col,posdiag,negdiag) 
            # also remove all the queens from board
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
                print("BAcktrack ended ....") # go to for loop for initial column and 
                                            #  try for another next column as initial column 



        backtrack(0) # start the search from 0th row
        return res  # return the set of all possible solution for problem



