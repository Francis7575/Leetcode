const canConstruct = (ransomNote, magazine) => {
  const maganizeArr = magazine.split("");
  const ransomNoteArr = ransomNote.split("");

  let hashTable = {};

  for (let i = 0; i < maganizeArr.length; i++) {
    // If the character already exists in the hashTable, its count is incremented.
    if (hashTable[maganizeArr[i]]) {
      hashTable[maganizeArr[i]]++;
      //   Otherwise, the character is added to the hashTable with a count of 1.
    } else {
      hashTable[maganizeArr[i]] = 1;
    }
  }
  console.log(hashTable);

  //   checks if the character exists in hashTable
  for (let i = 0; i < ransomNoteArr.length; i++) {
    if (hashTable[ransomNoteArr[i]]) {
      // ensures the function tracks how many characters are remaining after each use
      hashTable[ransomNoteArr[i]]--;
    } else {
      return false;
    }
  }
  return true;
};

console.log(canConstruct("aaa", "aa"));
console.log(canConstruct("aaa", "aaa"));
console.log(canConstruct("bb", "bbbb"));
