import functools


list_name = [2,3,4,6,34]

def add_names(first_name: str, last_name: str) -> str:
    return first_name + last_name

res = functools.reduce(lambda a, b: a+b, list_name)
print("Res: ", res)