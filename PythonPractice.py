l1 = [i for i in range(10)]
l2 = l1[-4:]  # Slicing with create new list with Shallow copy of items
print(l2)

# id of elements 6,7,8,9 will be same
print("l1: ", id(l1), " l2: ", id(l2), " l1[7] :", id(l1[7]), " l2[1] :", id(l2[1]))

# next id of l2[1] will be updated as it points to new value
l2[1] = 100
print("l1: ", l1, " l2: ", l2)
print("l1: ", id(l1), " l2: ", id(l2), " l1[1] :", id(l1[7]), " l2[1] :", id(l2[1]))

# interesting ways to print list in reverse (usual way l1.reverse() )
print("Reverse:", l1[-1::-1])
print("Reverse:", l1[::-1])


for _ in range(90):
    print("*", end="")
print("\nList Comprehensions\n")

lc1 = [x * 2 for x in range(10)]
lc2 = [x * x for x in lc1 if not x % 2]
lc3 = [(x, x + y, y) for x in lc1 for y in lc2 if x != y]
print("lc1:", lc1, "\nlc2:", lc2, "\nlc3:", lc3)

# Nesting of list comprehension
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
lc4 = [[row[i] for row in matrix] for i in range(4)]
print("\nlc4:", lc4)
lc4 = list(zip(*matrix))
print("lc4 using zip:", lc4)

for _ in range(90):
    print("*", end="")
print("\nMap\n")


# Courtesy for map, reduce, zip, filter : \
# https://medium.com/@lokeshsharma596/python-lambda-map-filter-reduce-and-zip-function-c59d8946a3ce
# https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce

# MAP: Apply map function to all items of iterable and create new iterable with mapped data
# syntax: map(func, *iterables) (*iterables means multiple iterables are accepted)
people = ["hariom", "ami", "dhyansh", "developer"]
up = list(map(lambda x: x.upper(), people))
print("Names in Upper:", up)

names = [
    {"first": "hariom", "last": "pandya"},
    {"first": "ami", "last": "raval"},
    {"first": "dhyansh", "last": "bhatt"},
]
first_names = list(map(lambda x: x["first"], names))
print("First name:", first_names)

# If the map function requires multiple arguments, multiple iterator needs to be passed to it
# Ex. consider below list. we need to round values as per element position. i.e. 1.1, 2.22, 3.333 and so on
data = [1.111111, 2.222222, 3.333333, 4.444444, 5.555555, 6.666666]
new_list = list(map(round, data, range(len(data) + 1)))
# Here note that we are pssing function object and not calling it(i.e. round not round())
# map will call function object for each item of iterator(s)

print("Map with Multiple iterators:", new_list)

# We can also implement zip function with map
print("zip using map:", *map(lambda a, b: (a, b), range(1, 11), range(11, 21)))

for _ in range(90):
    print("*", end="")
print("\nFilter\n")

# FILTER: Apply filter function and create new iterable with items which satisfy the filter condition
# syntax: filter(func, iterable) (accept only one iterable)
# Function must take one argument and return true or false if not the filter returns same filter back

odd_numbers = [*filter(lambda x: x % 2, range(10))]
even_numbers = [*filter(lambda x: not x % 2, range(10))]
print("Odd: ", odd_numbers, " Even: ", even_numbers)


for _ in range(90):
    print("*", end="")
print("\nZIP\n")

# ZIP: aggregates elements of iterables passed, and returns an iterator of tuples
# Incase if multiple iterator passed, iterator stops when shortest iterable is exhaused.
name = ["Hariom", "Pooja", "Dhyansh"]
roll_no = [4, 1, 3]
marks = [40, 50, 60]
mapped = zip(name, roll_no, marks)
print(list(mapped))
mapped_key_value = zip(name, roll_no)
# dict can be created if zip contains tuple of 2 elements. 1st element will be the key and 2nd element will be the value
print(dict(mapped_key_value))


for _ in range(90):
    print("*", end="")
print("\nREDUCE from functools\n")

# reduce : reduce(func, iterable[, initial])
# reduce the given iterator to single value as follows:
# apply function(that must accept two arguments) on 1st and 2nd element generete result.
# apply function on result and 3rd and so on...
# if initial is supplied it would be : result =initial and 1st,result=result and 2nd, result=resule and 3rd...

from functools import reduce

l3 = list(range(10))
print("Reduce:", reduce(lambda x, y: x + y, l3))


for _ in range(90):
    print("*", end="")
print("\nInteresting Examples of map/filter/zip \n")

users = [
    {"username": "hariom", "tweets": ["i love programming", "i am good"]},
    {"username": "ami", "tweets": []},
    {"username": "pooja", "tweets": ["India", "Python"]},
    {"username": "dhyansh", "tweets": []},
    {"username": "user", "tweets": ["i am good"]},
]

# Filter out Users which dont have any tweets/Inactive Users
inactive = list(filter(lambda user: not user["tweets"], users))
print(inactive)

# Filter inactive users with just username in uppercase.
inactive_names = map(lambda user: user["username"].upper(), inactive)
print(*inactive_names)

# Return a new list with the string “your name is” + name ,but only if length of name is bigger than 4
print(
    *map(
        lambda data: "Your name is " + data["username"],
        list(filter(lambda name: len(name["username"]) > 4, users)),
    )
)

# Return a new list of inactive users with the string “Inactive User:” + name(in upper) ,but only if length of name is 3
print(
    *map(
        lambda data: "Inactive User:" + data["username"].upper(),
        list(filter(lambda name: len(name["username"]) == 3, inactive)),
    )
)
