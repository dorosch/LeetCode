use std::cmp;

struct Solution;

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut biggest = 0;
        let mut second_biggest = 0;

        for number in nums {
            if number > biggest {
                second_biggest = biggest;
                biggest = number;
            } else {
                second_biggest = cmp::max(second_biggest, number);
            }
        }

        (biggest - 1) * (second_biggest - 1)
    }
}


#[cfg(test)]
mod tests {
    use crate::maximum_product_of_two_elements_in_an_array::Solution;

    #[test]
    fn max_product_test() {
        assert_eq!(Solution::max_product(Vec::from([3, 7])), 12);
        assert_eq!(Solution::max_product(Vec::from([3, 4, 5, 2])), 12);
        assert_eq!(Solution::max_product(Vec::from([1, 5, 4, 5])), 16);
    }
}
