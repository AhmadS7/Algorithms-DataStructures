// O(n) time \ O(1) space
function isValidateSubsequence(array, sequence) {
  let arrIndex = 0;
  let sequenceIndex = 0;

  while (arrIndex < array.length && sequenceIndex < sequence.length) {
    if (array[arrIndex] === sequence[sequenceIndex]) sequenceIndex++;
    arrIndex++;
  }
  return sequenceIndex === sequence.length;
}

console.log(
  isValidateSubsequence([5, 1, 22, 25, 6, -1, 8, 10, 11, 17], [1, 6, -1, 10])
);
