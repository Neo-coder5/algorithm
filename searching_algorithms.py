class LinearSearch:
    def find_number(self, n):
        for i in range(1, n+1):
            print(i)
            ans = str(input(f"thinking number y/n: "))
            if ans == 'y':
                print("Win!")
                return i
            elif ans == 'n':
                print("Not found")
sol = LinearSearch()
print(sol.find_number(10))




myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
class LinearSearch2:
    def find_number(self, list1, target):
        for i in range(len(list1)):
            ans = input(f"thinkung number: {i}? (y/n) ")

            if list1[i] == target:
                return list1[i]


        return None

sol = LinearSearch2()
print(sol.find_number(myList, 7))

class BinarySearch:
    def binary_search_f(self, lists, item):
        low = 0
        high = len(lists) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = lists[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None
list1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
sol = BinarySearch()
print(sol.binary_search_f(list1, 7))


class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:
                return mid

            if guess > target:
                high = mid - 1

            else:
                low = mid + 1

        return low





