candies = [2,3,5,1,3]

extraCandies = 3





def kidsWithCandies(candies, extraCandies):
    maxCandies = max(candies)
    result = []
    for i in range(len(candies)):
        result.append(candies[i] + extraCandies >= maxCandies)
    return result

print(kidsWithCandies(candies, extraCandies))