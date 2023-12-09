use std::rc::Rc;
use std::cell::RefCell;


#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

struct Solution;

impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        if let Some(root) = root {
            let mut node = root.borrow_mut();

            [
                Self::inorder_traversal(node.left.take()),
                vec![node.val],
                Self::inorder_traversal(node.right.take()),
            ].concat()
        } else {
            Vec::new()
        }
    }
}


#[cfg(test)]
mod tests {
    use std::cell::RefCell;
    use std::rc::Rc;
    use crate::binary_tree_inorder_traversal::{Solution, TreeNode};

    #[test]
    fn inorder_traversal_test() {
        let root = Some(Rc::new(RefCell::new(TreeNode {
            val: 1,
            left: None,
            right: Some(Rc::new(RefCell::new(TreeNode {
                val: 2,
                left: Some(Rc::new(RefCell::new(TreeNode {
                    val: 3,
                    left: None,
                    right: None
                }))),
                right: None
            })))
        })));
        assert_eq!(Solution::inorder_traversal(root), Vec::from([1, 3, 2]));
    }
}
