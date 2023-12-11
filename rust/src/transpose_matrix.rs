struct Solution;

impl Solution {
    pub fn transpose(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut transposed_matrix: Vec<Vec<i32>> = Vec::new();

        for col in 0..matrix[0].len() {
            let mut row: Vec<i32> = Vec::new();
            for row_index in 0..matrix.len() {
                row.push(matrix[row_index][col]);
            }

            transposed_matrix.push(row);
        }

        transposed_matrix
    }
}


#[cfg(test)]
mod tests {
    use crate::transpose_matrix::Solution;

    #[test]
    fn find_special_integer_test() {
        assert_eq!(Solution::transpose(
            Vec::from([Vec::from([1, 2, 3]), Vec::from([4, 5, 6]), Vec::from([7, 8, 9])])),
            Vec::from([Vec::from([1, 4, 7]), Vec::from([2, 5, 8]), Vec::from([3, 6, 9])])
        );
        assert_eq!(Solution::transpose(
            Vec::from([Vec::from([1, 2, 3]), Vec::from([4, 5, 6])])),
            Vec::from([Vec::from([1, 4]), Vec::from([2, 5]), Vec::from([3, 6])])
        );
    }
}
