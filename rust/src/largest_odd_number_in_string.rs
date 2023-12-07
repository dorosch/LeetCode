struct Solution;

impl Solution {
    pub fn largest_odd_number(num: String) -> String {
        num.chars()
            .rev()
            .skip_while(|&c| ['0', '2', '4', '6', '8'].contains(&c))
            .collect::<Vec<char>>()
            .iter()
            .rev()
            .collect()
    }
}


#[cfg(test)]
mod tests {
    use crate::largest_odd_number_in_string::Solution;

    #[test]
    fn largest_odd_number_test() {
        assert_eq!(Solution::largest_odd_number(String::from("52")), "5");
        assert_eq!(Solution::largest_odd_number(String::from("4206")), "");
        assert_eq!(Solution::largest_odd_number(String::from("35427")), "35427");
    }
}
