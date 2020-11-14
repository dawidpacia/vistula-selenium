# data types

a_int = 10
a_float = 10.0

a_string = "test"
b_string = 'test'
# a_char = "a" -> not exists
print(a_string[2])

a_list = [1, 2, 3, "test"]
a_list[1] = "x"
print(a_list[-1])
print(a_list)

a_tuple = (1, 2, 3, "test")
# a_tuple[1] = "x" -> exception

a_bool = True

a_dict = {
    "key": "value",
    "fruit": "apple",
    "drink": "coffee"
}

print(a_dict["fruit"])


a = 1
b = 10

while a < b:
    print(a)
    a += 1

if a > b:
    print("A is larger than B")
elif a < b:
    print("B is larger than A")
else:
    print("Number are equal")
