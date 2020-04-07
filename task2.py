list1 = [12, -7, 5, 64, -14]
print("Original numbers in the list: ",list1)
new_list1 = list(filter(lambda x: x >0, list1))
print("Positive numbers in the list: ",new_list1)

list2= [34, 1, 0, -23]
print("Original numbers in the list: ",list2)
new_list2 = list(filter(lambda x: x >0, list2))
print("Positive numbers in the list: ",new_list2)
