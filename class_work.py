print("Class Work number 1")

#Exercise 1 first and third 

age = 24
print('My age is: ', age)



#Exercise 1 second and third        

name = 'Daniel'
print('and my name is: ', name)


#Exercise 2

x = 10
y = 5

sum = x+y

print('the sum of x + y is: ',sum)
print(f"other options include subtruction: {x-y} \n multiplication: {x*y}\n and division: {x/y}")

#Exercise 3

a = 3
b = 7

#Solution 1

c=a
a=b
b=c
print(a,',',b)


#Solution 2
a, b = b, a

print(f"{a},{b}")



#Exercise 4
length_input = input("Enter the length of teh rectangle please:")
length=int(length_input)
width_input = input("Enter the width of teh rectangle please:")
width=int(width_input)

area = length*width
print("The area is:",area)


#Exercise 5
word= 'greetings'
#print(word)
new_word = word.replace('greetings','Hello World!')
print(new_word)

greetings='Hello World!'
print(len(greetings))
print(greetings[0],greetings[-1])

#Exercise 6
first_name = 'Daniel'
Last_name = ' Miroshnichenko'

full_name=first_name+Last_name
print('Your irl whoami is: ',full_name)
#print(f"{first_name}{Last_name}")

#Exercise 7
print(f"My name is {full_name}and I am {age} years old")

#Exercise 8

quote='To be or not to be, that is the question.'
print(quote.upper(),'\n',quote.lower())

#Exercise 9
word_slice = 'Python'

print(word_slice[:3])
print(word_slice[3:])
print(word_slice[::-1])

#Exercise 10

sentence='I love programming in Python.'
print(sentence.replace('Python','Assembly'))

#Exercise 11

text = 'The quick brown fox jumps over the lazy dog'
random_word='fox'
new_random_word='cat'
is_present=random_word in text
is_present1=new_random_word in text
print("Word status appears in the text: ",is_present)
print("Word status appears in the text: ",is_present1)

#Exercise 12

mylist = ["apple", "banana", "orange"]
print(mylist)
mylist.append('melon')
print(mylist)
mylist.remove("apple")
del mylist[0]
print(mylist)

#Exercise 13

animals = ["cat", "dog", "rabbit", "hamster"]
print(animals[0])
print(animals[-1])
print(len(animals))

#Exercise 14

List=[5, 10, 15, 20, 25]

List[1]=12
print(List)

List.append(30)

print(List)

print(List.pop())

del List[-1]

print(List)


#Exercise 15

new_List=[1,2,3,4,5,6,7,8,9,10]
print(new_List[0:5])
print(new_List[-3:])
print(new_List[::-1])
new_List.sort(reverse=True)
print(new_List)

#Exercise 16
list_of_numbers=[1,2,3,4,5]
power = [i**2 for i in list_of_numbers]
print(power)


#Exercise 17
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_counter = fruits.count('apple')
print(fruit_counter)

#Exercise 18
colors = ['red', 'green', 'blue',  'yellow', 'blue']
occurance=colors.index('blue')
print(occurance)

#Exercise 19
list_number_1=[1, 2, 3]
list_number_2=[4, 5, 6]
list_number_3=list_number_1+list_number_2
print(list_number_3)

#Exercise 20
def remove_all(last,value):
    while value in last:
        last.remove(value) 
numbers = [1, 2, 2, 3, 4, 2]
remove_all(numbers,2)
print(numbers)

#Exercise 21


