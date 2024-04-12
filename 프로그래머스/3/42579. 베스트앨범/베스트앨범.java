import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, List<List<Integer>>> genresToMusic = new HashMap<>();
        Map<String, Integer> cnt = new HashMap<>();
        for (int i = 0; i < plays.length; i++) {
            if (!cnt.containsKey(genres[i])) cnt.put(genres[i], 0);
            cnt.put(genres[i], cnt.get(genres[i])+plays[i]);

            if (!genresToMusic.containsKey(genres[i])) {
                genresToMusic.put(genres[i], new ArrayList<>());
            }
            genresToMusic.get(genres[i]).add(List.of(plays[i], i));
        }

        for (String key: genresToMusic.keySet()) {
            List<List<Integer>> result = (genresToMusic.get(key).stream()
                                          .sorted(
                                              Comparator.comparing((list) -> -list.get(0))
                                          )
                                          .collect(Collectors.toList()));
            genresToMusic.put(key, result);
        }

        List<Integer> answer = new ArrayList<>();
        List<Integer> integers = new ArrayList<>(cnt.values());
        integers.sort(Collections.reverseOrder());
        HashMap<Integer, String> cntToGenres = new HashMap<>();
        for (String key : cnt.keySet()) {
            cntToGenres.put(cnt.get(key), key);
        }

        for (int c : integers) {
            String g = cntToGenres.get(c);
            List<List<Integer>> arr = genresToMusic.get(g);
            List<Integer> first = arr.get(0);
            if (arr.size() == 1) answer.add(first.get(1));
            else {
                List<Integer> second = arr.get(1);
                if (second.get(0).equals(first.get(0))) {
                    if (second.get(1) > first.get(1)) answer.addAll(List.of(first.get(1), second.get(1)));
                    else answer.addAll(List.of(second.get(1), first.get(1)));
                } else {
                    answer.addAll(List.of(first.get(1), second.get(1)));
                }
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}