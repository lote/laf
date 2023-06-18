def generate_lassfaf_pattern(rows, columns):
    pattern = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if (i + j) % 2 == 0:
                pattern[i][j] = 1

    return pattern

def print_lassfaf_pattern(pattern):
    for row in pattern:
        for col in row:
            if col == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()

# Adjust the size of the pattern here
rows = 8
columns = 8

lassfaf_pattern = generate_lassfaf_pattern(rows, columns)
print_lassfaf_pattern(lassfaf_pattern)
