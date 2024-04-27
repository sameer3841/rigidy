def printGrid(grid, rowNum, colNum):
    for r in range(rowNum):
        print(("+----" * colNum) + "+")
        for c in range(colNum):
            print("| " + grid[r][c], end=" ")
        print("|")
    print(("+----" * colNum) + "+")


if __name__ == "__main__":
    print("Welcome to Kam's Grid Bracing Analyzer")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    braces = [['  ' for _ in range(cols)] for _ in range(rows)]

    while True:
        row = int(input("Enter index for row (or type -1 if finished bracing): "))
        if row == -1:
            break
        col = int(input("Enter column index now: "))
        braces[row][col] = '\\\\'

    printGrid(braces, rows, cols)