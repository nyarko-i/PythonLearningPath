# Dictionaries
band = {
    "vocals": "Plant",
    "Guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(type(band))
print(band2)

print(band["vocals"])
print(band.get("Guitar"))

#list all values 
print(band.values())


#list all items
print(band.items())

# verify a key exist
print("Guitar" in band)
print("Triangle" in band)


# change values 
band["vocals"] = "Coverdale"
band.update({"base": "JPJ"})

print(band)

print(band.pop("base"))
print(band)

band['drums'] = "Bonham"
print(band)

print(band.popitem())
print(band)

# delete and clear item

band['drums'] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries

# band2 = band # creates a reference 
# print("Bad copy!")
# print(band2)
# print(band)

# band2['drums'] = "dave"
# print(band)

band2 = band.copy()
band2['drums'] = 'Dave'
print("good copy!")
print(band)
print(band2)


## Using dictionary constructor function 

band3 = dict(band)
print("Good copy")
print(band3)

# Nested Dictionaries 

number1 = {
    "name": "plant",
    "instrument": "vocals"
}

number2 = {
    "name": "page",
    "instrument": "guiatar"
    
}


band = {
    'member1': number1,
    'member2': number2
}

print(band)

## Sets 
nums = { 1, 2, 3, 4}
nums2 = set((1,2,3,4))

print(nums)
print(type(nums))
print(nums2)

# No duplicate allowed 

nums = {1,3,3,5}
print(nums)


## True is a dupe of 1 and False is a dupe of zero
nums = {1, True, 2, False, 3,4,0}
print(nums)

print(2 in nums)
# but you cannot refer to an element in the set with an index position or a key 

# Add a mew element to a set 
nums.add(8)
print(nums)

# Add element from one set to another 
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# You can use update with list, tuple, and dictionaries too 


# merge two sets to create a new set 
one = {1,2,3}
two ={5,6,7}

myNewSet = one.union(two)
print(myNewSet)

# Keep only the duplicates 
one = {1,2,3}
two ={5,2,7}

one.intersection_update(two)
print(one)

# Keep everything except  the duplicates 
one = {1,2,3}
two ={5,2,7,3}

one.symmetric_difference_update(two)
print(one)




