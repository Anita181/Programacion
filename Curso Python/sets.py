# SETS

my_set = {}
print(type(my_set))

my_set = {"Python", "JavaScript", "C++"}
print(type(my_set))

# print(my_set[0]) Es un error porque en los set no hay un orden

my_set.add("C++")
print(my_set)

my_set_0 = {"Python", "JavaScript", "C++"}
my_set.difference_update(my_set_0)
print(my_set)

