# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/2/17 6:46 下午
'''


class Solution:
    def searchRange(self, nums, target: int) :

        n = len(nums)

        if n == 0: return [-1, -1]
        if n == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        left = left1 = 0
        right = right1 = n


        result = []

        # 左侧边界
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1

        print(f"left: {left}")



        # 右侧边界
        while left1 < right1:
            mid = int((left1 + right1) / 2)
            if nums[mid] == target:
                left1 = mid + 1
            elif nums[mid] > target:
                right1 = mid
            elif nums[mid] < target:
                left1 = mid + 1

        print(f"left1 -1 : {left1 -1}")


        if right1 == 0 or left == n :
            result = [-1, -1]
        else:
            result = [left, left1 -1]

        return result


s = Solution()
# s.searchRange([1,2,4,4,8,9], 4)
# print(s.searchRange([5,7,7,8,8,10], 6))

print(10 //2 )




