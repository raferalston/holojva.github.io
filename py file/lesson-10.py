nums = [123, 654, -1, 23, -16]

def apply_to_each(nums) :
    return -nums
def apply_to_read(L, f) :
    for i in range(len(L)) :
        L[i] = f(L[i])

apply_to_read(nums, apply_to_each)

print(nums)