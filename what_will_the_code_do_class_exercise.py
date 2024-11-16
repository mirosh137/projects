#will output the power of 2 of every even number

for i in range(1, 10):
 if i % 2 == 0:
    print(i * i) # print(i * 2)


# will print elloh

word = "hello"
new_word = word[1:] + word[0]
print(new_word)

#will output the square of every odd number because of n % 2 == 1

numbers = [1, 2, 3, 4, 5]
squared_numbers = [n ** 2 for n in numbers if n % 2 == 1]
print(squared_numbers)



#will output 10

fruits = {"apple": 3, "banana": 5, "cherry": 2}
total = 0
for fruit in fruits:
 total += fruits[fruit]
print(total)

#will output the inverted word

text = "Python"
result = ""
for char in text:
 result = char + result
print(result)

#will return {1,4}, because it return the values that are not in both sets

set_a = {1, 2, 3}
set_b = {2, 3, 4}
result = set_a.symmetric_difference(set_b)
print(result)

#will return hello stranger beacause of greet() and afterwards hello alice because of greet("Alice")

def greet(name="stranger"):
 print(f"Hello, {name}!")
greet()
greet("Alice")


#this code counts the amount of instances the letter 's' appears in the given string it will return 4

sentence = "This is a simple sentence."
count = sentence.count("s")
print(count)


#will print False

x = 10
y = 5
z = x > y and y < 0 or x < 0 #prints False
#z = x > y and y > 0 or x > 0 #prints True
print(z)
print(type(z)) #bool


#The next lines of code will return 1, 4, 7 every number till 10 with jumps of 3 because of n+=3 (n=n+3)

n = 1
while n < 10:
    print(n)
    n += 3

#this lines on the other hand will return 4, 7, 10
n = 1
while n < 10:
    n += 3
    print(n)


values = (1, 2, 3)
print(values)
a, b, c = values #this line allocates the values from the values tuple
print(a, b, c)
print(a + b + c)

#will print 30
data = [10, 20, 30, 40, 50]
print(data[-3])


#this will update the value of a field in the dictionary to 26

info = {"name": "Alice", "age": 25}
info["age"] = 26
print(info)
 

#it will print 2, 5, 8 although it is very weird and I have no real idea how it does that

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [row[1] for row in matrix]
print(result)











