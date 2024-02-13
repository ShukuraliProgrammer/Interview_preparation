# # simple way
# items = [2, 3, 4, 5, 6]
#
#
# def add_by_one(m):
#     return [i*2 for i in m]
#
# print(add_by_one(items))

# # map way
# # 1 - way
# items = [3,34,5,6,6]
# print(list(map(lambda x: x*2, items)))
#

# # 2-way
# def multiply(x):
#     return (x * x)
#
#
# def add(x):
#     return (x + x)
#
#
# func_list = [multiply, add]
#
# for i in range(5):
#     res = list(map(lambda x: x(i), func_list))
#     print("Res: ", res)

#
# number_list = range(-5, 5)
# print("Fil: ", filter(lambda x: x < 0, number_list))
# less_than_zero = list(filter(lambda x: x < 0, number_list))
# print(less_than_zero)
#


# Reduce: List -> [1,2,3,5,6]
#
# from functools import reduce
# items = [1,2,3,5,6]
# # res = 1
# # for i in items:
# #     res *= i
# # print("Natija: ", res)
#
# print(f"Natija: {reduce(lambda x, y: x * y, items)}")
#
# items = list(map(int, input().split(" ")))
#
# print("Items: ", items)

# # Decorator
#
# def dec_j(func):
#     def wrap_f(items, *args, **kwargs):
#         items_j = [i for i in items if i % 2 == 0]
#         res = func(items_j)
#         return res
#     return wrap_f
# @dec_j
# def cal_items(items):
#     return sum(items)
#
# print(cal_items([1,2,3,4,5]))