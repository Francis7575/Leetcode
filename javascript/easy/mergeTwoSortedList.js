// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
// Return the head of the merged linked list.
// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1,1,2,3,4,4]
// Example 2:

// Input: list1 = [], list2 = []
// Output: []
// Example 3:

// Input: list1 = [], list2 = [0]
// Output: [0]

// Definition for singly-linked list.
class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

function mergeTwoLists(list1, list2) {
  // Create a dummy node as the starting point of the merged list
  let dummy = new ListNode();
  let current = dummy;
  // Iterate through both lists
  while (list1 && list2) {
    if (list1.val <= list2.val) {
      current.next = list1; // adds the smaller node from list1 to the result list.
      list1 = list1.next;  // advance the pointer of list1 to the next node,
    } else {
      current.next = list2; // adds the smaller node from list2 to the result list.
      list2 = list2.next;  // advance the pointer of list2 to the next node,
    }
    current = current.next;
  }

  // append remaining nodes
  if (list1) {
    current.next = list1;
  }

  if (list2) {
    current.next = list2;
  }

  return dummy.next;
}

const list1 = new ListNode(1, new ListNode(3, new ListNode(5)));
const list2 = new ListNode(2, new ListNode(4, new ListNode(6)));
const result = mergeTwoLists(list1, list2);

function printList(list) {
  let array = [];
  while (list !== null) {
    array.push(list.val);
    list = list.next;
  }
  console.log(array);
}
printList(result);

// The time complexity is O(n + m), n is the number of nodes in list1 m, is the number of nodes in list2.
// The space complexity is O(1) since i'm not using any extra space for storing the nodes themselves