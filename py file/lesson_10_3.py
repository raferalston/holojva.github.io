def apply_to_read(L, f) :
    for i in range(len(i)) :
        L[i] = f(L[i])
nums = [1, 0, 3.14, -2]
apply_to_read(nums, abs)
print(nums, abs) 