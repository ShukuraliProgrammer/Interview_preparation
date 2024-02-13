# def squares(length):
#     for n in range(length):
#         yield n ** 2
#


#
squares = (n**2 for n in range(10))


print(next(squares))
print(next(squares))
print(next(squares))



