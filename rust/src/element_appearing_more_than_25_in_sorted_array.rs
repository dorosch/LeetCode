struct Solution;

impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let size =arr.len() / 4;

        for index in 0..arr.len() - size {
            if arr[index] == arr[index + size] {
                return arr[index];
            }
        }

        -1
    }
}


#[cfg(test)]
mod tests {
    use crate::element_appearing_more_than_25_in_sorted_array::Solution;

    #[test]
    fn find_special_integer_test() {
        assert_eq!(Solution::find_special_integer(Vec::from([1, 1])), 1);
        assert_eq!(Solution::find_special_integer(Vec::from([1, 2, 2, 6, 6, 6, 6, 7, 10])), 6);
    }
}
