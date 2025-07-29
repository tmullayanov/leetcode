macro_rules! test {
    ($name:ident: $input:expr => $expected:expr) => {
        {
            let actual = $input;
            let expected = $expected;
            if actual == expected {
                println!("✅ {}: OK", stringify!($name));
            } else {
                println!("❌ {}: FAILED", stringify!($name));
                println!("   Expected: {:?}", expected);
                println!("   Got:      {:?}", actual);
            }
        }
    };
}
struct Solution;

impl Solution {

    pub fn my_atoi(s: String) -> i32 {
        let mut result: i32 = 0;
        let mut started = false;
        let mut sign = 1;

        for c in s.chars() {
            match c {
                ' ' if !started => continue,
                '-' if !started => {
                    started = true;
                    sign = -1;
                },
                '+' if !started => {
                    started = true
                },
                '0'..='9' => {
                    started = true;

                    let digit = (c as u8 - b'0') as i32;

                    // check overflow
                    if result > (i32::MAX - digit) / 10 {
                        if sign == 1 {
                            return i32::MAX;
                        } else {
                            return i32::MIN;
                        }
                    }

                    result = result * 10 + digit;  
                },
                _ => break,
            }
        }

        result * sign
    }
}

pub fn main() {
    test!(test_42: Solution::my_atoi("42".to_string()) => 42);
    test!(test_leading_zeroes: Solution::my_atoi("0042".to_string()) => 42);
    test!(stop_when_non_digit: Solution::my_atoi("4193 with words".to_string()) => 4193);
    test!(zero_in_weird_string: Solution::my_atoi("0-1".to_string()) => 0);
    test!(l33t_before_nondigits: Solution::my_atoi("1337c334".to_string()) => 1337);
    test!(zero_when_no_digits: Solution::my_atoi("hello".to_string()) => 0);
    test!(negative: Solution::my_atoi("-5".to_string()) => -5);
    test!(zero_when_leading_nondigit: Solution::my_atoi("hello42".to_string()) => 0);

    test!(positive_overflow: Solution::my_atoi("2147483648".to_string()) => 2147483647);
    test!(negative_multidigit: Solution::my_atoi("-15".to_string()) => -15);
    test!(negative_overflow: Solution::my_atoi("-2147483649".to_string()) => -2147483648);
    test!(i32_min: Solution::my_atoi("-2147483648".to_string()) => -2147483648);
    test!(i32_max: Solution::my_atoi("2147483647".to_string()) => 2147483647);

    test!(negative_with_leading_zeroes: Solution::my_atoi("-042".to_string()) => -42);
    test!(leading_plus_recognized: Solution::my_atoi("+12".to_string()) => 12);
    test!(non_leading_plus_breaks: Solution::my_atoi("12+21hello".to_string()) => 12);
    test!(empty: Solution::my_atoi("".to_string()) => 0);
    test!(only_spaces: Solution::my_atoi("   ".to_string()) => 0);
    test!(plus_minus: Solution::my_atoi("+-12".to_string()) => 0);
    test!(minus_plus: Solution::my_atoi("-+12".to_string()) => 0);
}
