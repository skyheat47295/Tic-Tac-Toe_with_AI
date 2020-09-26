my_string = input().lower().split()
my_string_dict = {}
for item in my_string:
    my_string_dict[item] = my_string.count(item)
for item in my_string_dict:
    print(f'{item} {my_string_dict[item]}')
