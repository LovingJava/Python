nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n)
# print (my_list)

# my_list = [n for n in nums]
# print (my_list)

# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print (my_list)

# my_list = [n*n for n in nums]
# print (my_list)

# Using a map + lambda
# my_list = map(lambda n: n*n, nums)
# print (my_list)

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print (my_list)        

# my_list = [n for n in nums if n%2 == 0]
# print (my_list) 

# my_list = filter(lambda n: n%2 == 0, nums)
# print (my_list) 

names = ['', '', '', '', '']
