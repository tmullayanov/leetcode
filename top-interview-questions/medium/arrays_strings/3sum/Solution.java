import java.util.*;

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        var result = new HashSet<List<Integer>>();
        for (int i = 0; i < nums.length; i++) {
            var lookup = new HashMap<Integer, Integer>();
            for (int j = i + 1; j < nums.length; j++) {
                if (lookup.containsKey(nums[j])) {
                    // why does this have to be so dubious and awkward???
                    var triplet = new ArrayList<Integer>();
                    triplet.add(nums[i]);
                    triplet.add(nums[lookup.get(nums[j])]);
                    triplet.add(nums[j]);
                    Collections.sort(triplet);
                    result.add(triplet);
                }
                var diff = -nums[i] - nums[j];
                lookup.put(diff, j);
            }
        }

        return new ArrayList<>(result);
    }

    public static void main(String[] args) {
        var s = new Solution();

        int[][] tests = {
                { -1, 0, 1, 2, -1, -4 },
                { 0, 1, 1 },
                { 0, 0, 0 }
        };

        for (int[] test : tests) {
            var result = s.threeSum(test);
            System.out.println(result);
        }

    }
}