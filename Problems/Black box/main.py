# use the function blackbox(lst) that is already defined
my_list1 = [1, 2, 3]
my_list2 = blackbox(my_list1)
if id(my_list1) == id(my_list2):
    print('modifies')
else:
    print('new')
