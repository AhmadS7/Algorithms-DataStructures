// O(n^2) time | O(1) space
function twoNumberSum(array, targetSum) {
  for (let i = 0; i < array.length - 1; i++) {
    let firstNum = array[i];
    for (let j = 0; j < array.length; j++) {
      let secondNum = array[j];
      if (firstNum + secondNum === targetSum) {
        return [firstNum, secondNum];
      }
    }
  }
  return [];
}

// O(n) time | O(n) space
function twoNumberSum2(array, targetSum) {
  const nums = {};

  for (const num of array) {
    const potentialSum = targetSum - num;
    if (potentialSum in nums) {
      return [potentialSum, num];
    } else {
      nums[num] = true;
    }
  }

  return [];
}

function twoNumberSum3(array, targetSum) {
  array.sort((a, b) => a - b);

  let left = 0;
  let right = array.length - 1;

  while (left < right) {
    const currentSum = array[left] + array[right];

    if (currentSum === targetSum) {
      return [array[left], array[right]];
    } else if (currentSum < targetSum) {
      left++;
    } else if (currentSum > targetSum) {
      right--;
    }
  }

  return [];
}

console.log(twoNumberSum3([0, 7, 5, 3, 2, 10, -1], 9));
