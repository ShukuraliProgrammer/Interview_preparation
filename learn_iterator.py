

class Increment:

    def __iter__(self):
        self.a = 1

        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
my_list = ["salom", "alik", "qale"] # iterable

my_inc = my_list # iterator

my_iterater = iter(my_inc)

print(next(my_iterater))
print(next(my_iterater))
print(next(my_iterater))



my_for_iterator = iter([1,2,3,4,5,6])

while True:
    try:
        print(next(my_for_iterator))
    except StopIteration:
        break


for i in [1,2,3,4,5,6]:
    print(i)



#generator
def generator_count_func(number):
    while number > 0:
        yield number
        number -= 1

for i in generator_count_func(10):
    print(i)

