struct Solution;

impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let mut result = 0;

        let mut row_sums = vec![0; mat.len()];
        let mut col_sums = vec![0; mat[0].len()];

        for i in 0..mat.len() {
            for j in 0..mat[i].len() {
                row_sums[i] += mat[i][j];
                col_sums[j] += mat[i][j];
            }
        }

        for i in 0..mat.len() {
            for j in 0..mat[i].len() {
                if mat[i][j] == 1 && row_sums[i] == 1 && col_sums[j] == 1 {
                    result += 1;
                }
            }
        }

        result
    }
}


#[cfg(test)]
mod tests {
    use crate::special_positions_in_a_binary_matrix::Solution;

    #[test]
    fn num_special_test() {
        assert_eq!(Solution::num_special(
            Vec::from([Vec::from([1, 0, 0]), Vec::from([0, 0, 1]), Vec::from([1, 0, 0])])
        ), 1);
        assert_eq!(Solution::num_special(
            Vec::from([Vec::from([1, 0, 0]), Vec::from([0, 1, 0]), Vec::from([0, 0, 1])])
        ), 3);
    }
}
