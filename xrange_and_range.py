# list_nums = []
# for i in xrange(5):
#     list_nums.append(i)
#
# print(list_nums)


# # Iterator
#
# items = [2, 3, 4, "$5", 56]
#
# my_iterator = iter(items)
# while True:
#     try:
#         print(next(my_iterator))
#     except StopIteration:
#         break

# # Generator
#
# def count_down(n):
#     while True:
#         if n > 0:
#             yield n
#             n -= 1
# print(type(count_down(5)))
# for i in count_down(5):
#     print(i)


