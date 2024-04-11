import java.util.Arrays;
import java.util.Comparator;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book, Comparator.comparingInt(String::length));
        int minLength = phone_book[0].length();
        
        Set<String> set = new HashSet<>();
        for (String phone: phone_book) {
            StringBuffer sb = new StringBuffer(phone.substring(0, minLength-1));
            for (int i = minLength-1; i < phone.length(); i++) {
                String cur = sb.toString();
                if (set.contains(cur)) return false;
                sb.append(phone.charAt(i));
            }
            String last = sb.toString();
            set.add(last);
        }
        return true;
    }
}