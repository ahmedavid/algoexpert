def productSum(nums, m = 1):
    sum = 0
    for num in nums:
        if type(num) is list:
            sum += productSum(num, m + 1)
        else:
            sum += num
    
    return sum * m

nums = [5,2,[7,-1],3,[6,[-13,8],4]]
productSum(nums)
