use std::cmp::Ordering;
use std::collections::HashSet;


struct Solution;

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: HashSet<Vec<i32>> = HashSet::new();

        nums.sort();

        for i in 0..nums.len() {
            let mut j = i + 1;
            let mut k = nums.len() - 1;

            while j < k {
                match (nums[i] + nums[j] + nums[k]).cmp(&0) {
                    Ordering::Equal => {
                        result.insert(vec![nums[i], nums[j], nums[k]]);
                        j += 1;
                        k -= 1;
                    },
                    Ordering::Less => j += 1,
                    Ordering::Greater => k -= 1
                }
            }
        }

        result.into_iter().collect()
    }
}


#[cfg(test)]
mod tests {
    use crate::sum3::Solution;

    #[test]
    fn three_sum() {
        assert!(Solution::three_sum(Vec::from([0, 1, 1])).is_empty());
        assert_eq!(Solution::three_sum(Vec::from([0, 0, 0])), Vec::from([[0, 0, 0]]));
        assert_eq!(Solution::three_sum(Vec::from([-1, 0, 1, 2, -1, -4])), Vec::from([[-1, -1, 2], [-1, 0, 1]]));
    }
}
