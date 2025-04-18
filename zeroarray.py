nums = [0,1,0,3,12]

def movezeros(nums):
    n = len(nums)
    count = 0  # Count of non-zero elements

    # Traverse the array and move non-zero elements to the front
    for i in range(n):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1

    # Fill the remaining positions with zeros
    while count < n:
        nums[count] = 0
        count += 1
    return nums

print(movezeros(nums))