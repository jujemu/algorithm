import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int length = queue1.length;
        int totalLength = length * 2;
        
        Queue<Integer> q1 = new LinkedList<Integer>();
        Queue<Integer> q2 = new LinkedList<Integer>();
        
        long sum1 = 0, sum2 = 0;
        for (int i=0; i<length; i++) {
            q1.add(queue1[i]);
            q2.add(queue2[i]);
            
            sum1 += queue1[i];
            sum2 += queue2[i];
        }
        
        int answer = 0;
        int maxAnswer = totalLength * 2 + 1;
        while (answer < maxAnswer) {
            if (sum1 < sum2) {
                sum1 += q2.peek();
                sum2 -= q2.peek();
                
                q1.add(q2.poll());
                
                answer++;
            } else if (sum1 > sum2) {
                sum1 -= q1.peek();
                sum2 += q1.peek();
                
                q2.add(q1.poll());
                
                answer++;
            } else {
                return answer;
            }
        }
        
        return -1;
    }
}