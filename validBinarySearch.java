// Interesting 

public class ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) {
        if(root == null) {
            return true;
        }
        
        return validBSTRecursive(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    public boolean validBSTRecursive(TreeNode root, long minValue, long maxValue) {
        if(root == null) {
            return true;
        } else if(root.val >= maxValue || root.val <= minValue) {
            return false;
        } else {
            return validBSTRecursive(root.left, minValue, root.val) && validBSTRecursive(root.right, root.val, maxValue);
        }
    }
}