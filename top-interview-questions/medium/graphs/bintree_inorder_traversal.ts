class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function inorderTraversalRecursive(root: TreeNode | null): number[] {
  function inorder(node: TreeNode): number[] {
    // concise but maybe slow and memory-consuming due to copying elems
    const left_subtree = node.left ? inorder(node.left) : [];
    const right_subtree = node.right ? inorder(node.right) : [];

    return [...left_subtree, node.val, ...right_subtree];

    // more effective but more verbose
    // const res: number[] = [];
    // if (node.left) {
    //   res.push(...inorder(node.left));
    // }
    // res.push(node.val);
    // if (node.right) {
    //   res.push(...inorder(node.right));
    // }

    // return res;
  }

  if (root) return inorder(root);

  return [];
}

function inorderTraversal(root: TreeNode | null): number[] {
  const res: number[] = [];

  if (!root) {
    return res;
  }

  const stack: TreeNode[] = [root];
  let current: TreeNode | null = root.left;
  while (current != null || stack.length > 0) {
    if (current != null) {
      stack.push(current);
      current = current.left;
    } else {
      const prev = stack.pop() as TreeNode; // can't really have empty stack here.
      res.push(prev.val);
      current = prev.right;
    }
  }

  return res;
}

function test() {
  const root = new TreeNode(
    0,
    new TreeNode(1, new TreeNode(2), new TreeNode(3)),
    new TreeNode(
      4,
      new TreeNode(5, new TreeNode(6)),
      new TreeNode(7, null, new TreeNode(8))
    )
  );

  const traversal = inorderTraversal(root);
  const AU = [2, 1, 3, 0, 6, 5, 4, 7, 8];

  console.log(`AU=${str(AU)} GOT=${str(traversal)}`);
}

const str = (s: any) => JSON.stringify(s);

test();
