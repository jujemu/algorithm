import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        System.out.println(solution.solution());
    }
}

class Solution {
    int solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int M = Integer.parseInt(input[0]);
        int N = Integer.parseInt(input[1]);

        int remainingTomatoes = 0;
        Queue<Integer[]> q = new LinkedList<>();
        int[][] grid = new int[N][M];
        for (int i = 0; i < N; i++) {
            input = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                int cur = Integer.parseInt(input[j]);
                if (cur == 1) q.add(new Integer[]{i, j, 0});
                if (cur == 0) remainingTomatoes++;
                grid[i][j] = cur;
            }
        };

        int answer = 0;
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        boolean[][] visited = new boolean[N][M];
        while (!q.isEmpty()) {
            Integer[] cur = q.poll();
            int x = cur[0], y = cur[1], cnt = cur[2];

            if (answer < cnt) answer = cnt;
            for (int d = 0; d < 4; d++) {
                int nx = x + directions[d][0];
                int ny = y + directions[d][1];
                if (canPush(nx, N, ny, M, visited, grid)) {
                    visited[nx][ny] = true;
                    remainingTomatoes--;
                    q.add(new Integer[]{nx, ny, cnt + 1});
                }
            }
        }

        return remainingTomatoes == 0 ? answer : -1;
    }

    private boolean canPush(int nx, int N, int ny, int M, boolean[][] visited, int[][] grid) {
        return 0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny] && grid[nx][ny] == 0;
    }
}