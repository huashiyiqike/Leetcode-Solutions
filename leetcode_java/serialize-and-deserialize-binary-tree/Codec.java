import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */

class Codec {
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder res = new StringBuilder();
        if (root == null) return res.toString();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        res.append(String.valueOf(root.val)).append(",");
        while (!queue.isEmpty()) {
            Queue<TreeNode> next = new LinkedList<>();
            while (!queue.isEmpty()) {
                TreeNode cur = queue.poll();
                if (cur.left != null) {
                    res.append(String.valueOf(cur.left.val)).append(",");
                    next.offer(cur.left);
                } else {
                    res.append("#,");
                }
                if (cur.right != null) {
                    res.append(String.valueOf(cur.right.val)).append(",");
                    next.offer(cur.right);
                } else {
                    res.append("#,");
                }
            }
            queue = next;
        }
        return res.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.isEmpty()) return null;
        // data = String.join("",(data.split(",")));
        String[] datas = data.split(",");

        Queue<TreeNode> queue = new LinkedList<>();
        int i = 0;
        TreeNode root = new TreeNode(Integer.parseInt(datas[i]));
        queue.offer(root);
        while (i < datas.length - 1) {
            Queue<TreeNode> next = new LinkedList<>();
            while (!queue.isEmpty()) {
                TreeNode cur = queue.poll();
                i++;
                if (!datas[i].equals("#")) {
                    cur.left = new TreeNode(Integer.parseInt(datas[i]));
                    next.offer(cur.left);
                }
                i++;
                if (!datas[i].equals("#")) {
                    cur.right = new TreeNode(Integer.parseInt(datas[i]));
                    next.offer(cur.right);
                }
            }
            queue = next;
        }
        return root;
    }
}

// Encodes a tree to a single string.
//    public String serialize(TreeNode root) {
//        String res = "";
//        Stack<TreeNode> stack = new LinkedList<>();
//        stack.push(root);
//        while(!stack.isEmpty()){
//            TreeNode cur = stack.pop();
//            while(cur != null) {
//                res += String.valueOf(cur.val);
//                if(cur.left == null && cur.right == null){
//                    res += "##";
//                    break;
//                }
//                if (cur.right != null){
//                    stack.push(cur.right);
//                }else res += "#";
//                if (cur.left != null){
//                    cur = cur.left;
//                }else res += "#";
//            }
//        }
//        return res;
//    }

// Decodes your encoded data to tree.
//    public TreeNode deserialize(String data) {
//        TreeNode root = null;
//        if(data == null) return root;
//       // else root = TreeNode(Integer.parseInt(data.charAt(0)));
//        TreeNode cur = root;
//        int idx = 0;
//        while(idx < data.length()){
//            if(data.charAt(i) == "#")
//        }
//    }

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));

public class Codec {
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        helperS(root, sb);
        return sb.toString();
    }

    private void helperS(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("null").append(",");
            return;
        }

        sb.append(node.val).append(",");

        helperS(node.left, sb);
        helperS(node.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] vals = data.split("[,]");
        int[] index = new int[]{0};
        return helperD(vals, index);
    }

    private TreeNode helperD(String[] vals, int[] index) {
        if (index[0] == vals.length) {
            return null;
        }

        String visiting = vals[index[0]++];
        if (visiting.equals("null")) {
            return null;
        }

        TreeNode node = new TreeNode(Integer.valueOf(visiting));
        node.left = helperD(vals, index);
        node.right = helperD(vals, index);

        return node;
    }
}