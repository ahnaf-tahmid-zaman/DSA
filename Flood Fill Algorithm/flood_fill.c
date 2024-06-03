#include <stdio.h>

#define MAX_ROWS 100
#define MAX_COLS 100

int island_matrix[MAX_ROWS][MAX_COLS];
int visited_cells[MAX_ROWS][MAX_COLS];
int rows, cols, number_of_islands;
int current_island_area;

void perform_flood_fill(int x, int y, int island_number) {
    if (x < 0 || x >= rows || y < 0 || y >= cols || visited_cells[x][y] || island_matrix[x][y] != island_number) {
        return;
    }

    visited_cells[x][y] = 1;
    current_island_area++;

    perform_flood_fill(x + 1, y, island_number);
    perform_flood_fill(x - 1, y, island_number);
    perform_flood_fill(x, y + 1, island_number);
    perform_flood_fill(x, y - 1, island_number);
}

int main() {
    printf("Enter the number of islands, rows, and columns (e.g., 1 1 1, use spaces to separate numbers):\n");
    scanf("%d %d %d", &number_of_islands, &rows, &cols);

    printf("Enter the matrix values row by row (use spaces to separate numbers):\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &island_matrix[i][j]);
            visited_cells[i][j] = 0; // Initialize visited cells to 0 (unvisited)
        }
    }

    int largest_island_area = 0;
    int island_with_largest_area = -1;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (island_matrix[i][j] != 0 && !visited_cells[i][j]) { // If it's part of an island and not visited
                current_island_area = 0; // Reset current island area counter
                perform_flood_fill(i, j, island_matrix[i][j]); // Start flood fill

                if (current_island_area > largest_island_area) { // Check if we found a bigger island
                    largest_island_area = current_island_area; // Update largest island area
                    island_with_largest_area = island_matrix[i][j]; // Update island number
                }
            }
        }
    }

    printf("The largest island is %d with an area of %d.\n", island_with_largest_area, largest_island_area);

    return 0;
}
