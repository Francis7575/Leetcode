// Given an integer x, return true if x is a palindrome, and false otherwise.
// Example 1:
// Input: x = 121
// Output: true
// Explanation: 121 reads as 121 from left to right and from right to left.

// Example 2:
// Input: x = -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

// Example 3:
// Input: x = 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

const isPalindrome = function(x) {
    if (x < 0) {
      return false;
    }
    let reversed = 0; // store the reversed version of the number x
    let current = x;
    while (current !== 0) {
      reversed = reversed*10 + current % 10;
      current = Math.floor(current/10)
    }
    return x  === reversed;
}

const result = isPalindrome(121)
console.log(result)

// Example (x = 121):

// First iteration:
// reversed = 0 * 10 + 121 % 10 = 1
// current = Math.floor(121 / 10) = 12
// Second iteration:
// reversed = 1 * 10 + 12 % 10 = 12
// current = Math.floor(12 / 10) = 1
// Third iteration:
// reversed = 12 * 10 + 1 % 10 = 121
// current = Math.floor(1 / 10) = 0 
