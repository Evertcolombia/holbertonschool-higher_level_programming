#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [0]
idx = 0
new_element = 4
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
