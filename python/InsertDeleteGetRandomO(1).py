import random

class RandomizedSet:
    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        result = val not in self.numMap
        if result:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return result
    
    def remove(self, val: int) -> bool:
        result = val in self.numMap
        if result:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return result

    def getRandom(self) -> int:
        return random.choice(self.numList)
    
RandomizedSet = RandomizedSet()
# Test inserting elements
print("Insert 1:", RandomizedSet.insert(1))  # Expected True
print("Insert 2:", RandomizedSet.insert(2))  # Expected True
print("Insert 2:", RandomizedSet.insert(3))  # Expected True
print("Insert 2:", RandomizedSet.insert(4))  # Expected True
print("Insert 2:", RandomizedSet.insert(5))  # Expected True
print("Insert 1 again:", RandomizedSet.insert(1))  # Expected False (1 already exists)

# Check the internal state after insertions
print("Current list:", RandomizedSet.numList)
print("Current map:", RandomizedSet.numMap)

# Test removing an element
print("Remove 1:", RandomizedSet.remove(1))  # Expected True (1 exists and will be removed)
print("Remove 3 (non-existent):", RandomizedSet.remove(3))  # Expected False (3 does not exist)

# Check the internal state after removal
print("Current list after removal:", RandomizedSet.numList)
print("Current map after removal:", RandomizedSet.numMap)

# Test getRandom - run this a few times to see the randomness
print("Random element:", RandomizedSet.getRandom()) # print random element from the current list

# time complexity O(1) because the insert method checks if val is in numMap which is O(1) due to the hash map.
# space complexity O(n) because each unique val takes up space in both numList and numMap