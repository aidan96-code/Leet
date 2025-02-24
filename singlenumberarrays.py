#Find the unique number in an array

def SingleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
        return result
    
nums = [4,1,2,6,7,8,4,9]


print(f"The number that is unique in the array is {SingleNumber(nums)}")