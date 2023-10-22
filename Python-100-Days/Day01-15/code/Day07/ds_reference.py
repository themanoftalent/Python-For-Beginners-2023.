#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

print ('A Very Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']


# mylist is just another name pointing to the same object!
mylist = shoplist

# I purchased the first item, so I remove it from the list
del shoplist[0]

print ('shoplist is', shoplist)
print ('mylist is', mylist)
# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object
print ("---" * 14)
print ('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]

print ('shoplist is', shoplist)
print ('mylist is', mylist)
# Notice that now the two lists are different
