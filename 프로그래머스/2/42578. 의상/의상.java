import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < clothes.length; i++) {
            String kind = clothes[i][1];
            if (!map.containsKey(kind)) map.put(kind, 1);
            map.put(kind, map.get(kind)+1);
        }

        int answer = 1;
        for (Integer value: map.values()) {
            answer *= value;
        }

        return answer - 1;
    }
}