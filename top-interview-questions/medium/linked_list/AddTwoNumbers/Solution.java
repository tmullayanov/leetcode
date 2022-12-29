package AddTwoNumbers;

import java.util.StringJoiner;

//* Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    static ListNode fromArray(int[] digits) {
        var node = new ListNode();

        var cur = node;
        for (var i = 0; i < digits.length; i++) {
            cur.val = digits[i];
            if (i != digits.length - 1) {
                cur.next = new ListNode();
            }
            cur = cur.next;
        }

        return node;
    }

    public String toString() {
        var joiner = new StringJoiner(", ", "[", "]");
        joiner.add(Integer.toString(this.val));
        var next = this.next;
        while (next != null) {
            joiner.add(Integer.toString(next.val));
            next = next.next;
        }

        return joiner.toString();
    }
}

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = null;
        ListNode prev = null, current = null;
        int carry = 0;
        int sum = 0;
        while (l1 != null || l2 != null) {
            int i1 = l1 == null ? 0 : l1.val;
            int i2 = l2 == null ? 0 : l2.val;

            sum = i1 + i2 + carry;
            carry = sum / 10;
            sum %= 10;

            current = new ListNode(sum);
            if (head == null) {
                head = current;
            }
            if (prev != null) {
                prev.next = current;
            }
            prev = current;

            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }

        if (carry > 0) {
            current.next = new ListNode(carry);
        }

        return head;
    }

    public static void main(String[] args) {
        System.out.println("Hello!");

        var num1 = ListNode.fromArray(new int[] { 9, 9, 9 });
        var num2 = ListNode.fromArray(new int[] { 2, 2 });

        System.out.println(num1);
        var so = new Solution();
        var sum = so.addTwoNumbers(num1, num2);
        System.out.println(sum);
    }
}