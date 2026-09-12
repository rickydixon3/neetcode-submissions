class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #We can loop over the entire 2D array and create sets to check for
        #duplicates, if we find one we can return false
        #But that doesnt guarantee theres a duplicate in a 3x3 square
        #First we should probably figure out how to do the row, column
        #duplicate check

        seen = set()

        #check for duplicates in rows
        
        #iterate through board
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                #Create tuples that represents if there is a specific
                #number in that square, column, or board

                row_item = (r, num)
                col_item = (num, c)
                # Each square coordinate can be represented by 
                #col // 3 & row // 3 since theres 9 squares and its
                # a 9x9 grid
                square_item = (r // 3, c // 3, num)

                # checking if its in the set
                if row_item in seen or col_item in seen or square_item in seen:
                    return False

                seen.add(row_item)
                seen.add(col_item)
                seen.add(square_item)

        return True

        