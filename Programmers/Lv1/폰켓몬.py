def solution(nums):
    answer = 0
    len_all = len(nums)
    nums = set(nums)
    if len(nums) < len_all/2:
        answer = len(nums)
    else:
        answer = len_all/2
    return answer