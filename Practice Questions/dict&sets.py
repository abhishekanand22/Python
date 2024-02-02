 # Dict 

student_info={
    "Name" : "Abhishek",
    "Age" : 22,
    "Location" : "Jaipur",
    "Subjects_marks" :{
        "Phy" : 80,
        "Chem" : 88,
        "Bio" : 90
    },
    "Language" : "Hindi",
    "random" : ["true","false"]
}


# print all keys 
print(student_info.keys())


# print all values 
print(student_info.values())


# Return all pairs as tuple
print(student_info.items())


# return key according to value
print(student_info.get("Name"))


# update / add to dictionary
student_info.update({"contact" : "987654321"})
add_dict={
    "States Visited" : "Rajasthan , Uttar Pradesh , West Bengal , Bihar",
    "Languages Known" : "Hindi , English , Maithili",
    "Current Location" : "Lucknow"
}
student_info.update(add_dict)
print(student_info)


# Sets

collection=set()   #declaration 
names={'abhishek','anand'}
# add to set
collection.add(12)
collection.add(16)
collection.add(18)
collection.add(20)
collection.add(28)
collection.add(24)
collection.add('abhishek')

print("Set = ",collection)


# remove from set
collection.remove(24)


print("New Set =" ,collection)

#pop random values
print(collection.pop())

# add two sets
new_set=collection.union(names)
print(new_set)

#find intersection 
print(collection.intersection(names))


# user input

marks={}

x=int(input("enter Phy:"))
marks.update({"Phy" : x})

x=int(input("enter Chem:"))
marks.update({"Chem" : x})

x=int(input("enter Maths:"))
marks.update({"Maths" : x})

print(marks)

values ={9,"9.0"}
print(values)