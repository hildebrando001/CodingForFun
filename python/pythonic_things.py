######################
new_list = [x for x in range(50) if x % 2 == 0]
print(new_list) # print([x for x in range(50) if x % 2 == 0])
#####################################################
my_list = [1,2,3,4,5,6,7,8,9,10]
squares = [num*num for num in my_list]
print(squares) # print([num*num for num in my_list])
print([num*num for num in [1,2,3,4,5,6,7,8,9,10]])
#####################################################
valor = 5
print(valor in my_list) # returns True or False
#####################################################
list1 = [1,1,3,4,5,6,7,8,8,8,9,9]
print(set(list1))
#####################################################
print([x for x in [1, 2, 3, 4, 5] if x % 2 == 0])
