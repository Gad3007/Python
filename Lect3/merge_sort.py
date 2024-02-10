def merge_sort (nums):
    if len(nums) > 1:
        mid = len(nums) // 2 
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1 
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1 
            k += 1

        while j < len(left):
            nums[k] = right[j]
            j += 1 
            k += 1   

list1 = [1,4,6,5,8,7,2,3,43]
merge_sort(list1)
print(list1)