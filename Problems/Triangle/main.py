height = int(input())
triangle = ['#' * (x + 1) for x in range(0, (height * 2 - 1), 2)]
for lines in triangle:
    print(lines.center(height * 2 - 1))
