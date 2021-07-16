# slicing = create a substring by extracting elements from another string 
#           indexing [] or slice()
#           [start:stop:step]

#Example indexing[]
name = "Bro Code"

#Editor will automatic start with 0 if not type in
#[this start from 0 : this start from 1]
first_name = name[:3]
last_name = name[4:]
third_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(third_name)
print(reversed_name)

#Example slice()

website = "http://google.com"
website1 = "http://wikipedia.com"
#,
slice = slice(7,-4)

print(website[slice])
print(website1[slice])