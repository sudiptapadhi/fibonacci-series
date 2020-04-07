ASSIGNING ELEMENTS TO DIFFERENT LIST
list1 = [9, 3, 6, 5]
print("The original list : " + str(list1)) 
list1.extend(range(5)) 
print("The list after adding range elements : " + str(list1))

ACCESSING DATA USING TUPLE
tup1 = ('red', 'green', 9, 10);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];

DELETING DICTIONARY ELEMENT
dict = {"zayn" : 22, "harry" : 21, "jazz" : 21, "arya" : 21}  
print ("The dictionary before performing remove is : " + str(dict)) 
del dict['jazz'] 
print ("The dictionary after remove is : " + str(dict)) 
