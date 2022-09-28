from collections import Counter

# initializing list
test_list = [2, 5, 2, 8, 5, 6, 8, 8, 8, 5, 2, 6, 1]

# printing original list
print("The original list : " + str(test_list))

# using Counter.most_common() + list comprehension
# sorting and removal of duplicates
res = [key for key, value in Counter(test_list).most_common()]

# print result
print("The list after sorting and removal : " + str(res))