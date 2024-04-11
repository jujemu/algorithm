/*
입력
participant.length <= 100_000
*/
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < completion.length; i++) {
            String p = participant[i], c = completion[i];
            if (!map.containsKey(p)) map.put(p, 0);
            if (!map.containsKey(c)) map.put(c, 0);

            map.put(p, map.get(p) + 1);
            map.put(c, map.get(c) - 1);
        }
        
        String lastElement = participant[participant.length-1];
        if (!map.containsKey(lastElement)) return lastElement;
        else map.put(lastElement, map.get(lastElement)+1);
            
        for (String key : map.keySet()) {
            if (map.get(key) > 0) return key;
        } return "뿡이다";
    }
}