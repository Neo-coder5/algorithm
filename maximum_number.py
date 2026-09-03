# def maximum_number(a,b,c):
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     else:
#         if b>c:
#             return b
#         else:
#             return c
# print(maximum_number(3,7,11))

list1 = [4, 12, 5, 22, 8, 15, 3]
class Solution:
    def max(self, list1):
        if not list1:
            return None
        max_num = list1[0]

        i = 1
        while i < len(list1):
            if list1[i] > max_num:
                max_num = list1[i]
            i += 1
        return max_num
sol = Solution()
print(sol.max(list1))