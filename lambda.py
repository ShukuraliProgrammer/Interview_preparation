# list_multiple_items = lambda x, y: x*y
#
# res = list_multiple_items(2,3)
# print(res)
#
# list_multiple_values = [lambda arg=x: arg*10 for x in range(20)]
#
# for i in list_multiple_values:
#     print(i())

def my_wrapper(x: int) -> int:
    return lambda a, b: (x * b) + a

one_obj = my_wrapper(10)
print("res: ", one_obj(2,5))
