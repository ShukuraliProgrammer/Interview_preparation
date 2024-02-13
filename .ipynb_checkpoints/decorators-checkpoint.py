# def add_first_value(value):
#     return value + 10
#
#
# def add_second_value(value2):
#     return value2 + 20


# def two_value_sum_dec(func1):
#     def square_2(a,b):
#         x = func1(a,b)
#         return x ** 2
#     return square_2
#     # def kub_3(value2):
#     #     y = func2(value2)
#     #     return y ** 3
#
#
# @two_value_sum_dec
# def add_two_elements(a, b):
#     return a+b
#
# res=add_two_elements(10,9)
# print(res)



# def num_times(num_times):
#
#     def dec_func(func):
#
#         def wrapper(*args, **kwargs):
#
#             for i in range(num_times):
#                 result = func(*args, **kwargs)
#
#             return result
#
#         return wrapper
#     return dec_func
#
#
# @num_times(num_times=8)
# def add3(a,b):
#     print(a+b)
#     return a+b
#
# add3(23,34)


class LastName:
    def __init__(self, func):
        self.func = func
        self.last_name = "Rezamonov"

    def __call__(self, *args, **kwargs):
        print("This class called")
        return f"{self.last_name} {self.func(*args, **kwargs)}"


@LastName
def first_name_print(name):
    return name.upper()

res = first_name_print("Alibek")
print(res)