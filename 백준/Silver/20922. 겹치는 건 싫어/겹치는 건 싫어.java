import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Sol {

    public int solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int K = Integer.parseInt(input[1]);

        input = br.readLine().split(" ");
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(input[i]);
        }

        int maxLength = 0, curLength = 0;
        int[] cnt = new int[100_001];
        int p1 = 0;
        for (int p2 = 0; p2 < N; p2++) {
            curLength++;
            int right = numbers[p2];
            cnt[right]++;
            while (cnt[right] > K) {
                int left = numbers[p1++];
                cnt[left] -= 1;
                curLength--;
            }

            if (maxLength < curLength) {
                maxLength = curLength;
            }
        }

        return maxLength;
    }
}

public class Main {

    public static void main(String[] args) throws Exception {
        Sol sol = new Sol();
        System.out.println(sol.solution());
    }
}
