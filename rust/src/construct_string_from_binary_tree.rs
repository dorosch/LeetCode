use std::rc::Rc;
use std::cell::RefCell;


#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

struct Solution;

impl Solution {
    pub fn tree2str(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        if let Some(root) = root {
            let mut node = root.borrow_mut();

            return node.val.to_string() + &match (node.left.take(), node.right.take()) {
                (None, None) => {
                    String::new()
                },
                (left, None) => {
                    format!("({})", Self::tree2str(left))
                },
                (None, right) => {
                    format!("()({})", Self::tree2str(right))
                },
                (left, right) => {
                    format!("({})({})", Self::tree2str(left), Self::tree2str(right))
                }
            }
        } else {
            String::new()
        }
    }
}


#[cfg(test)]
mod tests {
    use std::cell::RefCell;
    use std::rc::Rc;
    use crate::construct_string_from_binary_tree::{Solution, TreeNode};

    #[test]
    fn tree2str_test() {
        let root = Some(Rc::new(RefCell::new(TreeNode {
            val: 1,
            left: Some(Rc::new(RefCell::new(TreeNode {
                val: 2,
                left: Some(Rc::new(RefCell::new(TreeNode {
                    val: 4,
                    left: None,
                    right: None
                }))),
                right: None
            }))),
            right: Some(Rc::new(RefCell::new(TreeNode::new(3))))
        })));
        assert_eq!(Solution::tree2str(root), "1(2(4))(3)");

        let root = Some(Rc::new(RefCell::new(TreeNode {
            val: 1,
            left: Some(Rc::new(RefCell::new(TreeNode {
                val: 2,
                left: None,
                right: Some(Rc::new(RefCell::new(TreeNode {
                    val: 4,
                    left: None,
                    right: None
                })))
            }))),
            right: Some(Rc::new(RefCell::new(TreeNode::new(3))))
        })));
        assert_eq!(Solution::tree2str(root), "1(2()(4))(3)");
    }
}
