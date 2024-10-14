// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

// Example 1:
// Input: s = "()"
// Output: true

// Example 2:
// Input: s = "()[]{}"
// Output: true

// Example 3:
// Input: s = "(]"
// Output: false

// Example 4:
// Input: s = "([])"
// Output: true

const isValid = function (s) {
  const mappings = new Map();
  // key opening brackets & value close brackets
  mappings.set('(', ')');
  mappings.set('[', ']');
  mappings.set('{', '}');
  const stack = [];

  for (let i = 0; i < s.length; i += 1) {
    if (mappings.has(s[i])) { // if it has open bracket push value from the map into the stack
      stack.push(mappings.get(s[i]));
    } else if (stack.pop() !== s[i]) {
      return false;
    }
  }
  return stack.length === 0;
};

const result = isValid("()[]{}");
console.log(result);

// time complexity O(n) because of the for loop iteration
// space complexity O(n) because of the input size