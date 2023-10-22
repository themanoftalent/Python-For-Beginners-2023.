print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
print(type(shoplist))
# mylist is just another name pointing to the same object!
mylist = shoplist


print('shoplist is', shoplist)
print('mylist is', mylist)
# I purchased the first item, so I remove it from the list
del shoplist[0]


# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object

print('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0] #deleting from the list

print('\nshoplist is', shoplist)
print('mylist is', mylist)
# Notice that now the two lists are different
