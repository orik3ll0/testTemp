def find_match(grid, word, x, y, nrow, ncol, level):
    l = len(word)

    # word matched
    if (level == l):
        return True

    # Out of Boundary
    if (x < 0 or y < 0 or x >= nrow or y >= ncol):
        return False

    # If grid matches with a letter while recursion
    if (grid[x][y] == word[level]):

        # Visited cell
        temp = grid[x][y]
        grid[x].replace(grid[x][y], "#")

        # finding word in 6 directions( Horizontally, Vertically, Diagonally )
        res = (find_match(grid, word, x - 1, y, nrow, ncol, level + 1) |
               find_match(grid, word, x + 1, y, nrow, ncol, level + 1) |
               find_match(grid, word, x, y - 1, nrow, ncol, level + 1) |
               find_match(grid, word, x, y + 1, nrow, ncol, level + 1) |
               find_match(grid, word, x+1, y + 1, nrow, ncol, level + 1) |
               find_match(grid, word, x-1, y + 1, nrow, ncol, level + 1))

        # marking this cell as unvisited again
        grid[x].replace(grid[x][y], temp)
        return res
    else:
        return False


def check_match(grid, word, nrow, ncol):
    word_length = len(word)

    # check if word related to grid size
    if (word_length > nrow or word_length > ncol):
        return False

    for i in range(nrow):
        for j in range(ncol):
            # If first letter matches, then recur and check
            if (grid[i][j] == word[0]):
                if (find_match(grid, word, i, j, nrow, ncol, 0)):
                    return True
    return False


# Driver Code
if __name__ == "__main__":

    grid = ["ABS",
            "DCE",
            "DFA"]

    nrow = len(grid)
    ncol = len(grid[0])

    my_word = input("Type 3 letters: ")

    # Checking if word exists or not
    if (check_match(grid, my_word.upper(), nrow, ncol)):
        print(True)
    else:
        print(False)
