import java.util.ArrayDeque;

public class ValidateBST {
  public static void main(String[] args) {
    var treeSimple = TreeNode.of(
        3,
        TreeNode.of(
            1, null, TreeNode.of(2)),
        TreeNode.of(5, TreeNode.of(4), TreeNode.of(6)));

    var inst = new ValidateBST();
    System.out.println(inst.isValidBST(treeSimple));

    var leetCodeTestTree = TreeNode.of(0, TreeNode.of(-1), null);
    System.out.println(inst.isValidBST(leetCodeTestTree));
  }

  public boolean isValidBST(TreeNode root) {

    var lefts = new ArrayDeque<TreeNode>();
    var rights = new ArrayDeque<TreeNode>();

    return isValidSubBST(root, lefts, rights);
  }

  private boolean isValidSubBST(TreeNode root, ArrayDeque<TreeNode> lefts, ArrayDeque<TreeNode> rights) {

    boolean valueOk = lefts.stream().allMatch(left -> left.val > root.val)
        && rights.stream().allMatch(right -> right.val < root.val);
    if (!valueOk) {
      return false;
    }

    lefts.add(root);
    var leftSubtreeOk = root.left == null || isValidSubBST(root.left, lefts, rights);

    lefts.removeLast();
    rights.add(root);
    var rightSubtreeOk = root.right == null || isValidSubBST(root.right, lefts, rights);

    rights.remove(root);

    return leftSubtreeOk && rightSubtreeOk;
  }

  class Solution {
    public boolean validate(TreeNode root, Integer low, Integer high) {

      if (root == null) {
        return true;
      }
      if ((low != null && root.val <= low) || (high != null && root.val >= high)) {
        return false;
      }
      return validate(root.right, root.val, high) && validate(root.left, low, root.val);
    }

    public boolean isValidBST(TreeNode root) {
      return validate(root, null, null);
    }
  }

}

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode() {
  }

  TreeNode(int val) {
    this.val = val;
  }

  TreeNode(int val, TreeNode left, TreeNode right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }

  static TreeNode of(int val, TreeNode left, TreeNode right) {
    return new TreeNode(val, left, right);
  }

  static TreeNode of(int val) {
    return new TreeNode(val);
  }
}