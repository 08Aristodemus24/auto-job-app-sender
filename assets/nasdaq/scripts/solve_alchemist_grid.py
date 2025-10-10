from typing import List

def solve(grid: List[List[int]], rules: List[dict]) -> List[List[int]]:
    n_rows = len(grid)
    n_cols = len(grid[-1])

    row_res = []
    for i in range(n_rows - 1):

        col_res = []
        for j in range(n_cols - 1):
            # this flag represents a pattern that has not
            # yet been found while in the current window
            flag = False

            # extract values of window
            top_left = grid[i][j]
            top_right = grid[i][j + 1]
            bottom_left = grid[i + 1][j]
            bottom_right = grid[i + 1][j + 1]

            # retrieve current window and compare it
            # against any existing pattern in the rules list
            window = [top_left, top_right, bottom_left, bottom_right]
            print(window)
            for rule in rules:
                if rule["pattern"] == window:
                    col_res.append(rule["result"])
                    flag = True

            # # if flag is not set to true or pattern has not
            # # been found then just append a 0 to the end
            if not flag:
                col_res.append(0)

        
        row_res.append(col_res)

    return row_res

    



if __name__ == "__main__":
    rules = [
        {"pattern": [1, 1, 4, 1], "result": 3},
        {"pattern": [1, 1, 1, 4], "result": 5},
        {"pattern": [2, 2, 2, 2], "result": 10}
    ]

    grid = [
        [2, 2, 1, 2],
        [2, 2, 3, 4],
        [1, 1, 1, 4],
        [1, 4, 1, 5],
    ]

    print(solve(grid, rules))
