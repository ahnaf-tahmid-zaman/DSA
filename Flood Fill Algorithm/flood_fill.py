def perform_flood_fill(x, y, island_number):
    if x < 0 or x >= rows or y < 0 or y >= cols or visited_cells[x][y] or island_matrix[x][y] != island_number:
        return

    visited_cells[x][y] = True
    global current_island_area
    current_island_area += 1

    perform_flood_fill(x + 1, y, island_number)
    perform_flood_fill(x - 1, y, island_number)
    perform_flood_fill(x, y + 1, island_number)
    perform_flood_fill(x, y - 1, island_number)


if __name__ == "__main__":
    print("Enter the number of islands, rows, and columns (e.g., 1 1 1, use spaces to separate numbers):")
    number_of_islands, rows, cols = map(int, input().split())

    print("Enter the matrix values row by row (use spaces to separate numbers):")
    island_matrix = []
    visited_cells = []
    for i in range(rows):
        row = list(map(int, input().split()))
        island_matrix.append(row)
        visited_cells.append([False] * cols)

    largest_island_area = 0
    island_with_largest_area = -1

    for i in range(rows):
        for j in range(cols):
            if island_matrix[i][j] != 0 and not visited_cells[i][j]:
                current_island_area = 0
                perform_flood_fill(i, j, island_matrix[i][j])

                if current_island_area > largest_island_area:
                    largest_island_area = current_island_area
                    island_with_largest_area = island_matrix[i][j]

    print("The largest island is", island_with_largest_area, "with an area of", largest_island_area)
