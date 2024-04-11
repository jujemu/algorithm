/*
N 마리 중 반 가져갈 수 있다.
원소 중에 같은 것이 있다.
반을 가져가면서 가장 많은 종류의 원소를 가져가고 싶다.

입력
nums.length <= 10_000
num <= 200_000
*/

class Solution {
    public int solution(int[] nums) {
        int unique = 0;
        int[] check = new int[200_001];
        for (int num: nums) {
            if (check[num] == 0) {
                check[num]++;
                unique++;
            }
        }
        
        return nums.length / 2 > unique ? unique : nums.length / 2;
    }
}