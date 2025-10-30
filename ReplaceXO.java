/*
You are given a grid[][] of size n*m, where every element is either 'O' or 'X'.
You have to replace all 'O' or a group of 'O' with 'X' that are surrounded by 'X'.
A 'O' (or a set of 'O') is considered to be surrounded by 'X' if there are 'X' at locations just below, just above, just left and just right of it.

Logic:
An 'O' should NOT be changed if:

It’s on the boundary, or

It’s connected (directly or indirectly) to an 'O' on the boundary.

Therefore:

We first mark all boundary-connected 'O's (using DFS or BFS).

Then we replace all remaining 'O's with 'X'.

Finally, we restore the temporarily marked 'O's.
*/

class Solution {
    public void fill(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        // Step 1: Mark all 'O's connected to the boundary
        for (int i = 0; i < n; i++) {
            // First and last column
            if (grid[i][0] == 'O') dfs(grid, i, 0, n, m);
            if (grid[i][m - 1] == 'O') dfs(grid, i, m - 1, n, m);
        }
        for (int j = 0; j < m; j++) {
            // First and last row
            if (grid[0][j] == 'O') dfs(grid, 0, j, n, m);
            if (grid[n - 1][j] == 'O') dfs(grid, n - 1, j, n, m);
        }

        // Step 2: Flip all remaining 'O's to 'X', and all '#' back to 'O'
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'O')
                    grid[i][j] = 'X';  // surrounded O → X
                else if (grid[i][j] == '#')
                    grid[i][j] = 'O';  // restore boundary-connected O
            }
        }
    }

    // DFS to mark connected 'O's
    private void dfs(char[][] grid, int i, int j, int n, int m) {
        if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] != 'O')
            return;

        grid[i][j] = '#'; // mark temporarily
        dfs(grid, i + 1, j, n, m);
        dfs(grid, i - 1, j, n, m);
        dfs(grid, i, j + 1, n, m);
        dfs(grid, i, j - 1, n, m);
    }
}
