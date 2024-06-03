# What is the Flood Fill Algorithm?
Imagine you have a grid (a big rectangle made of smaller squares) and some of those squares have numbers. These numbers represent islands, and each island is made up of squares with the same number. We want to find the biggest island, which means the group of connected squares with the same number.

## Steps of the Flood Fill Algorithm
1. Choose a Starting Point:

    * Find a square that is part of an island (a square with a number other than 0).
2. Check Boundaries:

    * Make sure we don't go outside the grid.
    * Ensure that we haven't already visited this square.
    * Confirm that the square belongs to the island we're currently exploring.
3. Color the Square:

    * Mark the current square as visited by changing its value or keeping track in a separate list.
    * Increase our count of squares for this island.
4. Explore Neighboring Squares:

    * Look at the squares directly above, below, to the left, and to the right of the current square.
    * Repeat the process for each of these squares if they belong to the same island.
## Simple Example
Imagine a 4x4 grid where:

* `0` represents water
* Numbers like `1` and `2` represent different islands

Here's the grid:
```
0 0 0 1
0 0 1 1
0 0 0 2
2 2 2 2
```
We want to find the biggest island. Let's use the flood fill algorithm to do this.

1. Choose a Starting Point:

    * We start at the first 1 we find, which is at position (0, 3).
2. Check Boundaries and Color the Square:

    * The square (0, 3) is part of the island 1, so we mark it as visited and increase the island count to 1.
    * We then look at its neighbors (0, 2), (1, 3), and so on.
3. Explore Neighboring Squares:

    * (1, 3) is 1, so we mark it as visited and increase the island count to 2.
    * (1, 2) is also 1, so we mark it as visited and increase the island count to 3.
    * (0, 2) and (0, 1) are 0, so we stop exploring in those directions.
4. Move to the Next Island:

    * After exploring all connected squares for the island 1, we move on to the next island 2.
5. Repeat the Process:

    * Start at (2, 3), the first 2 we find.
    * (2, 3) is part of island 2, so we mark it as visited and increase the island count to 1.
    * Explore (2, 2), (3, 3), and so on, marking them as visited and counting them.
    * Eventually, we find the entire island 2 and count its size, which is 5 squares.

By the end of this process, we compare the sizes of the islands we found:

* Island 1 has a size of 3 squares.
* Island 2 has a size of 5 squares.

So, the biggest island is 2 with an area of 5 squares.

# Code Explanation
## C
```
#include <stdio.h>
```
This line includes the standard input/output library, which provides functions like `printf()` and `scanf()`.
```
#define MAX_ROWS 100
#define MAX_COLS 100
```
These lines define constants `MAX_ROWS` and `MAX_COLS` with values 100 each. These constants are used to specify the maximum number of rows and columns in the matrix.
```
int island_matrix[MAX_ROWS][MAX_COLS];
int visited_cells[MAX_ROWS][MAX_COLS];
```
These lines declare two 2D arrays: island_matrix and visited_cells. island_matrix stores the input matrix representing islands, where each element is either 0 (water) or a positive integer (part of an island). visited_cells keeps track of visited cells during the flood fill operation.
```
int rows, cols, number_of_islands;
int current_island_area;
```
These lines declare variables to store the number of rows (rows), the number of columns (cols), the total number of islands (number_of_islands), and the current island area being calculated (current_island_area).
```
void perform_flood_fill(int x, int y, int island_number) {
```
This line declares a function named perform_flood_fill. It's a recursive function that performs flood fill starting from the cell (x, y) for the given island_number.

```
    if (x < 0 || x >= rows || y < 0 || y >= cols || visited_cells[x][y] || island_matrix[x][y] != island_number) {
        return;
    }
```
This block checks if the current cell (x, y) is within the bounds of the matrix, if it has been visited before, and if it belongs to the current island being explored. If any of these conditions are not met, the function returns without further exploration.

```
    visited_cells[x][y] = 1;
    current_island_area++;
```
These lines mark the current cell as visited and increment the current island's area count.

```
    perform_flood_fill(x + 1, y, island_number);
    perform_flood_fill(x - 1, y, island_number);
    perform_flood_fill(x, y + 1, island_number);
    perform_flood_fill(x, y - 1, island_number);
```
These lines recursively call the perform_flood_fill function for the adjacent cells (up, down, left, right) of the current cell, continuing the flood fill operation.

```
int main() {
```
This line declares the main function, which is the entry point of the program.

```
    printf("Enter the number of islands, rows, and columns (e.g., 1 1 1, use spaces to separate numbers):\n");
    scanf("%d %d %d", &number_of_islands, &rows, &cols);
```
These lines prompt the user to input the number of islands, rows, and columns. The scanf function reads these values from the standard input and stores them in the corresponding variables.

```
    printf("Enter the matrix values row by row (use spaces to separate numbers):\n");
```
This line prompts the user to input the matrix values row by row.

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &island_matrix[i][j]);
            visited_cells[i][j] = 0; // Initialize visited cells to 0 (unvisited)
        }
    }

These nested loops read the matrix values from the user input and initialize the visited_cells array to 0 (unvisited) for each cell.

    int largest_island_area = 0;
    int island_with_largest_area = -1;
