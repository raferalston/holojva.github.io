nums = [135,364,	290,	905,	319,	112,	500,	340,	921,	159,	103,	805,	97, 114,	551,	576,	996,	487,	128,	121]
min = nums[0]
max = 0

for i in range(len(nums)) :
    if nums[i] > max  :
        max = nums[i]
    if nums[i] < min :
        min = nums[i]    
print(f"Самое маленькое: {min}, самое большое {max}.")