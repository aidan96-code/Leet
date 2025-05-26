def find_unique_numbers(nums):
    # Step 1: Create an empty dictionary to count occurrences
    freq = {}

    # Step 2: Count each number in the list
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 3: Return a list of numbers that appear exactly once
    unique_nums = [num for num, count in freq.items() if count == 1]
    return unique_nums

nums = [4, 1, 2, 1, 2, 4, 9, 8]
result = find_unique_numbers(nums)
print(f"Numbers that appear only once: {result}")