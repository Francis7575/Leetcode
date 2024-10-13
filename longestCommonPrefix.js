// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

const longestCommonPrefix = function (strs) {
  if (strs.length === 0) return "";
  let prefix = strs[0];
  for (let i = 1; i < strs.length; i++) {
    // checks if the current prefix is not at the beginning of the string 
    while (strs[i].indexOf(prefix) !== 0) {
      // Shorten the prefix by removing the last character from the string until it matches 
      prefix = prefix.slice(0, -1);
      // If prefix becomes empty, return an empty string
      if (prefix === "") return "";
    }
  }
  return prefix;
};

// Time Complexity: 𝑂(𝑛⋅𝑚)
// Combining both loops, the time complexity can be expressed as: 𝑂(𝑛⋅𝑚) Where:
// n = number of strings in the input array
// m = length of the longest common prefix
// Space Complexity: 𝑂(1)
// Space for Variables: The function uses a constant amount of space for variables (like prefix, i),
// which does not scale with input size.
console.log(longestCommonPrefix(["flower", "flow", "flight"]));
