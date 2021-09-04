const num = [12, 3, 1, 2, -6, 5, -8, 6];

// O(n^2) Time / O(n) Space
function threeNumberSum(array, targetSum) {
  array.sort((a, b) => a - b);
  let triplets = [];

  for (let i = 0; i < array.length - 2; i++) {
    let left = i + 1;
    let right = array.length - 1;
    while (left < right) {
      let currentSum = array[i] + array[left] + array[right];
      if (currentSum == targetSum) {
        triplets.push([array[i], array[left], array[right]]);
        left += 1;
        right -= 1;
      } else if (currentSum < targetSum) {
        left += 1;
      } else if (currentSum > targetSum) {
        right -= 1;
      }
    }
  }
  return triplets;
}




console.log(threeNumberSum(num,0))