These lines declare variables to store the largest island area found and the corresponding island number.

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (island_matrix[i][j] != 0 && !visited_cells[i][j]) {
                current_island_area = 0;
                perform_flood_fill(i, j, island_matrix[i][j]);

                if (current_island_area > largest_island_area) {
                    largest_island_area = current_island_area;
                    island_with_largest_area = island_matrix[i][j];
                }
            }
        }
    }
These nested loops iterate through each cell of the matrix. If the cell belongs to an island and has not been visited, the flood fill operation is performed from that cell. If the area of the current island is larger than the previously recorded largest island area, it updates the largest island area and the corresponding island number.

    printf("The largest island is %d with an area of %d.\n", island_with_largest_area, largest_island_area);

This line prints the island number and its corresponding area, which represents the largest island found in the matrix.

```
    return 0;
}
```
This line ends the main function and returns 0, indicating successful execution of the program.

## Python
### Function: perform_flood_fill
```
def perform_flood_fill(x, y, island_number):
    if x < 0 or x >= rows or y < 0 or y >= cols or visited_cells[x][y] or island_matrix[x][y] != island_number:
        return
```
1. Function Definition:

* `perform_flood_fill(x, y, island_number)`: This is a recursive function that performs a flood fill (a form of depth-first search) to find the extent of an island in the matrix.
* Parameters:
    * `x`, `y`: The coordinates of the current cell being processed.
    * `island_number`: The value representing the current island in the matrix.
2. Boundary and Base Case Check:

* `if x < 0 or x >= rows or y < 0 or y >= cols`: Checks if the current coordinates are out of bounds.
* `or visited_cells[x][y]`: Checks if the current cell has already been visited.
* `or island_matrix[x][y] != island_number`: Checks if the current cell is not part of the current island.
* If any of these conditions are true, the function returns immediately, stopping the recursion.
```
    visited_cells[x][y] = True
    global current_island_area
    current_island_area += 1
```
3. Mark Cell as Visited:

* `visited_cells[x][y] = True`: Marks the current cell as visited to avoid reprocessing.
4. Increment Island Area:

* `global current_island_area`: Declares `current_island_area` as a global variable, allowing it to be modified within the function.
* `current_island_area += 1`: Increments the area of the current island.
```
    perform_flood_fill(x + 1, y, island_number)
    perform_flood_fill(x - 1, y, island_number)
    perform_flood_fill(x, y + 1, island_number)
    perform_flood_fill(x, y - 1, island_number)
```
5. Recursive Calls:
* These four lines recursively call `perform_flood_fill` for the neighboring cells (down, up, right, left). This ensures that all connected cells of the current island are processed.
### Main Code Block
```
if __name__ == "__main__":
    print("Enter the number of islands, rows, and columns (e.g., 1 1 1, use spaces to separate numbers):")
    number_of_islands, rows, cols = map(int, input().split())
```
1. Main Guard:

* `if __name__ == "__main__"`: ensures that the code inside this block only runs if the script is executed directly (not imported as a module).
2. Input Prompt:

* `print("Enter the number of islands, rows, and columns (e.g., 1 1 1, use spaces to separate numbers):")`: Asks the user for input.
* `number_of_islands, rows, cols = map(int, input().split())`: Reads the input, splits it by spaces, and converts each part to an integer, assigning them to `number_of_islands`, `rows`, and `cols`.
```
    print("Enter the matrix values row by row (use spaces to separate numbers):")
    island_matrix = []
    visited_cells = []
    for i in range(rows):
        row = list(map(int, input().split()))
        island_matrix.append(row)
        visited_cells.append([False] * cols)
```
3. Matrix Input:
* Prompts the user to enter the matrix values.
* Initializes `island_matrix` and `visited_cells` as empty lists.
* For each row, reads the input, splits it into integers, and appends it to `island_matrix`.
* Also appends a corresponding row of `False` values to `visited_cells`, indicating that no cells have been visited yet.
```
    largest_island_area = 0
    island_with_largest_area = -1
```
4. Initialize Tracking Variables:
* `largest_island_area = 0`: Keeps track of the largest island area found.
* `island_with_largest_area = -1`: Keeps track of the island number with the largest area.
```
    for i in range(rows):
        for j in range(cols):
            if island_matrix[i][j] != 0 and not visited_cells[i][j]:
                current_island_area = 0
                perform_flood_fill(i, j, island_matrix[i][j])

                if current_island_area > largest_island_area:
                    largest_island_area = current_island_area
                    island_with_largest_area = island_matrix[i][j]
```
5. Processing Each Cell:
* Nested loops iterate over each cell in the matrix.
* `if island_matrix[i][j] != 0 and not visited_cells[i][j]`: Checks if the cell is part of an island (non-zero) and has not been visited.
* `current_island_area = 0`: Resets the current island area before starting the flood fill.
* `perform_flood_fill(i, j, island_matrix[i][j])`: Initiates the flood fill from the current cell.
* `if current_island_area > largest_island_area`: Updates the largest island area and the corresponding island number if a larger island is found.
```
    print("The largest island is", island_with_largest_area, "with an area of", largest_island_area)
```
6. Output:
* Prints the number of the largest island and its area
### Summary
This script finds and prints the largest island in a given matrix. It uses a recursive flood fill algorithm to explore each island and keep track of the visited cells. The main logic ensures that each island is processed once, and the largest one is identified based on its area.