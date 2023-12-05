use std::collections::HashMap;


pub struct Solution;

impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        let mut indices: HashMap<i32, i32> = HashMap::new();

        for num in nums {
            result += indices.get(&num).unwrap_or(&0);
            *indices.entry(num).or_insert(0) += 1;
        }

        result
    }
}


#[cfg(test)]
mod tests {
    use crate::number_of_good_pairs::Solution;

    #[test]
    fn num_identical_pairs_test() {
        assert_eq!(Solution::num_identical_pairs(Vec::from([1, 2, 3, 1, 1, 3])), 4);
        assert_eq!(Solution::num_identical_pairs(Vec::from([1, 1, 1, 1])), 6);
        assert_eq!(Solution::num_identical_pairs(Vec::from([1, 2, 3])), 0);
    }
}
