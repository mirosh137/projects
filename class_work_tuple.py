print("Class Work number 2")

print("Section 1: Tuples")

#Exercise 1
my_tuple=(1,2,3)
print(my_tuple)
print(my_tuple[1])

#Exercise 2
person=('Daniel',24,'Petach Tikva')
name=person[0]
age=person[1]
city=person[2]
print(person,name,age,city)


#Exercise 3
tuple_1=(1,2,3)
tuple_2=(4,5,6)
nested_tuple=tuple_1+tuple_2
print("This is the nested tuple: ",nested_tuple)
print(f"This is the specific number in the nested tuple: {nested_tuple[4]}")

#Exercise 4
numbers=(1,2,3,2,4,2)
appearance = numbers.count(2)
print(appearance)



print("Section 2: Dictionaries")

#Exercise 1
student={
    "name": "Daniel",
    "age": 24,
    "grade": 92
}
print(student["name"])

#Exercise 2
student.update({"age": 25})
print(student)

student.pop("grade")
print(student)


if "grade" in student:
    x = True
else:
    x = False
print("The grade is in the dictionary:",x)        

#Exercise 3
capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
for country, capital in capitals.items(): 
    print(f"The capital of {country} is {capital}")

#Exercise 4


#Exercise 5

print("Section 3: Sets")

#Exercise 1
#Exercise 2
#Exercise 3
#Exercise 4
#Exercise 5
