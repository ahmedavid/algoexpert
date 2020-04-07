def twoNumberSumNaive(array,targetSum):
### O(n^2) Naive solution 
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum,secondNum]
    return []


def twoNumberSum(array, targetSum):
### O(n) Time, O(n) Space Solution
    nums = {}
    for num in array:
        complement = targetSum - num
        if complement in nums:
            return [complement,num]
        else:
            nums[num] = True
    return []

def twoNumberSumSort(array, targetSum):
    ### O(nlogn) solution because of sorting, O(1) Space complexity
    array.sort()
    left = 0;
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left],array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    
    return []
            