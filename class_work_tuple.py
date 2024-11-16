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
countries= capitals.keys()
print("these are the countries: ", countries)

cities= capitals.values()
print("these are the countries: ", cities)

items= capitals.items()
print("these are the countries: ", items)

get=capitals.get("Germany")
print("there is no Germany, ", get,"!")


#Exercise 5
def count_chars(text):

    char_counter = {}

    for char in text:
        if char in char_counter:
            char_counter[char] = char_counter[char] + 1
        else:
            char_counter[char] = 1
    return char_counter 

text = 'hello'
result = count_chars(text)
print(result)


text1 = 'wassup?'
number_list = list(text1)
print(number_list)
dict1 = {}
count = 0
for char in number_list:
    if char in dict1:
        dict1[char] = dict1[char] + 1
        #count = count + 1
    else:
        dict1[char] = 1



print(number_list," \n" , dict1)

print("Section 3: Sets")

#Exercise 1
my_set={1,2,3,4,5}
my_set.add(6)
my_set.add(3)  # won't add because it is a duplicate
my_set.remove(2)
print("this is your new set:\n",my_set)

#Exercise 2
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

set_c = set_a.union(set_b)
print(set_c)

set_c = set_a.intersection(set_b)
print("the duplicates are",set_c)

set_c = set_a.difference(set_b)
set_d = set_b.difference(set_a)
print(set_c,set_d)

set_e = set_a.symmetric_difference(set_b)
print(set_e)

#Exercise 3
numbers = [1, 2, 2, 3, 4, 4, 5]
#new_set = list(set(numbers))
new_set = set(numbers)

print(new_set)

#Exercise 4
if 3 in set_a:
     True
     print("The number is in the set")
if not 6 in set_a:
    True
    print("The number is not in the set")

#Exercise 5
set_b.add(7)
print(set_b)

set_b.remove(4)
print(set_b)

set_a.discard(1)
print(set_a)




