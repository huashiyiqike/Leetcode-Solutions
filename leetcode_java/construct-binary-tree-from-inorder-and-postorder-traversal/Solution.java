/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    int[] in, post;

    public TreeNode helper(int startin, int endin, int startpost, int endpost) {
        if (startin > endin) return null;
        TreeNode root = new TreeNode(post[endpost]);
        int root_in = startin;
        while (in[root_in] != post[endpost]) root_in++;
        root.left = helper(startin, root_in - 1, startpost,
                startpost - 1 + root_in - startin);
        root.right = helper(root_in + 1, endin,
                endpost - 1 - endin + root_in + 1, endpost - 1);
        return root;
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        in = inorder;
        post = postorder;
        return helper(0, in.length - 1, 0, post.length - 1);
    }
}

/**
 * Definition for binary tree
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
public class Solution {

    int[] inorder;
    int[] postorder;
    int p;

    TreeNode buildTree(int st, int ed) {

        if (st >= ed) return null;

        TreeNode root = new TreeNode(postorder[p]);

        int i;
        for (i = st; i < ed && inorder[i] != postorder[p]; i++) ;

        p--;
        root.right = buildTree(i + 1, ed);
        root.left = buildTree(st, i);

        return root;
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {

        this.p = postorder.length - 1;
        this.inorder = inorder;
        this.postorder = postorder;

        return buildTree(0, inorder.length);
    }
}