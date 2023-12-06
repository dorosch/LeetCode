struct Solution;

impl Solution {
    pub fn total_money(n: i32) -> i32 {
        let weeks = n / 7;
        let days = n % 7;

        ((weeks * (2 * 28 + (weeks - 1) * 7)) / 2) + (days * (2 * (weeks + 1) + (days - 1) * 1)) / 2
    }
}


#[cfg(test)]
mod tests {
    use crate::calculate_money_in_leetcode_bank::Solution;

    #[test]
    fn total_money_test() {
        assert_eq!(Solution::total_money(4), 10);
        assert_eq!(Solution::total_money(7), 28);
        assert_eq!(Solution::total_money(10), 37);
        assert_eq!(Solution::total_money(20), 96);
        assert_eq!(Solution::total_money(26), 135);
    }
}
