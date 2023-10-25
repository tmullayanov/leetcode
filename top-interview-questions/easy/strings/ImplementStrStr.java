public class ImplementStrStr {

  public static void main(String[] args) {
    var s = new Solution();

    System.out.printf("res=%d, expected=%d\n", s.strStr("sadbutsad", "sad"), 0);
    System.out.printf("res=%d, expected=%d\n", s.strStr("leetcode", "sad"), -1);
    System.out.printf("res=%d, expected=%d\n", s.strStr("badbutsad", "sad"), 6);
    System.out.printf("res=%d, expected=%d\n", s.strStr("badbutsad123", "sad"),
        6);

    System.out.println("============");
    var haystack = "mississippi";
    var needle = "issip";
    System.out.printf("res=%d, expected=%d\n", s.strStr(haystack, needle), 4);
  }
}

// naive O(n*m) solution
class Solution {
  public int strStr(String haystack, String needle) {
    if (needle.isBlank()) {
      return -1;
    }

    for (int haystackPos = 0; haystackPos <= haystack.length() - needle.length(); haystackPos++) {
      int needlePos = 0;

      while (needlePos < needle.length() && haystack.charAt(haystackPos + needlePos) == needle.charAt(needlePos)) {
        needlePos++;
      }

      if (needlePos == needle.length()) {
        return haystackPos;
      }
    }

    return -1;
  }
}
