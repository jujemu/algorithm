/*
팀 크기에 제한이 없다.
프로젝트를 함께할 팀원을 선택한다.
단 한명의 팀원을 선택한다.
자기 자신을 선택할 수 있다.

팀 결성 조건
1. 한 명의 팀원으로 구성되어, 자기 자신을 선택하거나
2. 신발끈으로 이어져 마지막 팀원이 첫 팀원을 선택하는 경우

한 원소에서 시작한 신발끈이 중간에 완성되면, 완성되지 않은 앞부분은 폐기
그러니깐 한 원소는 1. 아직 방문하지 않았거나 2. 폐기 3. 완성 상태를 가진다.

 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Solution solution = new Solution(br);
        StringBuffer sb = new StringBuffer();

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            sb.append(solution.solution()).append("\n");
        }
        System.out.println(sb);
    }
}

class Solution {

    BufferedReader br;

    Solution(BufferedReader br) {
        this.br = br;
    }

    int solution() throws IOException {
        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(number
                        -> Integer.parseInt(number)-1)
                .toArray();

        int result = 0;
        boolean[] visited = new boolean[n];
        for (int idx = 0; idx < n; idx++) {
            if (!visited[idx]) {
                result += dfs(new ArrayList<>(List.of(idx)), idx, numbers, visited);
            }
        }

        return n - result;
    }

    int dfs(List<Integer> members, int cur, int[] numbers, boolean[] visited) {
        visited[cur] = true;
        int partner = numbers[cur];

        if (visited[partner]) {
            int indexOfPartner = members.indexOf(partner);
            return indexOfPartner >= 0 ? members.size() - indexOfPartner : 0;
        }

        members.add(partner);
        return dfs(members, partner, numbers, visited);
    }
}