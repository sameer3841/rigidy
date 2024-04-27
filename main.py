def printGrid(grid, rowNum, colNum):
    for r in range(rowNum):
        print(("+----" * colNum) + "+")
        for c in range(colNum):
            print("| " + grid[r][c], end=" ")
        print("|")
    print(("+----" * colNum) + "+")


def find_eulerian_circuit(graph):
    if not enough_braces(graph):
        return None
    circuit = []
    while circuit:
        vertex = circuit[0]
        for neighbor in graph[vertex]:
            if neighbor not in circuit:
                circuit.append(neighbor)
                break
        else:
            circuit.pop()
    return circuit


def enough_braces(graph):
    num_of_brace = []
    for r in graph:
        for c in r:
            if c == '\\\\':
                num_of_brace.append('\\\\')
    return len(num_of_brace) <= (len(graph) + len(graph[0]))


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
    isRigid = find_eulerian_circuit(braces)
    if isRigid is None:
        print("This graph is not rigid")
    else:
        print("This graph passes rigidity")
