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

    public List<List<Integer>> threeSumInnerPointers(int[] nums) {
        var result = new ArrayList<List<Integer>>();

        Arrays.sort(nums);
        var n = nums.length;
        for (int start = 0; start < n - 2; start++) {
            if (nums[start] > 0) {
                break;
                // it's sorted, so we won't have -nums[start] as a sum in a right subarray
            }

            if (start > 0 && nums[start] == nums[start - 1]) {
                continue; // we already covered this, skip
            }

            int low = start + 1, high = n - 1;

            while (low < high) {
                var sum = nums[low] + nums[high] + nums[start];
                if (sum > 0) {
                    high--;
                } else if (sum < 0) {
                    low++;
                } else {
                    var triplet = new ArrayList<Integer>();
                    triplet.add(nums[start]);
                    triplet.add(nums[low]);
                    triplet.add(nums[high]);
                    result.add(triplet);

                    int last_low = nums[low], last_high = nums[high];
                    while (low < high && nums[low] == last_low) {
                        low++;
                    }
                    while (low < high && nums[high] == last_high) {
                        high--;
                    }

                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        var s = new Solution();

        int[][] tests = {
                { -1, 0, 1, 2, -1, -4 },
                { 0, 1, 1 },
                { 0, 0, 0 },
                { 0, 0, 0, 0, 0, -1, 1 }
        };

        for (int[] test : tests) {
            var result = s.threeSumInnerPointers(test);
            System.out.println(result);
        }

    }
}