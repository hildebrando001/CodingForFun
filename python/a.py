######################
my_list = [1,2,3,4,5,6,7,8,9,10]

squares = [num*num for num in my_list]
print(squares)
#####################################################
print([num*num for num in my_list]) # python é imoral 
#####################################################
print([num*num for num in [1,2,3,4,5,6,7,8,9,10]])