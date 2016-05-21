 
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    var res = [];
    function recursive(root){
        if(root != null){
            res.push(root.val); 
            recursive(root.left);  
            recursive(root.right); 
        }else{
            res.push('#');
        }
    }
    recursive(root)
    return res.join(' ');
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    data = data.split(' ');
    var i = 0;
    function recursive(){
        if(data.length == 0 || i >= data.length) return null;
        if(data[i] != '#'){
            var node = new TreeNode(parseInt(data[i++]));  
            node.left = recursive();
            node.right = recursive(); 
            return node;
        }else{
            i++;
            return null;
        }
    }
    return recursive();
};



/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */