from collections import deque


def list_manipulator(list_of_nums, add_rem, begg_end, *nums):
    list_of_nums = deque(list_of_nums)
    nums = list(nums)
    if add_rem == "add" and begg_end == "beginning":
        list_of_nums.extendleft(nums[::-1])
    elif add_rem == "add" and begg_end == "end":
        list_of_nums.extend(nums)
    elif add_rem == "remove" and begg_end == "beginning":
        if nums:
            for i in range(nums[0]):
                list_of_nums.popleft()
        else:
            list_of_nums.popleft()
    elif add_rem == "remove" and begg_end == "end":
        if nums:
            for i in range(nums[0]):
                list_of_nums.pop()
        else:
            list_of_nums.pop()

    return list(list_of_nums)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
