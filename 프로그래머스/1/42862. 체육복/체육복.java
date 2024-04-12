import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        boolean[] pluses = new boolean[n+1];
        for (int i: reserve) pluses[i] = true;
        
        Arrays.sort(lost);
        int answer = n - lost.length;
        for (int i = 0; i < lost.length; i++) {
            int curLost = lost[i];
            if (pluses[curLost]) {
                pluses[curLost] = false;
                lost[i] = 0;
                answer++;
            }
        }
        
        for(int i: lost) {
            if (i == 0) continue;
            
            if (pluses[i-1]) {
                pluses[i-1] = false;
                answer++;
                continue;
            }
            
            if (i != n && pluses[i+1]) {
                pluses[i+1] = false;
                answer++;
            }
        }
        
        return answer;
    }
}