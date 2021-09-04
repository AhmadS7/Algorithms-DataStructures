currentSum = [12,3,1,2,-6,5,-8,6]

# O(n^2) Time / O(n) Space  
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1                 
    return triplets
    

 
 
print(threeNumberSum(currentSum, 0))
    