class CountAndSay {
    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }

        String previousSolution = countAndSay(n - 1);

        int curr_count = 1;
        char curr_sym = previousSolution.charAt(0);
        StringBuilder builder = new StringBuilder();

        for (int i = 1; i < previousSolution.length(); i++) {
            var s = previousSolution.charAt(i);
            if (curr_sym == s) {
                curr_count++;
            } else {
                builder.append(curr_count).append(curr_sym);
                curr_count = 1;
                curr_sym = s;
            }
        }

        builder.append(curr_count).append(curr_sym);

        return builder.toString();
    }

    public static void main(String[] args) {
        Test[] tests = new Test[] {
                Test.of(1, "1"),
                Test.of(2, "11"),
                Test.of(3, "21"),
                Test.of(4, "1211"),
                Test.of(5, "111221"),
                Test.of(6, "312211")
        };

        var solution = new CountAndSay();

        for (var test : tests) {
            var result = solution.countAndSay(test.n);
            System.out.printf("Test:: n=%d, AU=%s result=%s\n", test.n, test.expected, result);
            System.out.printf("Test:: %s\n", result.equals(test.expected) ? "OK" : "FAIL");
        }
    }

    public static class Test {
        public final int n;
        public final String expected;

        public Test(int n, String expected) {
            this.n = n;
            this.expected = expected;
        }

        public static Test of(int n, String expected) {
            return new Test(n, expected);
        }
    }
}
